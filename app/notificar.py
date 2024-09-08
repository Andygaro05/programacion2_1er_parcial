from abc import ABC, abstractmethod
from datetime import datetime

class Notificar(ABC):
    """
    Clase abstracta que define la interfaz para enviar notificaciones.

    Esta clase proporciona un mecanismo básico para enviar notificaciones por diferentes canales.
    """
    def __init__(self):
        pass

    def enviar_notificacion(self, persona, mensaje):
        """
        Envía una notificación a una persona.

        Args:
            persona: Un objeto que representa a la persona a la que se enviará la notificación.
            mensaje (str): El mensaje de la notificación.
        """
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
        """
        Envía una notificación por WhatsApp.

        Args:
            persona: Un objeto que representa a la persona a la que se enviará la notificación.
            mensaje (str): El mensaje de la notificación.

        Returns:
            str: Un mensaje indicando que la notificación se está enviando.
        """
        return f"Enviando WhatsApp a {persona.nombre}: {mensaje}"

    def notificar_correo(self, persona, mensaje):
        """
        Envía una notificación por correo electrónico.

        Args:
            persona: Un objeto que representa a la persona a la que se enviará la notificación.
            mensaje (str): El mensaje de la notificación.

        Returns:
            str: Un mensaje indicando que la notificación se está enviando.
        """
        return f"Enviando correo a {persona.nombre}: {mensaje}"

    def notificar_sms(self, persona, mensaje):
        """
        Envía una notificación por SMS.

        Args:
            persona: Un objeto que representa a la persona a la que se enviará la notificación.
            mensaje (str): El mensaje de la notificación.

        Returns:
            str: Un mensaje indicando que la notificación se está enviando.
        """
        return f"Enviando SMS a {persona.nombre}: {mensaje}"
