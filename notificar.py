import notify2

APP = "Descargas2020"

notify2.init(APP)

def notificar(msg):
    n = notify2.Notification(msg,msg)
    n.show()

