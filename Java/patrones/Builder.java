package Java.patrones;

import java.util.ArrayList;
import java.util.List;

class Vacation {
    private String transport;
    private String accommodation;
    private List<String> activities;

    public Vacation() {
        this.transport = null;
        this.accommodation = null;
        this.activities = new ArrayList<>();
    }

    public void setTransport(String transport) {
        this.transport = transport;
    }

    public void setAccommodation(String accommodation) {
        this.accommodation = accommodation;
    }

    public void addActivity(String activity) {
        activities.add(activity);
    }

    @Override
    public String toString() {
        String vacationDetails = " ::::::----------------------------------:::::: Detalles del viaje :::::: -------------------------::::::";
        vacationDetails += "\nTransporte: " + this.transport;
        vacationDetails += "\nAlojamiento: " + this.accommodation;
        vacationDetails += "\nActividades: " + String.join(", ", activities);
        return vacationDetails;
    }
}

class Transport {
    private String transportType;
    private int cost;

    public Transport(String transportType, int cost) {
        this.transportType = transportType;
        this.cost = cost;
    }

    @Override
    public String toString() {
        return this.transportType + " (Costo: " + this.cost + ")";
    }
}

class Accommodation {
    private String accommodationType;
    private int cost;

    public Accommodation(String accommodationType, int cost) {
        this.accommodationType = accommodationType;
        this.cost = cost;
    }

    @Override
    public String toString() {
        return this.accommodationType + " (Costo: " + this.cost + ")";
    }
}

abstract class VacationBuilder {
    protected Vacation vacation;

    public VacationBuilder() {
        this.vacation = new Vacation();
    }

    public abstract void addTransport();

    public abstract void addAccommodation();

    public abstract void addActivities();

    public void reset() {
        this.vacation = new Vacation();
    }

    public Vacation getVacation() {
        return this.vacation;
    }
}

class BeachVacationBuilder extends VacationBuilder {
    @Override
    public void addTransport() {
        this.vacation.setTransport(new Transport("Vuelo", 500).toString());
    }

    @Override
    public void addAccommodation() {
        this.vacation.setAccommodation(new Accommodation("Resort en la playa", 300).toString());
    }

    @Override
    public void addActivities() {
        this.vacation.addActivity("Esnórquel");
        this.vacation.addActivity("Tomar el sol");
        this.vacation.addActivity("Vóley playa");
    }
}

class MountainVacationBuilder extends VacationBuilder {
    @Override
    public void addTransport() {
        this.vacation.setTransport(new Transport("Tren", 150).toString());
    }

    @Override
    public void addAccommodation() {
        this.vacation.setAccommodation(new Accommodation("Cabaña en la montaña", 250).toString());
    }

    @Override
    public void addActivities() {
        this.vacation.addActivity("Senderismo");
        this.vacation.addActivity("Esquí");
        this.vacation.addActivity("Ciclismo de montaña");
    }
}

class VacationDirector {
    private VacationBuilder builder;

    public VacationDirector(VacationBuilder builder) {
        this.builder = builder;
    }

    public void constructBeachVacation() {
        builder.reset();
        builder.addTransport();
        builder.addAccommodation();
        builder.addActivities();
    }

    public void constructMountainVacation() {
        builder.reset();
        builder.addTransport();
        builder.addAccommodation();
        builder.addActivities();
    }
}

public class Builder {
    public static void main(String[] args) {
        // Crear vacaciones de playa
        VacationBuilder beachVacationBuilder = new BeachVacationBuilder();
        VacationDirector vacationDirector = new VacationDirector(beachVacationBuilder);
        vacationDirector.constructBeachVacation();
        System.out.println(beachVacationBuilder.getVacation());

        // Crear vacaciones de montaña
        VacationBuilder mountainVacationBuilder = new MountainVacationBuilder();
        vacationDirector = new VacationDirector(mountainVacationBuilder);
        vacationDirector.constructMountainVacation();
        System.out.println(mountainVacationBuilder.getVacation());
    }
}
