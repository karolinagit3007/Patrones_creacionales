import datetime

class EventLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EventLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_logs'):
            self._logs = []  # Se usa una lista para mantener el orden de los eventos

    def log_event(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        if log_entry not in self._logs:  # Verifica si el evento ya fue registrado
            self._logs.append(log_entry)  # Agrega el evento en orden

    def show_logs(self):
        return "\n".join(self._logs)  # Muestra los logs en el orden en que fueron registrados

# Se crea una única instancia del logger
logger1 = EventLogger()
logger2 = EventLogger()

# Se registran eventos desde diferentes instancias
logger1.log_event("El sistema ha iniciado.")
logger2.log_event("Usuario inició sesión.")
logger1.log_event("Archivo guardado correctamente.")

# Ver logs desde cualquier instancia
print(logger1.show_logs())

# Verificar que solo hay una instancia
print(logger1 is logger2)  # True
