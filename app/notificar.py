from abc import ABC, abstractmethod
from datetime import datetime

class Notificar(ABC):
    def __init__(self, siguiente=None):
        self._siguiente = siguiente

    def notificar(self, persona, mensaje):
        if self._siguiente:
            self._siguiente.notificar(persona, mensaje)

class NotificacionWhatsapp(Notificar):
    def notificar(self, persona, mensaje):
        print(f"Enviando WhatsApp a {persona.nombre}: {mensaje}")

class NotificacionCorreo(Notificar):
    def notificar(self, persona, mensaje):
        print(f"Enviando correo a {persona.nombre}: {mensaje}")

class NotificacionSMS(Notificar):
    def notificar(self, persona, mensaje):
        print(f"Enviando SMS a {persona.nombre}: {mensaje}")
