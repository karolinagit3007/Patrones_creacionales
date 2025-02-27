package Java.patrones;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

class EventLogger {
    private static EventLogger instance = null;
    private List<String> logs;

    // Constructor privado para evitar la creación de instancias externas
    private EventLogger() {
        logs = new ArrayList<>();
    }

    // Método para obtener la instancia única de EventLogger (Singleton)
    public static EventLogger getInstance() {
        if (instance == null) {
            instance = new EventLogger();
        }
        return instance;
    }

    // Método para registrar un evento
    public void logEvent(String message) {
        String timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
        String logEntry = "[" + timestamp + "] " + message;

        if (!logs.contains(logEntry)) {  // Verifica si el evento ya fue registrado
            logs.add(logEntry);  // Agrega el evento al log
        }
    }

    // Método para mostrar los logs
    public String showLogs() {
        return String.join("\n", logs);  // Devuelve los logs en el orden en que fueron registrados
    }
}

public class Singleton {
    public static void main(String[] args) {
        // Se crea una única instancia del logger
        EventLogger logger1 = EventLogger.getInstance();
        EventLogger logger2 = EventLogger.getInstance();

        // Se registran eventos desde diferentes instancias
        logger1.logEvent("El sistema ha iniciado.");
        logger2.logEvent("Usuario inició sesión.");
        logger1.logEvent("Archivo guardado correctamente.");

        // Ver logs desde cualquier instancia
        System.out.println(logger1.showLogs());

        // Verificar que solo hay una instancia
        System.out.println(logger1 == logger2);  // true
    }
}
