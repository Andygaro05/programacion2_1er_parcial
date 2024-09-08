# Sistema de Gestión de Citas Médicas

## Descripción General
Este proyecto es un sistema de gestión de citas médicas desarrollado en Python. Permite:

* **Registrar pacientes y médicos.**
* **Agendar citas.**
* **Cancelar citas.**
* **Buscar citas por paciente, médico o fecha.**
* **Generar reportes.**

## Estructura del Proyecto
* **hospital.py:** Define el hospital (singleton).
* **medico.py:** Gestiona información de los médicos y sus horarios.
* **cita.py:** Maneja la creación y gestión de citas.
* **persona.py:** Representa a los pacientes.
* **handler.py:** Implementa el patrón Chain of Responsibility para la reserva de citas.
* **notificar.py:** Gestiona las notificaciones (WhatsApp, correo, SMS).
* **main.py:** Punto de entrada del programa.
* **reporte.py** Crea y gestiona los reportes

## Instalación
```bash
pip install -r requirements.txt
```

Usa el código con precaución.

Uso
Bash
python main.py
Usa el código con precaución.

Contribuciones
¡Las contribuciones son bienvenidas! Abre un issue en GitHub.

Licencia
MIT License

Próximos Pasos
Interfaz de usuario
Base de datos
Escalabilidad
Seguridad

Autores
Andres Felipe Londoño Mendieta

