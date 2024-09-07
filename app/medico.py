class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = {}  # Diccionario para almacenar el horario
        self.citas_confirmadas = []

    def __repr__(self):
        return f"{self.nombre}, {self.especialidad}"

class Medicos:
    def __init__(self):
        self.medicos = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_medico_especialidad(self, especialidad):
        return [medico for medico in self.medicos if medico.especialidad == especialidad]