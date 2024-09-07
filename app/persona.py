from cita import *
class Persona:
    def __init__(self, nombre, cc, celular, correo, fecha_nacimiento, medico_asignado):
        self.nombre = nombre
        self.cc = cc
        self.celular = celular
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.medico_asignado = medico_asignado

    def reservar_cita(self, medico, dia, hora):
        if medico.esta_disponible(dia, hora):
            cita = Cita(self, medico, dia, hora)
            return cita
        else:
            return None

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