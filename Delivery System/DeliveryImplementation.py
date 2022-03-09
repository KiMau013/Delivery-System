"""
File for implementing the full delivery process.
Handles creating trucks for loading, as well as implementing the process for deliveries.
"""

# Import necessary functions/standard library.
from datetime import datetime, timedelta
from GraphImplementation import graph
from NeighborImplementation import Neighbor_Implementation
from HashImplementation import packagesTable
import time

# Creates a class for the delivery trucks
# O(1)
class Delivery_Truck:

    # Constructor
    # Sets parameters as necessary
    # O(1)
    def __init__(self):
        self.packages = []
        self.path = []
        self.timeStart = None
        self.timeCurrent = None
        self.timeEnd = None
        self.truckSpeed = float(18/60)

    # Function for adding a package to the truck
    # O(1)
    def addPackage(self, package):
        self.packages.append(package)
        self.path.append(package[1])

    # Function for removing a package from the truck
    # O(1)
    def removePackage(self, package):
        self.packages.remove(package)
        self.path.remove(package[1])

    # Function for determining start time
    # O(1)
    def deliveryStart(self, time):
        self.timeStart = time

    # Function for determining the truck end time
    # O(1)
    def deliveryEnd(self, time):
        self.timeEnd = time
        return time

# Creates a different Truck from the Delivery_Truck class for each Truck in use
Truck1 = Delivery_Truck()
Truck2 = Delivery_Truck()
Truck3 = Delivery_Truck()

# Empty variable for a list of all addresses
addresses = []

# Loads the packages table through the graph functions
graph.vertexLoad(packagesTable)

# Function for loading the Delivery Trucks that were created
# O()
def Delivery_Loading():

    # Adds all addresses from graph to addresses list
    # O(n)
    for address in graph.graphDict:
         addresses.append(address)

    # Loads packages onto each of the 3 different trucks
    # O(n^2)
    for address in addresses:
        for package in graph.graphDict[address]:
            if package[0] in (1, 7, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 35, 37, 40):
                Truck1.addPackage(package)
            if package[0] in (2, 3, 6, 8, 11, 12, 17, 18, 25, 28, 32, 33, 36, 38, 39):
                Truck2.addPackage(package)
            if package[0] in (4, 5, 9, 10, 21, 22, 23, 24, 26):
                Truck3.addPackage(package)

    # Saves original path (Unused)
    Truck1Original = Truck1.path
    Truck2Original = Truck2.path
    Truck3Original = Truck3.path

    # Appends the HUB to each unoptomized path in order to account for trucks return back to home base (Unused)
    Truck1Original.append("HUB")
    Truck2Original.append("HUB")
    Truck3Original.append("HUB")

    # Runs the nearest neighbor path algorithm to determine the optimal path for each truck
    Truck1.path = Neighbor_Implementation(Truck1.path)
    Truck2.path = Neighbor_Implementation(Truck2.path)
    Truck3.path = Neighbor_Implementation(Truck3.path)

    # Appends the HUB to each path in order to return trucks back to home base
    Truck1.path.append("HUB")
    Truck2.path.append("HUB")
    Truck3.path.append("HUB")

# Function for displaying that the loading of the trucks was successful.
# O(1)
def Delivery_Loading_Confirmed():
    print(" \nAll trucks loaded up!  Path Charted.")
    print(" \nTruck 1 has", len(Truck1.packages), "Total Packages")
    print("Truck 1 Delivery List: ", *Truck1.packages, sep="\n")
    time.sleep(1)
    print("\nTruck 2 has", len(Truck2.packages), "Total Packages")
    print("Truck 2 Delivery List: ", *Truck2.packages, sep="\n")
    time.sleep(1)
    print("\nTruck 3 has", len(Truck3.packages), "Total Packages")
    print("Truck 3 Delivery List: ", *Truck3.packages, sep="\n")
    time.sleep(1)

