#Requisitos funcionales:

##Para el usuario:

* El sistema debe verificar la disponibilidad de medicos según su especialidad
* El sistema debe validar si el paciente ya tiene un medico asignado
* El sistema debe asignar un medico a un paciente según su especialidad y disponibilidad
* El sistema debe permitir la reserva de citas para los pacientes
* El sistema debe mostrar los horarios para las citas
* El sistema debe permitir ver las citas agendadas y disponibles
* El sistema debe permitir ver los horarios ocupados y disponibles
* El sistema debe permitir la cancelación de la cita
* El sistema debe permitir la liberación del espacio de una cita cancelada
* El sistema debe contactar al usuario 2 dias antes para confirmar y recordar la fecha hora de la cita 
* El sistema debe llevar un registro de información con los datos del usuario

<!-- las citas se agendan cada 20 minutos en promedio -->
<!-- Contactar por SMS o notificación de la app -->

##Para el medico:

* El sistema debe validar el calendario del medico y su disponibilidad
* El sistema debe permitir asignar un medico a un paciente para una cita
* El sistema debe llevar un registro de información con los datos del medico incluyendo su especialidad

##Para el gerente

* El sistema debe permitir calcular el porcentaje de ausentismo y evaluar la eficiencia de consultas
* El sistema debe generar reportes de:
- Medico con mas demanda
- 

<!-- Reporte para poder analizar tendencia de citas a lo largo del tiempo -->

* El sistema debe permitir exportar los reportes a excel

#Requerimientos no funcionales
* Interfaz de texto (consola)
* Menu intuitivo
* Codigo Limpio y PEP-8 