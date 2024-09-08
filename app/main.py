from hospital import *
from persona import *
from medico import *
from cita import *
from handler import *
from datetime import datetime, timedelta

# Crear un hospital
hospital = Hospital("Hospital XYZ", "Carrera 100# random")
hospital.__repr__()

# Crear médicos
medico1 = Medico("Dr. García", "Cardiología")
medico2 = Medico("Dra. López", "Pediatría")
medico3 = Medico("Dra. Ramires", "Psiquiatria")

# print(medico1.__repr__())
# print(medico2.__repr__())

# medico1.esta_disponible(datetime(2024, 11, 22, 10)) #esta disponible funciona bien

# Agregar las instancias a medicos
medicos = Medicos()
medicos.agregar_medico(medico1)
medicos.agregar_medicos([medico2, medico3])

# print(medicos.__repr__())

medicoxespecialidad = medicos.buscar_medico_especialidad("Psiquiatria")
# print(medicoxespecialidad.__repr__())

# # Crear personas
persona1 = Persona("Juan Pérez", 12345678, "1234567890", "juan@example.com", datetime.now().strftime('%Y-%m-%d'), medico1)
persona2 = Persona("Ana López", 87654321, "9876543210", "ana@example.com", datetime.now().strftime('%Y-%m-%d'), medico2)

# Crear citas
citas = Citas()
cita1 = Cita(persona1, medico1, datetime(2024, 11, 22, 10))
medico1.agregar_cita(cita1)

cita1.confirmar()
print(cita1.estado)

cita1.cancelar()
print(cita1.estado)

citas.agregar_cita(cita1)
citas.ver_citas()
citas.cancelar_cita(cita1)
citas.ver_citas()

##Pruebas personas
print(medico3.esta_disponible(datetime(2024, 11, 22, 10)))

persona3 = Persona("Ricardo molina", 87654332, "9876543222", "ricardo@example.com", datetime.now().strftime('%Y-%m-%d'), medico3)
persona3.reservar_cita(medico3,3,5)
cita2 = Cita(persona3, medico3, datetime(2024, 11, 22, 10))
citas.agregar_cita(cita2)
citas.ver_citas()

# persona3.cancelar_cita(cita2)
#prueba chain of responsability:07:00
request = Request(
    paciente=persona3,
    medico=medico3,
    fecha_hora=datetime(2024, 12, 23),
)

# Crear la cadena de responsabilidad
validate_handler = ValidateAvailabilityHandler(request)
show_schedule_handler = ShowAvailableScheduleHandler(validate_handler).handle(request, medicos)
notificar = NotifyPatientHandler(request).handle(request)