# Function for fixing the format of the datetime
# O(1)
def timeFormat(time, seconds):
    actualDate = datetime(100, 1, 1, time.hour, time.minute, time.second)
    actualDate = actualDate + timedelta(seconds = seconds)
    return actualDate.time()

# Function to deliver every package to the correct address
# O(n^2)
def Delivery():

    # Edge Weights for pathing
    pathDistance = graph.edgeWeight

    # Process to deliver all items with Truck 1
    Truck1StartTime = datetime(2021, 8, 1, hour=8, minute=0, second=0)
    Truck1.timeStart = Truck1StartTime
    Truck1.timeCurrent = Truck1StartTime
    # O(n^2)
    for i in range(0, len(Truck1.path) - 1):
        speed = Truck1.truckSpeed
        distance = pathDistance[Truck1.path[i], Truck1.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck1.timeCurrent, seconds)
        Truck1.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
        updateStatus = "DELIVERED AT: " + str(timeDelivered)
        for item in Truck1.packages:
            if Truck1.path[i+1] == item[1]:
                item[8] = updateStatus
    Truck1.timeEnd = Truck1.timeCurrent
    print("\nTruck 1 Deliveries: ", *Truck1.packages, sep="\n")
    time.sleep(1)

    # Process to deliver all items with Truck 2
    Truck2StartTime = datetime(2021, 8, 1, hour=9, minute=5, second=0)
    Truck2.timeStart = Truck2StartTime
    Truck2.timeCurrent = Truck2StartTime
    # O(n^2)
    for i in range(0, len(Truck2.path) - 1):
        speed = Truck2.truckSpeed
        distance = pathDistance[Truck2.path[i], Truck2.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck2.timeCurrent, seconds)
        Truck2.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
        updateStatus = "DELIVERED AT: " + str(timeDelivered)
        for item in Truck2.packages:
            if Truck2.path[i+1] == item[1]:
                item[8] = updateStatus
    Truck2.timeEnd = Truck2.timeCurrent
    print("\nTruck 2 Deliveries: ", *Truck2.packages, sep="\n")
    time.sleep(1)

    # Process to deliver all items with Truck 3
    Truck3StartTime = Truck1.timeEnd
    Truck3.timeStart = Truck3StartTime
    Truck3.timeCurrent = Truck3StartTime
    # O(n^2)
    for i in range(0, len(Truck3.path) - 1):
        speed = Truck3.truckSpeed
        distance = pathDistance[Truck3.path[i], Truck3.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck3.timeCurrent, seconds)
        Truck3.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
        updateStatus = "DELIVERED AT: " + str(timeDelivered)
        for item in Truck3.packages:
            if Truck3.path[i+1] == item[1]:
                item[8] = updateStatus
    Truck3.timeEnd = Truck3.timeCurrent
    print("\nTruck 3 Deliveries: ", *Truck3.packages, sep="\n")
    time.sleep(1)


