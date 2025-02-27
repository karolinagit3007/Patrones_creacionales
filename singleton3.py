import datetime

class EventLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EventLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_logs'):
            self._logs = []  

    def log_event(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        if log_entry not in self._logs:  
            self._logs.append(log_entry)  

    def show_logs(self):
        return "\n".join(self._logs)  

logger1 = EventLogger()
logger2 = EventLogger()

logger1.log_event("El sistema ha iniciado.")
logger2.log_event("Usuario inició sesión.")
logger1.log_event("Archivo guardado correctamente.")

print(logger1.show_logs())

print(logger1 is logger2)  