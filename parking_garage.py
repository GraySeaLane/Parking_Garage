#Juan, Grace, and I's group prject on Parking Garage
#Notes
# tickets[]
# parkingSpaces[]
# whileTrue loop?
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
# return f'{self.license_plate}'

#Parking rates:
#$1 per second, better be quick!

import math
from timeit import default_timer as timer

#first class
class Car:
    def __init__(self, license_plate, entry_time):
        self.license_plate = license_plate
        self.entry_time = entry_time
        # self.car_info = []

#second class
class Parking_Garage:
    def __init__(self):

        self.tickets = 200
        self.parking_spaces = 10
        self.currentTicket = {}

    def take_ticket(self):
        if self.parking_spaces > 0 and self.tickets > 0:
            print("Welcome to JGM Garage!")
            license_plate = input("Please enter your vehicle's license plate: ")
            self.currentTicket[license_plate] = {"paid": False, "entry_time": timer()}
            # self.currentTicket[license_plate] = {"paid": False}

            self.tickets -= 1
            self.parking_spaces -= 1
            print("Please take your ticket and find an available parking space.")
            # self.currentTicket[license_plate] = {[license_plate], ["entry_time"]: timer()}
        else:
            print(f"We have {self.parking_spaces} parking spaces available. I'm sorry.")
            # timer starts at input 1
            # decrement from available tickets and parking spaces
            # else:
            # print("Please enter a valid response.")
    
    def pay_for_parking(self):
        license_plate = input("Please enter your vehicle's license plate: ")
        if license_plate in self.currentTicket and not self.currentTicket[license_plate]["paid"]:
                exit_time = timer()
                entry_time = self.currentTicket[license_plate]["entry_time"]
                elapsed_time = int(exit_time - entry_time)
                payment_due = elapsed_time * 1
                # payment_due = 10

                print(f"Your amount due is: ${payment_due}")
                payment = int(input("Please enter payment: $"))
                if payment != payment_due:
                    print("Payment invalid. Please enter the correct dollar amount")
                elif payment == payment_due:
                    self.currentTicket[license_plate]["paid"] = True
                    print("Your ticket has been paid, you have 15 minutes to exit the garage.")
                else:
                    print("Please make a payment.")
        else:
            print("Invalid license plate number, please try again.")
    
    def leave_garage(self):
        license_plate = input("Please enter your vehicle's license plate: ")
        if license_plate in self.currentTicket:
             if self.currentTicket[license_plate]["paid"] == True:
                print("Thank you have a nice day!")
                self.tickets += 1
                self.parking_spaces += 1
                del self.currentTicket[license_plate]
    
    def run(self):
        while True:
            menu = input('To take a ticket press [t], to pay for parking press [p], to leave the garage press [g] or press [q] to quit: \n').lower()
            if menu == 't':
                self.take_ticket()
            if menu == 'p':
                self.pay_for_parking()
            if menu == 'g':
                self.leave_garage()
            elif menu == 'q':
                break
                

garage = Parking_Garage()
garage.run()
