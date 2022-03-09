"""
Main file for launching the Delivery program.
Will take user input as necessary to run program, fix packages, or specify a specific time.
"""

# Import necessary functions/standard library.
from DeliveryImplementation import *
import time

# Function that provides a CLI for the user to interact with.
# O(n)
def Delivery_UI():

    # Introduction
    print("Welcome to the Delivery System! \n")

    # Starting options
    while True:
        try:
            menu = int(input("What would you like to do? \n"
                             "(1) Run Full Delivery Program \n"
                             "(2) Request Delivery Details at a Specific Time  \n"
                             "(0) Exit \n"))

            # 0 - Exits program
            if menu == 0:
                print("You entered 0, Exiting Program. \n")
                time.sleep(1)
                return False

            # 1 - Launches Full Delivery Program
            elif menu == 1:
                print("Running Full Delivery Program! \n")
                print("Loading Trucks... \n")
                time.sleep(2)
                Delivery_Loading() #Runs function to load packages
                Delivery_Loading_Confirmed() #Displays Loading confirmation
                print("\nTrucks are loaded.  Starting Deliveries... \n")
                time.sleep(1)

                # Fixing Package #9 error
                while True:

                    try:
                        # Package 9 Options
                        updateWarning = int(input("WARNING!  Package ID #9 has incorrect address. \n"
                                              "(1) Fix Package Error \n"
                                              "(0) Exit Program \n"))

                        # 0 - Exits Program
                        if updateWarning == 0:
                            print("You entered 0, Exiting Program. \n")
                            time.sleep(1)
                            return False

                        # 1 - Fixes Package Address
                        if updateWarning == 1:
                            print("Fixing Package Address \n"
                                  "Updating Address to: 410 S State St \n")
                            time.sleep(2)
                            # O(n)
                            for parcel in Truck3.packages:
                                if parcel[7].startswith("Wrong"):
                                    Truck3.removePackage(parcel)
                            updatedAddress = ['9', '410 S State St', 'Salt Lake City', 'UT', '84103', 'EOD', '2',
                                              'Wrong address listed',
                                              'ON TRUCK FOR DELIVERY']
                            Truck3.addPackage(updatedAddress)
                            Truck3.path = Neighbor_Implementation(Truck3.path)
                            print("Address has been updated.  Optimal Path Rerouted.")
                            print("Continuing Deliveries... \n")
                            time.sleep(2)
                            Delivery() # Delivers all packages
                            time.sleep(1)
                            print(" \nAll items successfully delivered!\n")
                            travelTotal() # Calculates and displays all distances
                            print("All Deliveries Completed at:", Truck3.timeEnd.time())
                            time.sleep(2)
                            return False
                        else:
                            print("Incorrect Value Entered.  Please Try Again. \n")
                    except ValueError:
                        print("Incorrect Value Entered.  Please Try Again. \n")
                        continue
                return False

            # 2 - Launches Progam for statuses at a specific time
            elif menu == 2:
                print("Please specify a time to see package status.")
                Delivery_Loading()
                while True:
                    try:
                        # User Input for Hour
                        hour = int(input("Please enter the hour in 24H format: \n"))

                        # Gives prompts depending on range and continues
                        if hour in range(0, 7):
                            print("This time is before work starts.  All items will be at the HUB.")
                            break
                        elif hour in range(17, 24):
                            print("This time is after work hours.  All items will be DELIVERED.")
                            break
                        elif hour in range(7,18):
                            print("Hour: " + str(hour) + "\n")
                            time.sleep(.25)
                            break
                        else:
                            print("Incorrect Value Entered.  Please Try Again. \n")
                    except ValueError:
                        print("Incorrect Value Entered.  Please Try Again. \n")
                        continue

                while True:
                    try:
                        # User Input for Minute
                        minute = int(input("Please enter minute: \n"))

                        # Limits range
                        if minute in range(0, 60):
                            print("Minute: " + str(minute) + "\n")

                            # Different formats for time displaying to user
                            if hour < 10:
                                if minute < 10:
                                    print("Package Statuses at: 0" + str(hour) + ":0" + str(minute) + ":00")
                                else:
                                    print("Package Statuses at: 0" + str(hour) + ":" + str(minute) + ":00")
                            else:
                                if minute < 10:
                                    print("Package Statuses at: " + str(hour) + ":0" + str(minute) + ":00")
                                else:
                                    print("Package Statuses at: " + str(hour) + ":" + str(minute) + ":00")

                            # Additional branching depending on time input to solve package #9 address issue
                            if hour > 9:
                                if hour == 10:
                                    if minute < 20:
                                        time.sleep(2)
                                        packageStatus(hour, minute, 0) # Runs program with above parameters to get appropriate package status
                                        return False
                                    else:
                                        # Fixes Package #9 for the 10th hour if after 10:19am.
                                        print("Time is after 10:20am.  Package #9 address updated.")
                                        # O(n)
                                        for parcel in Truck3.packages:
                                            if parcel[7].startswith("Wrong"):
                                                Truck3.removePackage(parcel)
                                        updatedAddress = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD',
                                                          '2',
                                                          'Wrong address listed',
                                                          'ON TRUCK FOR DELIVERY']
                                        Truck3.addPackage(updatedAddress)
                                        Truck3.path = Neighbor_Implementation(Truck3.path)
                                        time.sleep(2)
                                        packageStatus(hour, minute, 0)  # Runs program with above parameters to get appropriate package status
                                        return False
                                else:
                                    # Fixes Package #9 for every other time after 10:59am.
                                    print("Time is after 10:20am.  Package #9 address updated.")
                                    # O(n)
                                    for parcel in Truck3.packages:
                                        if parcel[7].startswith("Wrong"):
                                            Truck3.removePackage(parcel)
                                    updatedAddress = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD',
                                                      '2',
                                                      'Wrong address listed',
                                                      'ON TRUCK FOR DELIVERY']
                                    Truck3.addPackage(updatedAddress)
                                    Truck3.path = Neighbor_Implementation(Truck3.path)
                                    time.sleep(2)
                                    packageStatus(hour, minute, 0) # Runs program with above parameters to get appropriate package status
                                    return False
                            else:
                                time.sleep(2)
                                packageStatus(hour, minute, 0) # Runs program with above parameters to get appropriate package status
                                return False
                        else:
                            print("Incorrect Value Entered.  Please Try Again. \n")
                    except ValueError:
                        print("Incorrect Value Entered.  Please Try Again. \n")
                        continue
            else:
                print("Incorrect Value Entered.  Please Try Again. \n")
        except ValueError:
            print ("Incorrect Value Entered.  Please Try Again. \n")
            continue
    SystemExit()



# Starts the UI, which starts program.
Delivery_UI()