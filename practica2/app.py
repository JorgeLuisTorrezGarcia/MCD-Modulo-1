class Vehicle:
    def __init__(self, brand, price_per_day):
        self.brand = brand
        self.price_per_day = price_per_day

    def calculate_rental(self, days):
        return self.price_per_day * days

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Price per day: ${self.price_per_day}")


class Car(Vehicle):
    def __init__(self, brand, price_per_day, num_doors):
        super().__init__(brand, price_per_day)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, price_per_day, bike_type):
        super().__init__(brand, price_per_day)
        self.bike_type = bike_type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.bike_type}")


def main():
    print("Sistema de renta de vehículos")
    print("1. Renta de Carro")
    print("2. Renta de Bicicleta")

    option = int(input("Seleccione una opción: "))
    days = int(input("Ingrese el número de días de renta: "))

    if option == 1:
        brand = "Toyota"
        price_per_day = 50.0
        num_doors = 4

        car = Car(brand, price_per_day, num_doors)
        car.display_info()
        print(f"Total a pagar: ${car.calculate_rental(days)}")
    elif option == 2:
        brand = "Giant"
        price_per_day = 15.0
        bike_type = "Mountain"

        bike = Bike(brand, price_per_day, bike_type)
        bike.display_info()
        print(f"Total a pagar: ${bike.calculate_rental(days)}")
        
main()
