package Java.patrones;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

class EventLogger {
    private static EventLogger instance = null;
    private List<String> logs;

    private EventLogger() {
        logs = new ArrayList<>();
    }

    public static EventLogger getInstance() {
        if (instance == null) {
            instance = new EventLogger();
        }
        return instance;
    }

    public void logEvent(String message) {
        String timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
        String logEntry = "[" + timestamp + "] " + message;

        if (!logs.contains(logEntry)) {  
            logs.add(logEntry);  
        }
    }

    public String showLogs() {
        return String.join("\n", logs);  
    }
}

public class Singleton {
    public static void main(String[] args) {
        EventLogger logger1 = EventLogger.getInstance();
        EventLogger logger2 = EventLogger.getInstance();

        logger1.logEvent("El sistema ha iniciado.");
        logger2.logEvent("Usuario inició sesión.");
        logger1.logEvent("Archivo guardado correctamente.");

        System.out.println(logger1.showLogs());

        System.out.println(logger1 == logger2); 
    }
}
