from abc import ABC, abstractmethod
from medico import *
from cita import *
from notificar import *
from datetime import datetime

class Handler(ABC):
    """
    Clase abstracta que define el patrón Chain of Responsibility para manejar solicitudes de citas.
    Esta clase representa un eslabón en la cadena de procesamiento de solicitudes.
    """
    def __init__(self, random, successor=None):
        """
        Inicializa un nuevo objeto Handler.

        Args:
            successor (Handler, opcional): El siguiente handler en la cadena.
        """
        self._successor = successor

    def handle(self, request): 
        """
        Maneja una solicitud. Si hay un siguiente handler en la cadena, delega el procesamiento a él.

        Args:
            request (Request): La solicitud a procesar.
        """
        if self._successor:
            self._successor.handle(request)

class ValidateAvailabilityHandler(Handler):
    """
    Valida la disponibilidad del médico para la cita solicitada.
    Si el médico está disponible, delega la solicitud al siguiente handler.
    """
    def handle(self, request):
        # Validar disponibilidad del médico
        if request.medico.esta_disponible(request.fecha_hora):
            # Si está disponible, continuar con el siguiente handler
            super().handle(request)
        else:
            print("El médico no está disponible a esa hora.")
class ShowAvailableScheduleHandler(Handler):
    """
    Muestra los horarios disponibles para un médico y permite al usuario seleccionar una hora.

    Args:
        request (Request): Objeto de solicitud que contiene la información de la cita.
        medicos (list): Lista de objetos Medico.
        citas (list): Lista de objetos Cita.

    Este handler realiza las siguientes acciones:
    1. Obtiene la especialidad del médico solicitada.
    2. Busca médicos disponibles con esa especialidad.
    3. Presenta al usuario los horarios disponibles del médico seleccionado.
    4. Permite al usuario seleccionar una hora.
    5. Si el usuario confirma la hora, delega la solicitud al siguiente handler.

    Raises:
        ValueError: Si la fecha ingresada por el usuario no es válida.
    """
    def handle(self, request, medicos, citas):
        # Obtener la especialidad del médico de la solicitud
        especialidad = request.medico.especialidad

        # Buscar médicos con la especialidad indicada
        medicos_con_especialidad = Medicos.buscar_medico_especialidad(medicos, especialidad)

        if medicos_con_especialidad:
            # Seleccionar el primer médico encontrado
            medico_seleccionado = medicos_con_especialidad[0]

            # Pedir al usuario que ingrese la fecha deseada
            fecha_deseada = request.fecha_hora
            # input("Ingrese la fecha deseada (formato: YYYY-MM-DD): ")
            try:
                pass
            except ValueError:
                print("Fecha inválida. Por favor, ingrese una fecha en formato YYYY-MM-DD.")
                return

            # Mostrar los horarios disponibles del médico seleccionado para la fecha deseada
            print("Horarios disponibles para: ", medico_seleccionado.nombre, " el ", datetime.strftime(fecha_deseada, '%y-%m-%d'))
            for dia, horarios in medico_seleccionado.horario.items():
                if dia == fecha_deseada.weekday() + 1:  # Ajustar el índice del día (0-6 -> 1-7)
                    for hora, disponible in horarios.items():
                        if disponible:
                            print(f"Hora {hora}")

            # Si hay horarios disponibles, continuar con la siguiente acción
            if any(horarios.values() for horarios in medico_seleccionado.horario.values()):
                hora_deseada_str = input("Ingrese la hora deseada (ejemplo: 10:00): ")
                try:
                    hora_deseada = datetime.strptime(hora_deseada_str, '%H:%M').time()
                    hora_deseada_str = str(hora_deseada)
                    if hora_deseada_str in map(str, medico_seleccionado.horario[dia]):
                            if medico_seleccionado.horario[dia][hora_deseada]:
                                # Si el usuario confirma la hora, continuar con la siguiente acción
                                confirmar = input("¿Desea reservar esta cita? (s/n): ")
                                if confirmar.lower() == 's':
                                    fecha_hora = datetime.combine(fecha_deseada, hora_deseada)
                                    request.fecha_hora = fecha_hora
                                    medico_seleccionado.agregar_cita(request)
                                    request.confirmar()
                                    citas.agregar_cita(request)
                                    super().handle(request)
                                else:
                                    print("Cita cancelada.")
                            else:
                                print("Hora inválida. Por favor, seleccione una hora disponible.")
                except ValueError:
                    print("Hora inválida. Por favor, ingrese una hora en formato HH:MM.")
                    return
            else:
                print("No hay horarios disponibles para esa fecha.")
        else:
            print("No se encontraron médicos disponibles para esa especialidad.")



    def _mostrar_horarios_disponibles(self, medico):
        """
        Muestra los horarios disponibles para un médico en particular.

        Args:
            medico (Medico): Objeto que representa al médico.

        Este método es utilizado internamente para presentar los horarios disponibles
        de un médico en un formato legible para el usuario.
        """
        print("Horarios disponibles para", medico.nombre)
        for dia, horarios in medico.horario.items():
            for hora, disponible in horarios.items():
                if disponible:
                    print(f"Día {dia}, Hora {hora}")

    def _validar_horario(self, medico, horario_seleccionado):
        """
        Valida si un horario seleccionado por el usuario es válido para el médico.

        Args:
            medico (Medico): Objeto que representa al médico.
            horario_seleccionado (str): Cadena que representa el horario seleccionado (ej: "Lunes 10:00").

        Returns:
            bool: True si el horario es válido, False en caso contrario.
        """
        try:
            dia, hora = horario_seleccionado.split(',')
            dia, hora = int(dia.strip()), int(hora.strip())
            return medico.horario.get(dia, {}).get(hora, False)
        except (ValueError, KeyError):
            return False

class NotifyPatientHandler(Handler):
    """
    Notifica al paciente sobre una cita médica programada.

    Args:
        request (Request): Objeto de solicitud que contiene la información de la cita.

    Este handler envía una notificación al paciente recordándole su próxima cita.
    La notificación se envía a través de la clase `Notificar`.

    **Pasos:**
    1. Crea una instancia de la clase `Notificar`.
    2. Construye un mensaje de notificación estándar.
    3. Envía la notificación al paciente utilizando el método `enviar_notificacion` de la clase `Notificar`.
    4. Imprime un mensaje en la consola para confirmar el envío de la notificación.

    **Nota:** El contenido del mensaje de notificación y el método de envío pueden ser personalizados en la clase `Notificar`.
    """
    def handle(self, request):
        # Notificar al paciente
        notificar = Notificar()
        mensaje = "Recuerde que tiene una cita medica en 2 dias"
        notificar.enviar_notificacion(request.paciente, mensaje=mensaje)
        print(f"Enviando mensaje a {request.paciente.nombre}")
        print(f"Persona notificada para la cita con {request.medico.nombre} el {request.fecha_hora}")