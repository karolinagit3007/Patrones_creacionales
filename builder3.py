class Vacation:
    def __init__(self):
        self.transport = None
        self.accommodation = None
        self.activities = []

    def set_transport(self, transport):
        self.transport = transport

    def set_accommodation(self, accommodation):
        self.accommodation = accommodation

    def add_activity(self, activity):
        self.activities.append(activity)

    def __str__(self):
        vacation_details = " ::::::----------------------------------:::::: Detalles del viaje :::::: -------------------------::::::"
        vacation_details += f"\nTransporte: {self.transport}"
        vacation_details += f"\nAlojamiento: {self.accommodation}"
        vacation_details += "\nActividades: " + ", ".join(self.activities)
        return vacation_details

class Transport:
    def __init__(self, transport_type, cost):
        self.transport_type = transport_type
        self.cost = cost

    def __str__(self):
        return f"{self.transport_type} (Costo: {self.cost})"

class Accommodation:
    def __init__(self, accommodation_type, cost):
        self.accommodation_type = accommodation_type
        self.cost = cost

    def __str__(self):
        return f"{self.accommodation_type} (Costo: {self.cost})"

class VacationBuilder:
    def __init__(self):
        self.vacation = Vacation()

    def add_transport(self):
        pass

    def add_accommodation(self):
        pass

    def add_activities(self):
        pass

    def reset(self):
        self.vacation = Vacation()

    def get_vacation(self):
        return self.vacation

class BeachVacationBuilder(VacationBuilder):
    def add_transport(self):
        self.vacation.set_transport(Transport("Vuelo", 500))

    def add_accommodation(self):
        self.vacation.set_accommodation(Accommodation("Resort en la playa", 300))

    def add_activities(self):
        self.vacation.add_activity("Esnórquel")
        self.vacation.add_activity("Tomar el sol")
        self.vacation.add_activity("Vóley playa")

class MountainVacationBuilder(VacationBuilder):
    def add_transport(self):
        self.vacation.set_transport(Transport("Tren", 150))

    def add_accommodation(self):
        self.vacation.set_accommodation(Accommodation("Cabaña en la montaña", 250))

    def add_activities(self):
        self.vacation.add_activity("Senderismo")
        self.vacation.add_activity("Esquí")
        self.vacation.add_activity("Ciclismo de montaña")

class VacationDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_beach_vacation(self):
        self.builder.reset()
        self.builder.add_transport()
        self.builder.add_accommodation()
        self.builder.add_activities()

    def construct_mountain_vacation(self):
        self.builder.reset()
        self.builder.add_transport()
        self.builder.add_accommodation()
        self.builder.add_activities()

beach_vacation_builder = BeachVacationBuilder()
vacation_director = VacationDirector(beach_vacation_builder)
vacation_director.construct_beach_vacation()
print(beach_vacation_builder.get_vacation())

mountain_vacation_builder = MountainVacationBuilder()
vacation_director = VacationDirector(mountain_vacation_builder)
vacation_director.construct_mountain_vacation()
print(mountain_vacation_builder.get_vacation())
