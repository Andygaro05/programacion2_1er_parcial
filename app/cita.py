from medico import *
class Cita:
    def __init__(self, paciente, medico, fecha_hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def __repr__(self):
        return f"Cita con {self.medico.nombre} el {self.fecha_hora}"

class Citas:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def cancelar_cita(self, cita):
        for i, c in enumerate(self.citas):
            if c == cita:
                self.citas.pop(i)
                cita.estado = "cancelada"
                return True
        return False
    
    def ver_citas(self):
        if not self.citas:
            print("No hay citas registradas.")
        else:
            for cita in self.citas:
                print(cita)

    def buscar_citas_por_paciente(self, paciente):
        return print([cita for cita in self.citas if cita.paciente == paciente])

    def buscar_citas_por_medico(self, medico):
        return print([cita for cita in self.citas if cita.medico == medico])

    #pulir metodo
    def buscar_citas_por_fecha(self, fecha):
        return [cita for cita in self.citas if cita.fecha_hora.date() == fecha]
