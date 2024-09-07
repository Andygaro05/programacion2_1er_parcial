from hospital import *
from persona import *
from medico import *
from datetime import datetime

# Crear un hospital
hospital = Hospital("Hospital XYZ", "Carrera 100# random")

# Crear médicos
medico1 = Medico("Dr. García", "Cardiología")
medico2 = Medico("Dra. López", "Pediatría")

# Agregar las instancias a medicos
medicos = Medicos()
medicos.agregar_medico(medico1)
medicos.agregar_medico(medico2)

# Crear personas
persona1 = Persona("Juan Pérez", 12345678, "1234567890", "juan@example.com", datetime.now().strftime('%Y-%m-%d'), medico1)
persona2 = Persona("Ana López", 87654321, "9876543210", "ana@example.com", datetime.now().strftime('%Y-%m-%d'), medico2)

personas = Personas()
personas.agregar_personas([persona1, persona2])

# Buscar médicos por especialidad
cardiologos = medicos.buscar_medico_especialidad("Cardiología")
print(cardiologos)

# Mostrar información de las personas
print(personas)