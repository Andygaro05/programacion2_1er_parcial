from hospital import *
from persona import *
from medico import *
from cita import *
from handler import *
from datetime import datetime

# Crear un hospital
hospital = Hospital("Hospital XYZ", "Carrera 100# random")
hospital.__repr__()

# Crear médicos
medico1 = Medico("Dr. García", "Cardiología")
medico2 = Medico("Dra. López", "Pediatría")
medico3 = Medico("Dra. Ramires", "Psiquiatria")

print(medico1.__repr__())
print(medico2.__repr__())

print(medico1.esta_disponible(datetime(2024, 11, 22, 10))) #esta disponible funciona bien

# Agregar las instancias a medicos
medicos = Medicos()
medicos.agregar_medico(medico1)
medicos.agregar_medicos([medico2, medico3])

print(medicos.__repr__())

medicoxespecialidad = medicos.buscar_medico_especialidad("Psiquiatria")
print(medicoxespecialidad.__repr__())

# # Crear personas
persona1 = Persona("Juan Pérez", 12345678, "1234567890", "juan@example.com", datetime.now().strftime('%Y-%m-%d'), medico1)
persona2 = Persona("Ana López", 87654321, "9876543210", "ana@example.com", datetime.now().strftime('%Y-%m-%d'), medico2)

# Crear citas
cita1 = Cita(persona1, medico1, datetime(2024, 11, 22, 10))
medico1.agregar_cita(cita1)

cita1.confirmar()
print(cita1.estado)

cita1.cancelar()
print(cita1.estado)

# personas = Personas()
# personas.agregar_personas([persona1, persona2])

# # Buscar médicos por especialidad
# cardiologos = medicos.buscar_medico_especialidad("Cardiología")
# print(cardiologos)

# # Mostrar información de las personas
# print(personas)

# cita1 = Cita(persona1, medico1, datetime(2024, 11, 22, 10))

# # Agregando la cita al médico y a citas
# medico1.agregar_cita(cita1)
# citas = Citas()
# citas.agregar_cita(cita1)  

# # Confirmando la cita
# cita1.confirmar()

# # Buscando citas de un médico
# citas_del_medico1 = medico1.citas
# print(citas_del_medico1)


