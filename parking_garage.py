#Juan, Grace, and I's group prject on Parking Garage



# currentTicket{}

# tickets[]
# parkingSpaces[]

# whileTrue loop

# counter

# input

# kicks off timer when user takes ticket

# garage = spaces available 

# add dunder

# import datetime

# current_time = datetime.datetime.now()

# import timeit
# start = timeit.timeit()
# print("hello")
# end = timeit.timeit()
# print(end - start)

from timeit import default_timer as timer

# start = timer()

# print(23*2.3)

# end = timer()
# print(end - start)

class Car():
    def __init__(self, license_plate, make, model, color):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.color = color
        self.car_info = []

    def __repr__(self):
        return f'{self.make}, {self.model}, {self.color}, {self.license_plate}'

        

class Parking_Garage():

    def __init__(self):
        self.tickets = 200
        self.cars_added = []
        self.parking_spaces = 100
        self.parking_spaces_available = parking_spaces_available


    def take_ticket(self):
        while True: 
            if self.parking_spaces > 0:
                response = input(f"Welcome to JGM Garage, please press enter your vehicle's: {self.make}, {self.model}, {self.color}, and {self.license_plate}").lower()
                continue
                response == input("Press 1 to take your ticket")
                if response == input("1"):
                    start = timer()
                    print("Please take your ticket and find an available parking space.")
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    self.car_info = [self.make, self.model, self.color, self.license_plate]
            else:
                print(f"We have {self.parking_spaces} parking spaces available. I'm sorry.")
        
            # timer starts at input 1
            # decrement from available tickets and parking spaces
        else:
            print("Please enter a valid response.")
            
        
        

    def pay_for_parking(self):
        print()
        while True:
            response = input()

    def leave_garage(self):

    def update_tickets(self):

    def update_parking_spaces(self):
        return self.parking_spaces