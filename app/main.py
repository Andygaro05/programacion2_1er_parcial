from hospital import Hospital
from persona import *
from datetime import datetime

hospital = Hospital("Hospital XYZ", "Carrera 100# random")
hospital.__repr__()

# hospital = Hospital("XYZ", "prueba") #crashea demostrando asi que el singleton funciona 

# Creando algunas instancias de Persona
persona1 = Persona("Juan Pérez", 12345678, "1234567890", "juan@example.com", datetime.now(), None)
persona2 = Persona("Ana López", 87654321, "9876543210", "ana@example.com", datetime.now(), None)

# Creando una instancia de Personas
personas = Personas()

# Agregando personas a la lista
personas.agregar_persona(persona1)
personas.agregar_persona(persona2)

# Creando una lista de personas y agregándolas
nueva_lista_personas = [
    Persona("Pedro Gómez", 54321, "123456789", "pedro@example.com", datetime.now(), None),
    Persona("Maria Sánchez", 98765, "987654321", "maria@example.com", datetime.now(), None)
]
personas.agregar_personas(nueva_lista_personas)

print(personas)