from cita import *
from datetime import time
class Medico:
    def __init__(self, nombre, especialidad):
        """
        Inicializa un nuevo objeto Medico.

        Args:
            nombre (str): Nombre del médico.
            especialidad (str): Especialidad del médico.
        """
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = {dia: 
                        {time(hora): True for hora in range(7, 21)} 
                        for dia in range(1, 8)
                        }  # Horario estándar de 7am a 9pm
        self.citas_confirmadas = []
        self.citas = []

    def esta_disponible(self, fecha_hora):
        """
        Verifica si el médico está disponible en la fecha y hora especificadas.

        Args:
            fecha_hora (datetime): Objeto datetime que representa la fecha y hora.

        Returns:
            bool: True si está disponible, False si no.
        """
        dia, hora = fecha_hora.date().weekday() + 1, fecha_hora.hour
        return self.horario.get(dia, {}).get(hora, False)
    

    def agregar_cita(self, cita):
        """
        Agrega una cita al historial del médico.

        Args:
            cita (Cita): Objeto de la clase Cita.
        """
        self.citas.append(cita)

    def __repr__(self):
        """
        Devuelve una representación en cadena del objeto Medico.
        """
        return f"{self.nombre}, {self.especialidad}"

class Medicos:
    def __init__(self):
        """
        Inicializa una nueva lista de médicos.
        """
        self.medicos = []

    def agregar_medico(self, medico):
        """
        Agrega un médico a la lista.

        Args:
            medico (Medico): Objeto de la clase Medico.
        """
        self.medicos.append(medico)

    def agregar_medicos(self, medicos):
        """
        Agrega una lista de médicos a la lista existente.

        Args:
            medicos (list): Lista de objetos Medico.
        """
        for medico in medicos:
            self.medicos.append(medico)

    def buscar_medico_especialidad(self, especialidad):
        """
        Busca médicos por especialidad.

        Args:
            especialidad (str): Especialidad a buscar.

        Returns:
            list: Lista de médicos con la especialidad indicada.
        """
        return [medico for medico in self.medicos if medico.especialidad == especialidad]
    
    def __repr__(self):
        """
        Devuelve una representación en cadena de la lista de médicos.
        """
        return f"Lista de médicos: \n{'\n'.join(str(medico) for medico in self.medicos)}"