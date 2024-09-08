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
        
    def cancelar_cita(self, cita, motivos_cancelacion):
        """
        Cancela una cita y permite al usuario seleccionar un motivo.

        Args:
            cita (Cita): La cita a cancelar.
            motivos_cancelacion (list): Lista de motivos de cancelación posibles.
        """

        print("Motivos de cancelación:")
        for i, motivo in enumerate(motivos_cancelacion):
            print(f"{i+1}. {motivo}")

        motivo_seleccionado = int(input("Seleccione el motivo de cancelación: ")) - 1

        # Validar que el motivo seleccionado sea válido
        if 0 <= motivo_seleccionado < len(motivos_cancelacion):
            cita.cancelar()
            print(f"Cita cancelada. Motivo: {motivos_cancelacion[motivo_seleccionado]}")
            # Aquí puedes agregar lógica para notificar al médico, etc.
        else:
            print("Motivo de cancelación inválido.")

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