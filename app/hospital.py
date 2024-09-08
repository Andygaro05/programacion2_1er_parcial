class Hospital:
  """
    Clase Singleton que representa un hospital.

    Esta clase garantiza que solo exista una instancia del hospital en todo el programa.
  """
  __instance = None
  
  @staticmethod
  def get_instance():
    """
        Obtiene la única instancia del hospital.

        Returns:
            Hospital: La instancia del hospital.
    """

    if Hospital.__instance == None:
        Hospital()
    return Hospital.__instance

  def __init__(self, nombre, direccion):
    """
        Inicializa un nuevo objeto Hospital.

        Args:
            nombre (str): Nombre del hospital.
            direccion (str): Dirección del hospital.

        Raises:
            Exception: Si se intenta crear una segunda instancia del hospital.
    """
    self.nombre = nombre
    self.direccion = direccion
    if Hospital.__instance != None:
        raise Exception("Esta clase es un singleton")
    else:
        Hospital.__instance = self

  def __repr__(self) -> str:
    """
        Devuelve una representación en cadena del objeto Hospital.

        Returns:
            str: La representación en cadena del hospital.
    """
    print(f"Hospital {self.nombre} ubicado en {self.direccion}")