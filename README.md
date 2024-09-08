# Sistema de Gestión de Citas Médicas

## Descripción general
Este proyecto en Python implementa un sistema simple para gestionar citas médicas en un hospital. Permite a los usuarios:

* **Reservar citas:** Verificando la disponibilidad del médico y confirmando la cita.
* **Cancelar citas:** Con diferentes motivos de cancelación.
* **Buscar citas:** Por paciente, médico o fecha.
* **Gestionar médicos:** Agregar, buscar y ver horarios.

## Estructura del proyecto
* **hospital.py:** Define la clase `Hospital` (singleton) para representar el hospital.
* **medico.py:** Define la clase `Medico` para representar a los médicos y sus horarios.
* **cita.py:** Define las clases `Cita` y `Citas` para gestionar las citas.
* **persona.py:** Define las clases `Persona` y `Personas` para representar a los pacientes.
* **handler.py:** Implementa el patrón Chain of Responsibility para manejar la lógica de reserva de citas.
* **notificar.py:** Define las clases para enviar notificaciones (WhatsApp, correo, SMS).
* **main.py:** El punto de entrada del programa, donde se crean los objetos y se realizan las pruebas.

## Instalación
Para ejecutar este proyecto, asegúrate de tener Python instalado. Puedes instalar las dependencias adicionales usando pip:

```bash
pip install -r requirements.txt
```

## USO
python main.py

¡Claro! Aquí tienes el README.md en un formato que puedes copiar y pegar directamente en tu archivo de Markdown, con algunas mejoras adicionales:

Markdown
# Sistema de Gestión de Citas Médicas

## Descripción General
Este proyecto Python implementa un sistema simple para gestionar citas médicas en un hospital. Permite a los usuarios:

* **Reservar citas:** Verificando la disponibilidad del médico y confirmando la cita.
* **Cancelar citas:** Con diferentes motivos de cancelación.
* **Buscar citas:** Por paciente, médico o fecha.
* **Gestionar médicos:** Agregar, buscar y ver horarios.

## Estructura del Proyecto
* **hospital.py:** Define el hospital (singleton).
* **medico.py:** Gestiona información de los médicos y sus horarios.
* **cita.py:** Maneja la creación y gestión de citas.
* **persona.py:** Representa a los pacientes.
* **handler.py:** Implementa el patrón Chain of Responsibility para la reserva de citas.
* **notificar.py:** Gestiona las notificaciones (WhatsApp, correo, SMS).
* **main.py:** Punto de entrada del programa.

## Instalación
```bash
pip install -r requirements.txt
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

