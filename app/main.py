from hospital import *
from persona import *
from medico import *
from cita import *
from handler import *
from reporte import *
from datetime import datetime

# Crear un hospital
hospital = Hospital("Hospital XYZ", "Carrera 100# random")
print(f"Bienvenido al sistema de citas medicas del {hospital.nombre}" )

# Crear médicos
medico1 = Medico("Dr. García", "Cardiología")
medico2 = Medico("Dra. López", "Pediatría")
medico3 = Medico("Dra. Ramires", "Psiquiatria")
medico4 = Medico("Dr. Gómez", "Ginecología")
medico5 = Medico("Dr. Pérez", "Oftalmología")
medico6 = Medico("Dr. Sánchez", "Ortopedia")
medico7 = Medico("Dr. Díaz", "Neurología")
medico8 = Medico("Dr. Hernández", "Urología")
medico9 = Medico("Dr. Moreno", "Dermatología")
medico10 = Medico("Dr. Torres", "Endocrinología")

medicos = Medicos()
medicos.agregar_medico(medico1)
medicos.agregar_medicos([medico2, medico3,medico4, medico5, medico6, medico7, medico8, medico9, medico10])

# # Crear personas
persona1 = Persona("Juan Pérez", 12345678, "1234567890", "juan@example.com", datetime.now().strftime('%Y-%m-%d'), medico1)
persona2 = Persona("Ana López", 87654321, "9876543210", "ana@example.com", datetime.now().strftime('%Y-%m-%d'), medico2)

# Crear citas
citas = Citas()

#Crear objeto reporte
reporte = Reporte(citas) 


def menu_principal():
    while True:
        print("\nMenú principal:")
        print("1. Ver lista de médicos")
        print("2. Buscar médico por especialidad")
        print("3. Reservar cita")
        print("4. Cancelar cita")
        print("5. Ver mis citas")
        print("6. Ver reporte de citas (Medico mas agendado)")
        print("7. Ver reporte de citas (Motivo de cancelación mas común)")
        print("8. Exportar a excel")
        print("9. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            #mostrar medicos
            print("Nuestros doctores siempre estan listos para atenderte a continuación nuestra lista de medicos con sus especialidades")
            print(medicos.__repr__())
            pass

        elif opcion == '2':
            #Mostrar especialidad
            print("Especialidades")
            print(medicos.__repr__())

            especialidad = input("Ingrese la especialidad del médico que busca: ")
            medicoxespecialidad = medicos.buscar_medico_especialidad(especialidad)
            print(medicoxespecialidad.__repr__())
            pass

        elif opcion == '3':
            #Reservar cita
            nombre = input("Ingresa tu nombre completo: ")
            cc = int(input("Ingresa tu cedula: "))
            celular = input("Ingresa tu celular: ")
            correo = input("Ingresa tu correo: ")
            especialidad_buscada = input("Ingrese la especialidad del médico que busca: ")
            medicos_utiles = medicos.buscar_medico_especialidad(especialidad_buscada)
            medico_asignado = medicos_utiles[0]

            mes = int(input("Ingresa el mes que te gustaria la cita ejemplo (10): "))
            dia = int(input("Ingresa el dia que te gustaria la cita: ejemplo (12): "))
            persona3 = Persona(nombre, cc, celular, correo, datetime.now().strftime('%Y-%m-%d'), medico_asignado=medico_asignado)
            
            request = Cita(
                paciente=persona3,
                medico=medico_asignado,
                fecha_hora=datetime(2024, mes, dia),
            )
            validate_handler = ValidateAvailabilityHandler(request)
            show_schedule_handler = ShowAvailableScheduleHandler(validate_handler).handle(request, medicos, citas)
            notificar = NotifyPatientHandler(show_schedule_handler).handle(request)
            print(request.estado)

        elif opcion == '4':
            # Cancelar cita
            persona3.cancelar_cita(request, citas)
            print(request.estado)
            pass
        elif opcion == '5':
            # Ver mis citas
            persona3.ver_citas(citas)
            pass
        elif opcion == '6':
            #ver reportes
            # Crear un objeto Reporte
            medico_mas_agendado, cantidad_citas = reporte.medico_mas_agendado()
            print(f"El médico más agendado es {medico_mas_agendado.nombre} con {cantidad_citas} citas.")

        elif opcion == '7':
            # Crear un objeto Reporte
            motivo_mas_comun, cantidad_cancelaciones = reporte.motivo_cancelacion_mas_comun()
            print(f"El motivo de cancelación más común es '{motivo_mas_comun}' con {cantidad_cancelaciones} cancelaciones.")
        
        elif opcion == '8':
            # Crear un objeto Reporte
            reporte.exportar_a_excel()

        elif opcion == '9':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()