'''

NAME > Braden Shrum

FILE NAME > Automobile Creator

DESCRIPTION > This app will allow the user to input the year, make, model, doors (2 or 4), and roof type (sunroof or solid) 
              and the program will make a nice display showing the stats of the car they created.

'''

class Vehicle:
    def __init__(self, type): # Store the type of vehicle
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car") # Set the parent class' type attribute by calling its __init__() function

        #Set the attributes of the car
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def showStats(self):
        '''
        Print the stats of the vehicle in a nice display
        '''
        # Uses a docstring so I can easily format the display
        print(f'''
            Vehicle type: {self.type}
            Year: {self.year}
            Make: {self.make}
            Model: {self.model}
            Number of doors: {self.doors}
            Type of roof: {self.roof}
        ''')

def main():
    #Get input from the user on all the car specifications
    year = input("Enter the year of your car > ")
    make = input("Enter the make of your car > ")
    model = input("Enter the model of your car > ")
    doors = input("Enter the amount of doors your car has (2 or 4) > ")
    roof = input("Enter the roof type that your car has (Solid or sunroof) > ")

    while True: #loop until all exceptions and input problems have been solved

        # test the year variable to make sure it doesn't have any letters or special characters
        try:
            year = int(year)
        except ValueError:
            print("Year must be an integer")
            year = input("Enter the year of your car > ")
            continue

        # test the door variable to make sure it doesn't have any letters or special characters
        try:
            doors = int(doors)
        except ValueError:
            # Tell the user what is wrong and ask for a new input
            print("Doors must be an integer. Either 2 or 4")
            doors = input("Enter the amount of doors your car has (2 or 4) > ")
            continue
        
        if year > 2023: # If the year is over 2023
            # Tell the user what is wrong and ask for a new input
            print("You cannot use cars from the future, sorry")
            year = input("Enter the year of your car > ")
            continue

        if (doors != 2) and (doors != 4): # If the user entered an incorrect amount of doors (anything other than 2 or 4)
            # Tell the user what is wrong and ask for a new input
            doors = input("Enter the amount of doors your car has (2 or 4) > ")
            continue
        if roof.lower() != "solid" and roof.lower() != "sunroof": # if the user input an incorrect roof type (anything other than sunroof or solid)
            # Tell the user what is wrong and ask for a new input
            print("roof must be either solid or sunroof")
            roof = input("Enter the roof type that your car has (Solid or sunroof) > ")
            continue
        break # This statement runs when all exceptions are solved and if statements are passed over

    # Construct the Automobile class from the variables and show the stats in a nice format
    car = Automobile(year, make, model, doors, roof)
    car.showStats()


if __name__ == "__main__":
    main()