# Function to deliver every package to the correct address, but only up to a specified time.
# O(n^2)
def packageStatus(hour, minute, second):

    # Edge Weights for pathing
    pathDistance = graph.edgeWeight
    endTime = datetime(2021, 8, 1, hour, minute, second)

    # Process to deliver all items with Truck 1
    Truck1StartTime = datetime(2021, 8, 1, hour=8, minute=0, second=0)
    Truck1.timeStart = Truck1StartTime
    Truck1.timeCurrent = Truck1StartTime
    # O(n)
    if endTime > Truck1StartTime: #Changes status of packages on truck.
        for package in Truck1.packages:
            package[8] = "ON TRUCK FOR DELIVERY"
    # O(n^2)
    for i in range(0, len(Truck1.path) - 1):
        speed = Truck1.truckSpeed
        distance = pathDistance[Truck1.path[i], Truck1.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck1.timeCurrent, seconds)
        if timeDelivered < endTime.time():
            Truck1.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
            updateStatus = "DELIVERED AT: " + str(timeDelivered)
            for item in Truck1.packages:
                if Truck1.path[i+1] == item[1]:
                    item[8] = updateStatus
    Truck1.timeEnd = Truck1.timeCurrent
    print(" \nTruck 1 Status: ", *Truck1.packages, sep="\n")
    time.sleep(1)

    # Process to deliver all items with Truck 2
    Truck2StartTime = datetime(2021, 8, 1, hour=9, minute=5, second=0)
    Truck2.timeStart = Truck2StartTime
    Truck2.timeCurrent = Truck2StartTime
    # O(n)
    if endTime > Truck2StartTime: #Changes status of packages on truck.
        for package in Truck2.packages:
            package[8] = "ON TRUCK FOR DELIVERY"
    # O(n^2)
    for i in range(0, len(Truck2.path) - 1):
        speed = Truck2.truckSpeed
        distance = pathDistance[Truck2.path[i], Truck2.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck2.timeCurrent, seconds)
        if timeDelivered < endTime.time():
            Truck2.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
            updateStatus = "DELIVERED AT: " + str(timeDelivered)
            for item in Truck2.packages:
                if Truck2.path[i+1] == item[1]:
                    item[8] = updateStatus
    Truck2.timeEnd = Truck2.timeCurrent
    print(" \nTruck 2 Status: ", *Truck2.packages, sep="\n")
    time.sleep(1)

    # Process to deliver all items with Truck 3
    # Requires additional criteria to determine the correct start time for Truck 3
    Truck1Complete = 0
    # O(n)
    for item in Truck1.packages:
        if item[8].startswith("DELIVERED"):
            Truck1Complete += 1
    if len(Truck1.packages) == Truck1Complete:
        Truck3StartTime = Truck1.timeEnd
    else:
        Truck3StartTime = datetime(2021, 8, 1, hour=10, minute=0, second=0)
    Truck3.timeStart = Truck3StartTime
    Truck3.timeCurrent = Truck3StartTime
    # O(n^2)
    for i in range(0, len(Truck3.path) - 1):
        speed = Truck3.truckSpeed
        distance = pathDistance[Truck3.path[i], Truck3.path[i+1]]
        minutes = distance/speed
        seconds = round(minutes * 60, 2)
        timeDelivered = timeFormat(Truck3.timeCurrent, seconds)
        if timeDelivered < endTime.time():
            Truck3.timeCurrent = datetime(2021, 8, 1, timeDelivered.hour, timeDelivered.minute, timeDelivered.second)
            updateStatus = "DELIVERED AT: " + str(timeDelivered)
            for item in Truck3.packages:
                if Truck3.path[i+1] == item[1]:
                    item[8] = updateStatus
            for item in Truck3.packages: # Changes status of packages on truck if any are still not delivered.
                if item[8] == "HUB":
                    item[8] = "ON TRUCK FOR DELIVERY"
    Truck3.timeEnd = Truck3.timeCurrent
    print(" \nTruck 3 Status: ", *Truck3.packages, sep="\n")
    time.sleep(1)


# Function for determining the distance travelled
# O(n)
def travelDistance(path):
    edgeWeights = graph.edgeWeight
    total = 0
    for i in range(0, len(path) - 1):
        total = total + edgeWeights[path[i], path[i+1]]
    return total


# Function for running the total travel distance for each truck and outputting it to the user.
# O(1)
def travelTotal():
    Truck1Total = travelDistance(Truck1.path)
    Truck2Total = travelDistance(Truck2.path)
    Truck3Total = travelDistance(Truck3.path)
    allTrucks = Truck1Total + Truck2Total + Truck3Total
    print("Truck 1 Distance: ", round(Truck1Total, 2))
    print("Truck 2 Distance: ", round(Truck2Total, 2))
    print("Truck 3 Distance: ", round(Truck3Total, 2))
    print("Total Distance Travelled: ", round(allTrucks, 2))