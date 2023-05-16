# Define the Vehicle class, which has make and model attributes
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Define the Car class, which is a subclass of Vehicle and adds a doors attribute
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

# Define the Truck class, which is a subclass of Vehicles and adds a bed_length attribute
class Truck(Vehicle):
    def __init__(self, make, model, bed_length):
        super().__init__(make, model)
        self.bed_length = bed_length

# Define the Garage class, which contains a list of vehicles
class Garage:
    def __init__(self):
        self.vehicles = []

    # Define the add_vehicle method, which adds a vehicle to the list and prints a message
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.make} {vehicle.model} added to the garage.")

    # Define the print_vehicles method, which prints a list of the vehicles in the garage
    def print_vehicles(self):
        print("Vehicles in the garage:")
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f"{vehicle.make} {vehicle.model}, {vehicle.doors} doors")
            elif isinstance(vehicle, Truck):
                print(f"{vehicle.make} {vehicle.model}, bed length: {vehicle.bed_length}")

# Print welcome message
print("Welcome to Bellevue University Virtual Garage\n")

# Create new Garage object
garage = Garage()

# Start loop to ask user to add vehicles to the garage
while True:
    # Ask the user if they want to add a car or truck, or quit the program
    vehicle_type = input("\nAdd a car or truck? (type 'car' or 'truck', or 'q' to quit): ")
    if vehicle_type == 'q':
        break
    # Ask the user for the make and model of the vehicle
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    # If the user chose a car, ask for the number of doors and create a Car object
    if vehicle_type == 'car':
        doors = int(input("Enter the number of doors: "))
        vehicle = Car(make, model, doors)
    # If the user chose a truck, ask for the bed length and create a Truck object
    elif vehicle_type == 'truck':
        bed_length = input("Enter the bed length: ")
        vehicle = Truck(make, model, bed_length)
    # Add the vehicle to the garage using the add_vehicle method
    garage.add_vehicle(vehicle)

# Print a thank you message when the program is done
print("\nThank you for using the Bellevue University virtual garage!")
