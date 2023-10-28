#Juan, Grace, and I's group prject on Parking Garage

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

#importing timer
# start = timer()

# print(23*2.3)

# end = timer()
# print(end - start)
# currentTicket{}

# def __repr__(self):
#     return f'{self.license_plate}'

import math
from timeit import default_timer as timer
# from IPython.display import Image, display

currentTicket = {}


#Parking rates: 
#$1 per second, better be quick!


#first class
class Car:
    def __init__(self, license_plate, entry_time):
        self.license_plate = license_plate
        self.car_info = []
        self.paid = False
        self.entry_time = entry_time

        
#second class
class Parking_Garage:

    def __init__(self):
        self.tickets = 200
        self.parking_spaces = 100
        self.cars = {}
    
    def take_ticket(self):
        if self.parking_spaces > 0 and self.tickets > 0:
            print("Welcome to JGM Garage!")
            license_plate = input("Please enter your vehicle's license plate: ")
           #old
            # currentTicket[license_plate] = {"paid": False, "entry_time": timer()}
            #new
            self.cars[license_plate] = Car(license_plate, timer())
           
            self.tickets -= 1
            self.parking_spaces -= 1
            print("Please take your ticket and find an available parking space.")

            # self.currentTicket[license_plate] = [license_plate] #"entry_time":} #timer()
        

        else:
            print(f"We have {self.parking_spaces} parking spaces available. I'm sorry.")

            # timer starts at input 1
            # decrement from available tickets and parking spaces
        # else: 
        # print("Please enter a valid response.")
        
        
    def pay_for_parking(self):
        license_plate = input("To pay please re-enter your vehicle's license plate: ")
        if license_plate in self.cars:
        # if curr_car
            curr_car = self.cars[license_plate]

        # print(curr_car)
        if license_plate in currentTicket and not currentTicket[license_plate]["paid"]:
                exit_time = timer()
                entry_time = currentTicket[license_plate]["entry_time"]
                elapsed_time = int(exit_time - entry_time)
                payment_due = elapsed_time * 1
                print(f"Your amount due is: ${payment_due}")
                payment = int(input("Please enter payment: $"))
                if payment != payment_due:
                    print("Payment invalid. Please enter correct dollar amount")
                    
                elif payment == payment_due:
                    currentTicket[license_plate]["paid"] = True
                    print("Your ticket has been paid, you have 15 minutes to exit the garage.")
                
                else:
                    print("Please make a payment.")
        
        else:
            print("Invalid license plate number, please try again.")
            
    def leave_garage(self):
        license_plate = input("Please enter your vehicle's license plate: ")
        if license_plate in currentTicket: 
             if currentTicket[license_plate]["paid"] == True:
                print("Thank you have a nice day!")
                # display(Images/cute.jpeg)

                self.parking_spaces += 1
                del currentTicket[license_plate]

                  



#         print()
#         while True:
#             response = input()

#     def leave_garage(self):

#     def update_tickets(self):

#     def update_parking_spaces(self):
#         return self.parking_spaces

Car()
garage = Parking_Garage()
garage.run()

# Parking_Garage().take_ticket()
# Parking_Garage().pay_for_parking()
# Parking_Garage().leave_garage()
