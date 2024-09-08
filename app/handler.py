from abc import ABC, abstractmethod
from medico import *
from cita import *
from notificar import *
from datetime import datetime

class Request:
    def __init__(self, paciente, medico, fecha_hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora

    def __str__(self) -> str:
        return f"cita el dia {self.fecha_hora} con el medico {self.medico}"
class Handler(ABC):
    def __init__(self, random, successor=None):
        self._successor = successor

    def handle(self, request): 

        if self._successor:
            self._successor.handle(request)

class ValidateAvailabilityHandler(Handler):
    def handle(self, request):
        # Validar disponibilidad del médico
        if request.medico.esta_disponible(request.fecha_hora):
            print("Esta entrando en el if")
            # Si está disponible, continuar con el siguiente handler
            super().handle(request)
        else:
            print("El médico no está disponible a esa hora.")
class ShowAvailableScheduleHandler(Handler):
    def handle(self, request, medicos):
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
        print("Horarios disponibles para", medico.nombre)
        for dia, horarios in medico.horario.items():
            for hora, disponible in horarios.items():
                if disponible:
                    print(f"Día {dia}, Hora {hora}")

    def _validar_horario(self, medico, horario_seleccionado):
        try:
            dia, hora = horario_seleccionado.split(',')
            dia, hora = int(dia.strip()), int(hora.strip())
            return medico.horario.get(dia, {}).get(hora, False)
        except (ValueError, KeyError):
            return False

class NotifyPatientHandler(Handler):
    def handle(self, request):
        # Notificar al paciente
        notificar = Notificar()
        mensaje = "Recuerde que tiene una cita medica en 2 dias"
        notificar.enviar_notificacion(request.paciente, mensaje=mensaje)
        print(f"Enviando mensaje a {request.paciente.nombre}")
        print(f"Persona notificada para la cita con {request.medico.nombre} el {request.fecha_hora}")