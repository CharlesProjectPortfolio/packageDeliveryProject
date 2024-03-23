# Charles Chrietzberg 011042509

import datetime
import math
import csv

from hashTable import ChainingHashTable
from PackageClass import Package
from Truck1 import delivery
from UserInterface import interface

# Function to get the package data from the csv file and inset them into the hash table
def loadPackageData(fileName):
    with open(fileName) as packageData:
        packages = csv.reader(packageData, delimiter=',')
        next(packages)  # skip header
        for package in packages:
            pID = int(package[0])
            paddress = package[1]
            pcity = package[2]
            pstate = package[3]
            pzipcode = package[4]
            pdeliveryDeadline = package[5]
            pweight = package[6]
            pstatus = "at the hub"

            # movie object
            p = Package(pID, paddress, pcity, pstate, pzipcode, pdeliveryDeadline, pweight, pstatus)
            # print(m)

            # insert it into the hash table
            myHash.insert(pID, p)
# function to get the Data from the DistanceTable.csv and load it into a 2D list
def loadDistanceData(fileName):
    with open(fileName) as distanceData:
        distances = csv.reader(distanceData, delimiter=',')
        #next(distances)  # skip header
        counter1 = 0
        counter2 = 0
        for distance in distances:  # O(n^2)
            address.append(distance[0])
            for sideways in range(0, 28, 1):
                if distance[sideways].replace(".", "", 1).isdigit():
                    distancesList[counter1][counter2] = float(distance[sideways])
                    counter2 = counter2 + 1
            counter2 = 0
            counter1 = counter1 + 1

myHash = ChainingHashTable() # Create a new instance of the hash table class

loadPackageData('PackageData.csv') # Call loadPackageData

# Create list to hold ordered addresses
address = list()
# Create table to hold ordered distances for addresses
rows, cols = (27, 27)
distancesList = [[-1.0 for i in range(cols)] for j in range(rows)]

loadDistanceData('DistanceTable.csv') # Call loadDistanceData

count = 0
count2 = 0
# loop to fill in the rest of the ordered addresses table Time complexity - O(n^3), space Complexity O(n)
for row in distancesList:
    for col in row:
        count = count + 1
        if col == 0.0:
            for i in range(count, len(row), 1):
                distancesList[count2][i] = distancesList[i][count2]
    count2 = count2 + 1
    count = 0

counting = 0
# loop to remove the zipcodes from the addresses
for i in address:  #O(n)
    position = i.find("(")
    if position != -1:
        address[counting] = i[1:position-1]
    counting = counting + 1

truck1 = list() # Create list to hold packages for truck 1
truck1.append(myHash.search(1))
truck1.append(myHash.search(13))
truck1.append(myHash.search(14))
truck1.append(myHash.search(15))
truck1.append(myHash.search(16))
truck1.append(myHash.search(19))
truck1.append(myHash.search(20))
truck1.append(myHash.search(29))
truck1.append(myHash.search(30))
truck1.append(myHash.search(31))
truck1.append(myHash.search(34))
truck1.append(myHash.search(37))
truck1.append(myHash.search(40))
truck1.append(myHash.search(2))
truck1.append(myHash.search(4))
truck1.append(myHash.search(5))

truck2 = list() # Create list to hold packages for truck 2
truck2.append(myHash.search(3))
truck2.append(myHash.search(18))
truck2.append(myHash.search(36))
truck2.append(myHash.search(38))
truck2.append(myHash.search(7))
truck2.append(myHash.search(8))
truck2.append(myHash.search(10))
truck2.append(myHash.search(11))
truck2.append(myHash.search(12))
truck2.append(myHash.search(17))
truck2.append(myHash.search(21))
truck2.append(myHash.search(22))
truck2.append(myHash.search(23))
truck2.append(myHash.search(24))
truck2.append(myHash.search(26))
truck2.append(myHash.search(27))

startTime = datetime.time(8,0, 0) # Start the clock at 8 AM
currentDay = datetime.date.today()
starting = datetime.datetime.combine(currentDay, startTime) # Create datetime object with start time of 8 AM
currentTimeTruck1 = starting # Create currentTime for truck1
currentTimeTruck2 = starting # create current time for truck2
truckSpeed = 18 / 60 # Calculate truck speed
totalMiles = 0 # Keep track of total miles traveled
countInd = 0
# loop to assign the packages loaded for delivery with "en route" and a start time
for i in truck1:  # O(n)
        status = "en route " + str(startTime)
        package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
        myHash.insert(i.ID, package)
# loop to assign the packages loaded for delivery with "en route" and a start time
for i in truck2:  # O(n)
        status = "en route " + str(startTime)
        package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
        myHash.insert(i.ID, package)

for j in range(len(address)):  # O(n)
        if address[j] == "5383 S 900 East #104":
            address[j] = "5383 South 900 East #104"
# Call truck delivery function
result = delivery(address, truck1, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash)
# Calculate the time and distance to travel back to the hub
totalMiles = result[0] + result[2]
minutes = math.floor(result[2] / truckSpeed)
seconds = round(((result[2] / truckSpeed) - (math.floor((result[2] / truckSpeed)))) * 60)
currentTimeTruck1 = result[1] + datetime.timedelta(minutes=minutes, seconds=seconds)
finishedTruck1 = currentTimeTruck1

result2 = delivery(address, truck2, distancesList, truckSpeed, currentTimeTruck2, totalMiles, myHash)
totalMiles = result2[0]

truck3 = list() # Create list for packages on truck 3
truck3.append(myHash.search(6))
truck3.append(myHash.search(9))
truck3.append(myHash.search(25))
truck3.append(myHash.search(28))
truck3.append(myHash.search(32))
truck3.append(myHash.search(33))
truck3.append(myHash.search(35))
truck3.append(myHash.search(39))

for i in truck3:  # O(n)
    if i.ID == 9:
        pack = Package(i.ID, '410 S State St', i.city, i.state, '84111', i.deliveryDeadline, i.weight, i.status)
        myHash.insert(i.ID, pack)
        i.address = '410 S State St'

for i in truck3:  # O(n)
    status = "en route " + str(currentTimeTruck1)
    pack = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
    myHash.insert(i.ID, pack)

checkTruck3 = list()
for i in truck3:  # O(n)
    checkTruck3.append(i)

correctAddressTime = datetime.time(10, 20, 0)  # Time for correct address
combinedCorrectAddressTime = datetime.datetime.combine(currentDay, correctAddressTime)  # datetime object for correct address
# Call truck delivery function
result3 = delivery(address, truck3, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash)
totalMiles = result3[0]

interface(totalMiles, myHash, finishedTruck1, combinedCorrectAddressTime, checkTruck3)
