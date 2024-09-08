from abc import ABC, abstractmethod
from medico import *
from cita import *
from notificar import *

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
            # Si está disponible, continuar con el siguiente handler
            super().handle(request)
        else:
            print("El médico no está disponible a esa hora.")
class ShowAvailableScheduleHandler(Handler):
    def handle(self, request):
        # Obtener la especialidad del médico de la solicitud
        especialidad = request.medico.especialidad

        # Buscar médicos con la especialidad indicada
        medicos_con_especialidad = Medicos.buscar_medico_especialidad(especialidad)

        if medicos_con_especialidad:
            # Seleccionar el primer médico encontrado
            medico_seleccionado = medicos_con_especialidad[0]

            # Mostrar los horarios disponibles del médico seleccionado
            print("Horarios disponibles para: ", medico_seleccionado.nombre)
            for dia, horarios in medico_seleccionado.horario.items():
                for hora, disponible in horarios.items():
                    if disponible:
                        print(f"Día {dia}, Hora {hora}")

            # Si el usuario confirma la hora, continuar con la siguiente acción
            confirmar = input("¿Desea reservar esta cita? (s/n): ")
            if confirmar.lower() == 's':
                super().handle(request)
            else:
                print("Cita cancelada.")
        else:
            print("No se encontraron médicos disponibles para esa especialidad.")

class ConfirmarCitaHandler(Handler, Medicos):
    def handle(self, request):
        # Obtener la especialidad del médico de la solicitud
        especialidad = request.medico.especialidad
        print(especialidad)
        # Buscar médicos con la especialidad indicada
        medicos_con_especialidad = Medicos.buscar_medico_especialidad(especialidad)

        if medicos_con_especialidad:
            # Seleccionar el primer médico encontrado
            medico_seleccionado = medicos_con_especialidad[0]

            # Mostrar los horarios disponibles del médico seleccionado
            self._mostrar_horarios_disponibles(medico_seleccionado)

            # Obtener el horario seleccionado por el usuario
            horario_seleccionado = input("Ingrese el horario deseado (ejemplo: Día 1, Hora 10): ")

            # Validar el horario seleccionado
            if self._validar_horario(medico_seleccionado, horario_seleccionado):
                # Crear la instancia de la cita
                nueva_cita = Cita(request.paciente, medico_seleccionado, horario_seleccionado)

                # Agregar la cita a las citas confirmadas del médico y a la lista general de citas
                medico_seleccionado.citas_confirmadas.append(nueva_cita)
                citas = Citas()
                citas.agregar_cita(nueva_cita)

                print("Cita confirmada exitosamente.")
                # Agregar la cita a las citas confirmadas del médico y a la lista general de citas
                medico_seleccionado.citas_confirmadas.append(nueva_cita)
                citas.agregar_cita(nueva_cita)

                # Crear una cadena de responsabilidad para notificaciones
                notificacion_whatsapp = NotificacionWhatsapp()
                notificacion_correo = NotificacionCorreo(notificacion_whatsapp)
                notificacion_sms = NotificacionSMS(notificacion_correo)
            else:
                print("El horario seleccionado no está disponible.")
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
        print(f"Cita confirmada con {request.medico.nombre} el {request.fecha_hora}")
        super().handle(request)