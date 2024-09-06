class Hospital:
  __instance = None
  
  @staticmethod
  def get_instance():
      if Hospital.__instance == None:
          Hospital()
      return Hospital.__instance

  def __init__(self, nombre, direccion):
      self.nombre = nombre
      self.direccion = direccion
      if Hospital.__instance != None:
          raise Exception("Esta clase es un singleton")
      else:
          Hospital.__instance = self

  def __repr__(self) -> str:
     print(f"Hospital {self.nombre} ubicado en {self.direccion}")