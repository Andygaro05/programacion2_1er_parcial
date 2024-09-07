from cita import *
class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = {dia: 
                        {hora: True for hora in range(7, 21)} 
                        for dia in range(1, 8)
                        }  # Horario estándar de 7am a 9pm
        self.citas_confirmadas = []
        self.citas = []
    

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def __repr__(self):
        return f"{self.nombre}, {self.especialidad}"

class Medicos:
    def __init__(self):
        self.medicos = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_medico_especialidad(self, especialidad):
        return [medico for medico in self.medicos if medico.especialidad == especialidad]