from cita import *
from medico import *
from datetime import datetime, timedelta

class Persona:
    def __init__(self, nombre, cc, celular, correo, fecha_nacimiento, medico_asignado):
        self.nombre = nombre
        self.cc = cc
        self.celular = celular
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.medico_asignado = medico_asignado

    def reservar_cita(self, medico, dia, hora):
        """Reserva una cita con el médico especificado en el día y hora dados.    
        
    Args:
        medico (Medico): El objeto Médico.
        dia (int): El día de la semana (1-7).
        hora (int): La hora (0-23).
    
    Returns:
        Cita: El objeto Cita creado, o None si no hay disponibilidad.
        """

        # Crear un objeto datetime a partir de dia y hora
        fecha_hora = datetime(2023, 1, 1) + timedelta(days=dia-1, hours=hora)

        if medico.esta_disponible(fecha_hora):
            cita = Cita(self, medico, fecha_hora)
            return cita
        else:
            return None
        
    def cancelar_cita(self,request, citas):
        """
    Cancela una cita y permite al usuario seleccionar un motivo de cancelación.

    Args:
        cita (Cita): La cita a cancelar.
        """

        motivos_cancelacion = ["Doble reserva", "Cambio de horario", "Otro"]

        print("Motivos de cancelación:")
        for i, motivo in enumerate(motivos_cancelacion, start=1):
            print(f"{i}. {motivo}")

        while True:
            try:
                motivo_seleccionado = int(input("Seleccione el motivo de cancelación (0 para cancelar): "))
                if motivo_seleccionado == 0:
                    return None
                elif 1 <= motivo_seleccionado <= len(motivos_cancelacion):
                    citas.cancelar_cita(request)
                    print(f"Cita cancelada. Motivo: {motivos_cancelacion[motivo_seleccionado - 1]}")
                
                    return motivos_cancelacion[motivo_seleccionado - 1]
                else:
                    print("Motivo de cancelación inválido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def ver_citas(self, citas):
        """Muestra todas las citas del paciente.

        Busca en la lista global de citas las que pertenecen a este paciente.
        """

        if not citas.citas:  # Assuming citas is a global variable
            print("No hay citas registradas.")
        else:
            print(f"Citas de {self.nombre}:")
            for cita in citas.citas:
                if cita.paciente == self:
                    print(cita)
    def __str__(self):
        """Retorna una Representación de cada paciente"""
        return f"Paciente {self.nombre} - {self.cc} Nacido en: {self.fecha_nacimiento}"

class Personas:
    def __init__(self):
        self.lista_personas = []

    def agregar_persona(self, persona):
        """Agrega una instancia de Persona a la lista de personas.

        Args:
            persona (Persona): La instancia de Persona a agregar.
        """
        self.lista_personas.append(persona)

    def agregar_personas(self, lista_personas):
        """Agrega una lista de instancias de Persona a la lista de personas.

        Args:
            lista_personas (list): Una lista de instancias de Persona.
        """
        self.lista_personas.extend(lista_personas)

    def __str__(self):
        """Devuelve una representación legible de todas las personas."""
        return "\n".join(str(persona) for persona in self.lista_personas)