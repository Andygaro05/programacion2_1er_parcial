from abc import ABC, abstractmethod
from datetime import datetime

class Notificar(ABC):
    def __init__(self):
        pass

    def enviar_notificacion(self, persona, mensaje):
        tipo_notificacion = input("Ingrese el tipo de notificación (whatsapp(1), correo(2), sms(3)): ")
        if tipo_notificacion == '1':
            self.notificar_whatsapp(persona, mensaje)
        elif tipo_notificacion == '2':
            self.notificar_correo(persona, mensaje)
        elif tipo_notificacion == '3':
            self.notificar_sms(persona, mensaje)
        else:
            print("Tipo de notificación inválido.")

    def notificar_whatsapp(self, persona, mensaje):
        return f"Enviando WhatsApp a {persona.nombre}: {mensaje}"

    def notificar_correo(self, persona, mensaje):
        return f"Enviando correo a {persona.nombre}: {mensaje}"

    def notificar_sms(self, persona, mensaje):
        return f"Enviando SMS a {persona.nombre}: {mensaje}"
