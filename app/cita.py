from medico import *
class Cita:
    """
    Representa una cita médica.

    Atributos:
        paciente (Paciente): Objeto que representa al paciente.
        medico (Medico): Objeto que representa al médico.
        fecha_hora (datetime): Fecha y hora de la cita.
        estado (str): Estado actual de la cita (pendiente, confirmada, cancelada).

    Métodos:
        confirmar(): Cambia el estado de la cita a "confirmada".
        cancelar(): Cambia el estado de la cita a "cancelada".
        __repr__(): Devuelve una representación en cadena de la cita.
    """
    def __init__(self, paciente, medico, fecha_hora):
        """
        Inicializa una nueva instancia de la clase Cita.

        Args:
            paciente (Paciente): Objeto que representa al paciente.
            medico (Medico): Objeto que representa al médico.
            fecha_hora (datetime): Fecha y hora de la cita.
        """
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.estado = "pendiente"

    def confirmar(self):
        """
        Confirma la cita cambiando su estado a "confirmada".
        """
        self.estado = "confirmada"

    def cancelar(self):
        """
        Cancela la cita cambiando su estado a "cancelada".
        """
        self.estado = "cancelada"

    def __repr__(self):
        """
        Devuelve una representación en cadena de la cita en un formato legible.

        Returns:
            str: Una cadena que representa la cita.
        """
        return f"Cita con {self.medico.nombre} el {self.fecha_hora}"

class Citas:
    """
    Representa una colección de citas médicas.

    Atributos:
        citas (list): Lista de objetos Cita.

    Métodos:
        agregar_cita(cita): Agrega una nueva cita a la lista.
        cancelar_cita(cita): Cancela una cita existente.
        ver_citas(): Muestra todas las citas registradas.
        buscar_citas_por_paciente(paciente): Busca y muestra las citas de un paciente específico.
        buscar_citas_por_medico(medico): Busca y muestra las citas de un médico específico.
        buscar_citas_por_fecha(fecha): Busca y devuelve las citas de una fecha específica.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Citas.
        """
        self.citas = []

    def agregar_cita(self, cita):
        """
        Agrega una nueva cita a la lista de citas.

        Args:
            cita (Cita): Objeto de la clase Cita a agregar.
        """
        self.citas.append(cita)

    def cancelar_cita(self, cita):
        """
        Cancela una cita existente.

        Args:
            cita (Cita): Objeto de la clase Cita a cancelar.

        Returns:
            bool: True si la cita fue encontrada y cancelada, False en caso contrario.
        """
        for i, c in enumerate(self.citas):
            if c == cita:
                self.citas.pop(i)
                cita.estado = "cancelada"
                return True
        return False
    
    def ver_citas(self):
        """
        Muestra todas las citas registradas en la consola.
        """
        if not self.citas:
            print("No hay citas registradas.")
        else:
            for cita in self.citas:
                print(cita)

    def buscar_citas_por_paciente(self, paciente):
        """
        Busca y muestra las citas de un paciente específico.

        Args:
            paciente (Paciente): Objeto que representa al paciente.
        """
        return print([cita for cita in self.citas if cita.paciente == paciente])

    def buscar_citas_por_medico(self, medico):
        """
        Busca y muestra las citas de un médico específico.

        Args:
            medico (Medico): Objeto que representa al médico.
        """
        return print([cita for cita in self.citas if cita.medico == medico])

    #pulir metodo
    def buscar_citas_por_fecha(self, fecha):
        """
        Busca y devuelve las citas de una fecha específica.

        Args:
            fecha (date): Objeto datetime.date que representa la fecha.

        Returns:
            list: Lista de citas que coinciden con la fecha.
        """
        return [cita for cita in self.citas if cita.fecha_hora.date() == fecha]
