class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def showStats(self):
        print(f'''
            Vehicle type: {self.type}
            Year: {self.year}
            Make: {self.make}
            Model: {self.model}
            Number of doors: {self.doors}
            Type of roof: {self.roof}
        ''')

def main():
    year = input("Enter the year of your car > ")
    make = input("Enter the make of your car > ")
    model = input("Enter the model of your car > ")
    doors = input("Enter the amount of doors your car has (2 or 4) > ")
    roof = input("Enter the roof type that your car has (Solid or sunroof) > ")

    while True:
        try:
            year = int(year)
        except ValueError:
            print("Year must be an integer")
            year = input("Enter the year of your car > ")
            continue

        try:
            doors = int(doors)
        except ValueError:
            print("Doors must be an integer. Either 2 or 4")
            doors = input("Enter the amount of doors your car has (2 or 4) > ")
            continue
        
        if year > 2023:
            print("You cannot use cars from the future, sorry")
            year = input("Enter the year of your car > ")
            continue
        if (doors != 2) and (doors != 4):
            doors = input("Enter the amount of doors your car has (2 or 4) > ")
            continue
        if roof.lower() != "solid" and roof.lower() != "sunroof":
            print("roof must be either solid or sunroof")
            roof = input("Enter the roof type that your car has (Solid or sunroof) > ")
            continue
        break

    car = Automobile(year, make, model, doors, roof)
    car.showStats()


if __name__ == "__main__":
    main()