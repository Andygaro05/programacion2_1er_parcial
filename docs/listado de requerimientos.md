#Requisitos funcionales:

##Para el usuario:

* El sistema debe permitir la reserva de citas para los pacientes
* El sistema debe validar si el paciente ya tiene un medico asignado
* El sistema debe verificar la disponibilidad de medicos según su especialidad
* El sistema debe asignar un medico a un paciente según su especialidad y disponibilidad
* El sistema debe mostrar los horarios para las citas
* El sistema debe permitir ver las citas agendadas, disponibles y canceladas
* El sistema debe permitir la cancelación de la cita
* El sistema debe almacenar el motivo de la cancelación
* El sistema debe permitir la liberación del espacio de una cita cancelada
* El sistema debe notificar al usuario 2 dias antes para confirmar y recordar la fecha hora de la cita 
* El sistema debe llevar un registro de información con los datos del usuario


##Para el medico:

* El sistema debe validar el calendario del medico y su disponibilidad
* El sistema debe permitir asignar un medico a un paciente para una cita
* El sistema debe llevar un registro de información con los datos del medico incluyendo su especialidad

##Para el gerente

* El sistema debe generar reportes de:
- Medico con mas demanda
- Motivos de cancelación

* El sistema debe permitir exportar los reportes a excel

#Requerimientos no funcionales
* Interfaz de texto (consola)
* Menu intuitivo
* Codigo Limpio y PEP-8 