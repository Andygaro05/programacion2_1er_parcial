import pandas as pd

class Reporte:
    """
    Clase para generar reportes a partir de un conjunto de citas médicas.

    Args:
        citas (Citas): Objeto que contiene la lista de citas.

    Attributes:
        citas (Citas): Referencia al objeto Citas.
    """
    def __init__(self, citas):
        """
        Constructor de la clase.

        Args:
            citas (Citas): Objeto que contiene la lista de citas.
        """
        self.citas = citas

    def medico_mas_agendado(self):
        """
        Determina el médico con más citas agendadas.

        Returns:
            tuple: Una tupla con el médico más agendado y la cantidad de citas.
        """
        contador_medicos = {}
        for cita in self.citas.citas:  # Aquí se itera sobre la lista de citas dentro del objeto Citas
            if cita.medico in contador_medicos:
                contador_medicos[cita.medico] += 1
            else:
                contador_medicos[cita.medico] = 1

        medico_mas_agendado = max(contador_medicos, key=contador_medicos.get)
        return medico_mas_agendado, contador_medicos[medico_mas_agendado]

    def motivo_cancelacion_mas_comun(self):
        """
        Determina el motivo de cancelación más común entre las citas.

        Returns:
            tuple: Una tupla con el motivo de cancelación más común y la cantidad de veces que se repite.
        """
        motivos_cancelacion = {}
        for cita in self.citas.citas:
            if cita.estado == 'cancelada':
                if cita.motivo_cancelacion in motivos_cancelacion:
                    motivos_cancelacion[cita.motivo_cancelacion] += 1
                else:
                    motivos_cancelacion[cita.motivo_cancelacion] = 1

        try:
            motivo_mas_comun = max(motivos_cancelacion, key=motivos_cancelacion.get)
            return motivo_mas_comun, motivos_cancelacion[motivo_mas_comun]
        except ValueError:
            print("No hay citas canceladas para calcular el motivo más común.")
            return None, 0

    def exportar_a_excel(self, nombre_archivo='reporte_citas.xlsx'):
        """
        Exporta los datos de las citas a un archivo Excel.

        Args:
            nombre_archivo (str, optional): Nombre del archivo Excel a generar.
                Por defecto: 'reporte_citas.xlsx'.
        """
        # Crear un DataFrame de pandas con los datos de las citas
        data = []
        for cita in self.citas:
            data.append([cita.paciente.nombre, cita.medico.nombre, cita.fecha_hora, cita.estado])

        df = pd.DataFrame(data, columns=['Paciente', 'Médico', 'Fecha y Hora', 'Estado'])

        # Exportar a Excel
        df.to_excel(nombre_archivo, index=False)