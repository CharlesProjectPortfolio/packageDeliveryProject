# Charles Chrietzberg 011042509

import datetime
import math
import csv

from hashTable import ChainingHashTable
from PackageClass import Package
from Truck1 import delivery
from Truck2 import delivery2
from Truck3 import delivery3

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
milesTraveled = 0 # create variable for miles traveled truck1
milesTraveled2 = 0 # create variable for miles traveled truck2
totalMiles = 0 # Keep track of total miles traveled
addressIndexTruck1 = list() # List of indexes from the address list to be used in the distances table lookup truck1
addressIndexTruck2 = list() # List of indexes from the address list to be used in the distances table lookup truck2
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
'''
# Loop to match the addresses from truck1 and the addresses list and put them into addressIndexTruck1
for i in truck1:  # O(n^2)
    for j in address:
        if i.address == j:
            addressIndexTruck1.append(countInd)
            break
        countInd = countInd + 1
    countInd = 0
'''
for j in range(len(address)):  # O(n)
        if address[j] == "5383 S 900 East #104":
            address[j] = "5383 South 900 East #104"
'''
countInd = 0
for i in truck2:  # O(n^2)
    for j in address:
        if i.address == j:
            addressIndexTruck2.append(countInd)
            break
        countInd = countInd + 1
    countInd = 0
'''
placeHolder = list()
'''
nextAddressIndex = 0 # Holds to index for the minimum distance in distancesAddressIndexTruck1
nextIndexForDistances = 0 # Holds the value at that index position in addressIndexTruck1
distancesAddressIndexTruck1 = list() # List to determine which address on the truck is the next closest address

nextAddressIndex2 = 0 # Holds to index for the minimum distance in distancesAddressIndexTruck2
nextIndexForDistances2 = 0 # Holds the value at that index position in addressIndexTruck2
distancesAddressIndexTruck2 = list() # List to determine which address on the truck (2) is the next closest address
# Start at hub and deliver package 15 first to meet 9 AM deadline for truck1
backToHub = 0
moving = 0
'''

result = delivery(address, truck1, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash)
check1 = result[0]
check2 = result[1]
print(check1, "   ", check2)
totalMiles = result[0]
currentTimeTruck1 = result[1]
result2 = delivery2(address, truck2, distancesList, truckSpeed, currentTimeTruck2, totalMiles, myHash)
check3 = result2[0]
check4 = result2[1]
print(check3, "   ", check4)
totalMiles = result2[0]
'''
# while loop is O(n^3)
while addressIndexTruck1:# While loop to iterate through truck 1 and deliver the packages to the next closest address
    if moving == 0: # If first iteration of the while loop get the closest address to the HUB
        for i in addressIndexTruck1: # Loop through a list of index positions from address
            for j in range(len(distancesList[moving])): # Use the index to get the row in distancesList
                # Since addressList and DistancesList are both ordered the index from addressList
                # will match up to the distance in that row of distancesList
                if j == i: # Check if j and i math index values
                    # If they match put the distance into distancesAddressIndexTruck1
                    distancesAddressIndexTruck1.append(distancesList[moving][j])
                    break
        for i in truck1:
            if i.ID != 15:
                continue
            for j in range(len(addressIndexTruck1)):
                if i.address == address[addressIndexTruck1[j]]:
                    placeHolder.append(j)

        # force the delivery of package number 15 to meet the 9 AM deadline
        milesTraveled = distancesAddressIndexTruck1[placeHolder[0]] # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled # variable for total miles traveled
        nextAddressIndex = distancesAddressIndexTruck1.index(milesTraveled) # get index of minimum
        nextIndexForDistances = addressIndexTruck1[nextAddressIndex] # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(milesTraveled/truckSpeed)
        seconds = round(((milesTraveled/truckSpeed) - (math.floor((milesTraveled/truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        placeHolderValue = addressIndexTruck1[placeHolder[0]]
        while milesTraveled in distancesAddressIndexTruck1: # remove values for already delivered packages from truck1
            for i in truck1:
                if i.address == address[placeHolderValue]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck1.remove(i)
                    break
            distancesAddressIndexTruck1.remove(milesTraveled)
            addressIndexTruck1.remove(nextIndexForDistances)

        distancesAddressIndexTruck1.clear()
        placeHolder.clear()

    else:
        for i in addressIndexTruck1:
            for j in range(len(distancesList[nextIndexForDistances])):
                if j == i:
                    distancesAddressIndexTruck1.append(distancesList[nextIndexForDistances][j])
                    break

        milesTraveled = min(distancesAddressIndexTruck1) # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled # Variable for total miles traveled
        nextAddressIndex = distancesAddressIndexTruck1.index(min(distancesAddressIndexTruck1)) # get index of minimum
        nextIndexForDistances = addressIndexTruck1[nextAddressIndex] # Use that index to get the value for the next distance list

        if len(addressIndexTruck1) == 1:
            backToHub = nextIndexForDistances

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(min(distancesAddressIndexTruck1)/truckSpeed)
        seconds = round(((min(distancesAddressIndexTruck1)/truckSpeed) - (math.floor((min(distancesAddressIndexTruck1)/truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        holder = addressIndexTruck1[nextAddressIndex]
        while nextIndexForDistances in addressIndexTruck1: # remove values for already delivered packages
            for i in truck1:
                if i.address == address[nextIndexForDistances]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck1.remove(i)
                    break
            addressIndexTruck1.remove(nextIndexForDistances)
        distancesAddressIndexTruck1.clear()
    moving = moving + 1

# Use while loop to find next closest address and update and remove package delivered from truck1
distBackToHub = distancesList[0][backToHub] # Get the distance from the last address back to the hub
totalMiles = totalMiles + distBackToHub # Add the distance to totalMiles
# Calculate the time to travel that distance and add it to the current time
minutes = math.floor(distBackToHub / truckSpeed)
seconds = round(((distBackToHub / truckSpeed) - (
    math.floor((distBackToHub / truckSpeed)))) * 60)
currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)
'''
finishedTruck1 = currentTimeTruck1
'''
moving = 0
# While loop for truck2 O(n^3)
while addressIndexTruck2:  # While loop to iterate through truck 2 and deliver the packages to the next closest address
    if moving == 0:  # If first iteration of the while loop get the closest address to the HUB
        # Truck2 for loop
        for i in addressIndexTruck2:  # Loop through a list of index positions from address
            for j in range(len(distancesList[moving])):  # Use the index to get the row in distancesList
                # Since addressList and DistancesList are both ordered the index from addressList
                # will match up to the distance in that row of distancesList
                if j == i:  # Check if j and i math index values
                    # If they match put the distance into distancesAddressIndexTruck2
                    distancesAddressIndexTruck2.append(distancesList[moving][j])
                    break

        # Truck2 set variables
        milesTraveled2 = min(
            distancesAddressIndexTruck2)  # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled2  # variable for total miles traveled
        nextAddressIndex2 = distancesAddressIndexTruck2.index(milesTraveled2)  # get index of minimum
        nextIndexForDistances2 = addressIndexTruck2[
            nextAddressIndex2]  # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck2 to get to next address
        minutes = math.floor(milesTraveled2 / truckSpeed)
        seconds = round(((milesTraveled2 / truckSpeed) - (math.floor((milesTraveled2 / truckSpeed)))) * 60)
        currentTimeTruck2 = currentTimeTruck2 + datetime.timedelta(minutes=minutes, seconds=seconds)

        while nextIndexForDistances2 in addressIndexTruck2:  # remove values for already delivered packages from truck2
            for i in truck2:
                if i.address == address[nextIndexForDistances2]:
                    status = "Delivered " + str(currentTimeTruck2)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck2.remove(i)
                    break
            addressIndexTruck2.remove(nextIndexForDistances2)

        distancesAddressIndexTruck2.clear()

    else:
        for i in addressIndexTruck2:
            for j in range(len(distancesList[nextIndexForDistances2])):
                if j == i:
                    distancesAddressIndexTruck2.append(distancesList[nextIndexForDistances2][j])
                    break

        # set variables for truck2
        milesTraveled2 = min(
            distancesAddressIndexTruck2)  # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled2  # Variable for total miles traveled
        nextAddressIndex2 = distancesAddressIndexTruck2.index(min(distancesAddressIndexTruck2))  # get index of minimum
        nextIndexForDistances2 = addressIndexTruck2[
            nextAddressIndex2]  # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck2 to get to next address
        minutes = math.floor(min(distancesAddressIndexTruck2) / truckSpeed)
        seconds = round(((min(distancesAddressIndexTruck2) / truckSpeed) - (
            math.floor((min(distancesAddressIndexTruck2) / truckSpeed)))) * 60)
        currentTimeTruck2 = currentTimeTruck2 + datetime.timedelta(minutes=minutes, seconds=seconds)

        while nextIndexForDistances2 in addressIndexTruck2:  # remove values for already delivered packages from truck2
            for i in truck2:
                if i.address == address[nextIndexForDistances2]:
                    status = "Delivered " + str(currentTimeTruck2)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck2.remove(i)
                    break
            addressIndexTruck2.remove(nextIndexForDistances2)
        distancesAddressIndexTruck2.clear()
    moving = moving + 1
'''
truck3 = list() # Create list for packages on truck 3
truck3.append(myHash.search(6))
truck3.append(myHash.search(9))
truck3.append(myHash.search(25))
truck3.append(myHash.search(28))
truck3.append(myHash.search(32))
truck3.append(myHash.search(33))
truck3.append(myHash.search(35))
truck3.append(myHash.search(39))

addressIndexTruck3 = list()

for i in truck3:  # O(n)
    if i.ID == 9:
        pack = Package(i.ID, '410 S State St', i.city, i.state, '84111', i.deliveryDeadline, i.weight, i.status)
        myHash.insert(i.ID, pack)

truck3[0] = (myHash.search(6))
truck3[1] = (myHash.search(9))
truck3[2] = (myHash.search(25))
truck3[3] = (myHash.search(28))
truck3[4] = (myHash.search(32))
truck3[5] = (myHash.search(33))
truck3[6] = (myHash.search(35))
truck3[7] = (myHash.search(39))
'''
countInd = 0
for i in truck3:  # O(n^2)
    for j in address:
        if i.address == j:
            addressIndexTruck3.append(countInd)
            break
        countInd = countInd + 1
    countInd = 0
'''
for i in truck3:  # O(n)
    status = "en route " + str(currentTimeTruck1)
    pack = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
    myHash.insert(i.ID, pack)

checkTruck3 = list()
for i in truck3:  # O(n)
    checkTruck3.append(i)
'''
nextAddressIndex3 = 0 # Holds to index for the minimum distance in distancesAddressIndexTruck3
nextIndexForDistances3 = 0 # Holds the value at that index position in addressIndexTruck3
distancesAddressIndexTruck3 = list() # List to determine which address on the truck is the next closest address
milesTraveled3 = 0
'''
correctAddressTime = datetime.time(10, 20, 0)  # Time for correct address
combinedCorrectAddressTime = datetime.datetime.combine(currentDay,
                                                  correctAddressTime)  # datetime object for correct address

result3 = delivery3(address, truck3, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash)
check5 = result3[0]
check6 = result3[1]
print(check5, "   ", check6)
totalMiles = result3[0]
'''
moving = 0
# While loop is O(n^3)
while  addressIndexTruck3:# While loop to iterate through truck3 and deliver the packages to the next closest address
    if moving == 0: # If first iteration of the while loop, get the closest address to the HUB
        for i in addressIndexTruck3: # Loop through a list of index positions from address
            for j in range(len(distancesList[moving])): # Use the index to get the row in distancesList
                # Since addressList and DistancesList are both ordered the index from addressList
                # will match up to the distance in that row of distancesList
                if j == i: # Check if j and i math index values
                    # If they match put the distance into distancesAddressIndexTruck3
                    distancesAddressIndexTruck3.append(distancesList[moving][j])
                    break
        for i in truck3: # Start with package 25 to 10:30 delivery deadline
            if i.ID != 25:
                continue
            for j in range(len(addressIndexTruck3)):
                if i.address == address[addressIndexTruck3[j]]:
                    placeHolder.append(j)

        # force the delivery of package number 25 to meet the 10:30 AM deadline
        milesTraveled3 = distancesAddressIndexTruck3[placeHolder[0]] # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled3 # variable for total miles traveled
        nextAddressIndex3 = distancesAddressIndexTruck3.index(milesTraveled3) # get index of minimum
        nextIndexForDistances3 = addressIndexTruck3[nextAddressIndex3] # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck3 to get to next address
        minutes = math.floor(milesTraveled3/truckSpeed)
        seconds = round(((milesTraveled3/truckSpeed) - (math.floor((milesTraveled3/truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        placeHolderValue = addressIndexTruck3[placeHolder[0]]
        while milesTraveled3 in distancesAddressIndexTruck3: # remove values for already delivered packages from truck3
            for i in truck3:
                if i.address == address[placeHolderValue]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck3.remove(i)
                    break
            distancesAddressIndexTruck3.remove(milesTraveled3)
            addressIndexTruck3.remove(nextIndexForDistances3)

        distancesAddressIndexTruck3.clear()
        placeHolder.clear()

    elif moving == 1:
        for i in addressIndexTruck3: # Loop through a list of index positions from address
            for j in range(len(distancesList[nextIndexForDistances3])): # Use the index to get the row in distancesList
                # Since addressList and DistancesList are both ordered the index from addressList
                # will match up to the distance in that row of distancesList
                if j == i: # Check if j and i math index values
                    # If they match put the distance into distancesAddressIndexTruck1
                    distancesAddressIndexTruck3.append(distancesList[nextIndexForDistances3][j])
                    break
        for i in truck3: # force next delivery to address 6 to meet 10:30 AM delivery deadline
            if i.ID != 6:
                continue
            for j in range(len(addressIndexTruck3)):
                if i.address == address[addressIndexTruck3[j]]:
                    placeHolder.append(j)

        # force the delivery of package number 6 to meet the 10:30 AM deadline
        milesTraveled3 = distancesAddressIndexTruck3[placeHolder[0]] # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled3 # variable for total miles traveled
        nextAddressIndex3 = distancesAddressIndexTruck3.index(milesTraveled3) # get index of minimum
        nextIndexForDistances3 = addressIndexTruck3[nextAddressIndex3] # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(milesTraveled3/truckSpeed)
        seconds = round(((milesTraveled3/truckSpeed) - (math.floor((milesTraveled3/truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        placeHolderValue = addressIndexTruck3[placeHolder[0]]
        while milesTraveled3 in distancesAddressIndexTruck3: # remove values for already delivered packages from truck3
            for i in truck3:
                if i.address == address[placeHolderValue]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck3.remove(i)
                    break
            distancesAddressIndexTruck3.remove(milesTraveled3)
            addressIndexTruck3.remove(nextIndexForDistances3)

        distancesAddressIndexTruck3.clear()
        placeHolder.clear()

    else:
        for i in addressIndexTruck3:
            for j in range(len(distancesList[nextIndexForDistances3])):
                if j == i:
                    distancesAddressIndexTruck3.append(distancesList[nextIndexForDistances3][j])
                    break

        milesTraveled3 = min(distancesAddressIndexTruck3) # Add the distance traveled to the next address to milesTraveled
        totalMiles = totalMiles + milesTraveled3 # Variable for total miles traveled
        nextAddressIndex3 = distancesAddressIndexTruck3.index(min(distancesAddressIndexTruck3)) # get index of minimum
        nextIndexForDistances3 = addressIndexTruck3[nextAddressIndex3] # Use that index to get the value for the next distance list

        if len(addressIndexTruck3) == 1:
            backToHub = nextIndexForDistances3

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(min(distancesAddressIndexTruck3)/truckSpeed)
        seconds = round(((min(distancesAddressIndexTruck3)/truckSpeed) - (math.floor((min(distancesAddressIndexTruck3)/truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        holder = addressIndexTruck3[nextAddressIndex3]
        while nextIndexForDistances3 in addressIndexTruck3: # remove values for already delivered packages
            for i in truck3:
                if i.address == address[nextIndexForDistances3]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    truck3.remove(i)
                    break
            addressIndexTruck3.remove(nextIndexForDistances3)
        distancesAddressIndexTruck3.clear()
    moving = moving + 1
'''
# Create Console interface for user
exitProgram = 0
test = 0
while exitProgram == 0:  # O(n^3)
    # Ask if user would like to print all package status and total mileage
    userInput1 = input("Would you like to print all package status and total mileage? (Enter Y or N): ")
    if userInput1 == "Y" or userInput1 == "N":
        test = 1
    while test != 1:
        userInput1 = input("Would you like to print all package status and total mileage? (Enter Y or N): ")
        if userInput1 == "Y" or userInput1 == "N":
            test = 1
    if userInput1 == "Y":
        for i in range(len(myHash.table)):
            print("Package: {}".format(myHash.search(i + 1)))
        print("Total Miles: ", totalMiles)
    test = 0
    # Ask if user would like to get a single package status with a time
    userInput2 = input("Would you like to get a single package status with a time? (Enter Y or N): ")
    if userInput2 == "Y" or userInput2 == "N":
        test = 1
    while test != 1:
        userInput2 = input("Would you like to get a single package status with a time? (Enter Y or N): ")
        if userInput2 == "Y" or userInput2 == "N":
            test = 1
    if userInput2 == "Y":
        packageID = int(input("Enter the package ID (1 - 40): "))
        if packageID < 1 or packageID > 40:
            testing = 0
            while testing != 1:
                packageID = int(input("Enter the package ID (1 - 40): "))
                if 1 <= packageID <= 40:
                    testing = 1
        packageHolder = myHash.search(packageID)
        temp = packageHolder.status
        print(temp)
        statusHolder = datetime.datetime.strptime(temp[10:len(temp)], '%Y-%m-%d %H:%M:%S')
        timeInput = input("Enter the time (HH:MM:SS): ")
        putTogether = str(datetime.date.today()) + " " + timeInput
        convertDateTime = datetime.datetime.strptime(putTogether, '%Y-%m-%d %H:%M:%S')
        check = 0
        for i in checkTruck3:
            if i.ID == packageID:
                check = 1
                break
        if statusHolder > convertDateTime > finishedTruck1 and check == 1:
            packStatus = "en route " + str(convertDateTime)
            if packageID == 9 and convertDateTime < combinedCorrectAddressTime:
                print(packageHolder.ID, ", ",
                      "300 State St, ",
                      packageHolder.city, ", ",
                      "84103, ",
                      packageHolder.weight, ", ",
                      packStatus)
            else:
                print(packageHolder.ID, ", ",
                      packageHolder.address, ", ",
                      packageHolder.city, ", ",
                      packageHolder.zipCode, ", ",
                      packageHolder.weight, ", ",
                      packStatus)
        elif convertDateTime < statusHolder and check == 1:
            packStatus = "at the hub " + str(convertDateTime)
            if packageID == 9 and convertDateTime < combinedCorrectAddressTime:
                print(packageHolder.ID, ", ",
                      "300 State St, ",
                      packageHolder.city, ", ",
                      "84103, ",
                      packageHolder.weight, ", ",
                      packStatus)
            else:
                print(packageHolder.ID, ", ",
                      packageHolder.address, ", ",
                      packageHolder.city, ", ",
                      packageHolder.zipCode, ", ",
                      packageHolder.weight, ", ",
                      packStatus)
        elif convertDateTime < statusHolder:
            packStatus = "en route " + str(convertDateTime)
            print(packageHolder.ID, ", ",
                  packageHolder.address, ", ",
                  packageHolder.city, ", ",
                  packageHolder.zipCode, ", ",
                  packageHolder.weight, ", ",
                  packStatus)
        else:
            print(packageHolder.ID, ", ",
                  packageHolder.address, ", ",
                  packageHolder.city, ", ",
                  packageHolder.zipCode, ", ",
                  packageHolder.weight, ", ",
                  packageHolder.status)
    test = 0
    # Ask if user would like to get all package status with a time
    userInput3 = input("Would you like to get all package status with a time? (Enter Y or N): ")
    if userInput3 == "Y" or userInput3 == "N":
        test = 1
    while test != 1:
        userInput3 = input("Would you like to get all package status with a time? (Enter Y or N): ")
        if userInput3 == "Y" or userInput3 == "N":
            test = 1
    if userInput3 == "Y":
        timeInput = input("Enter the time (HH:MM:SS): ")
        putTogether = str(datetime.date.today()) + " " + timeInput
        convertDateTime = datetime.datetime.strptime(putTogether, '%Y-%m-%d %H:%M:%S')
        for i in range(len(myHash.table)):
            check = 0
            packageHolder = myHash.search(i+1)
            statusHolder = datetime.datetime.strptime(packageHolder.status[10:len(packageHolder.status)], '%Y-%m-%d %H:%M:%S')
            for j in checkTruck3:
                if j.ID == packageHolder.ID:
                    check = 1
                    break
            if statusHolder > convertDateTime > finishedTruck1 and check == 1:
                packStatus = "en route " + str(convertDateTime)
                if packageHolder.ID == 9 and convertDateTime < combinedCorrectAddressTime:
                    print(packageHolder.ID, ", ",
                          "300 State St, ",
                          packageHolder.city, ", ",
                          "84103, ",
                          packageHolder.weight, ", ",
                          packStatus)
                else:
                    print(packageHolder.ID, ", ",
                          packageHolder.address, ", ",
                          packageHolder.city, ", ",
                          packageHolder.zipCode, ", ",
                          packageHolder.weight, ", ",
                          packStatus)
            elif convertDateTime < statusHolder and check == 1:
                packStatus = "at the hub " + str(convertDateTime)
                if packageHolder.ID == 9 and convertDateTime < combinedCorrectAddressTime:
                    print(packageHolder.ID, ", ",
                          "300 State St, ",
                          packageHolder.city, ", ",
                          "84103, ",
                          packageHolder.weight, ", ",
                          packStatus)
                else:
                    print(packageHolder.ID, ", ",
                          packageHolder.address, ", ",
                          packageHolder.city, ", ",
                          packageHolder.zipCode, ", ",
                          packageHolder.weight, ", ",
                          packStatus)
            elif convertDateTime < statusHolder:
                packStatus = "en route " + str(convertDateTime)
                print(packageHolder.ID, ", ",
                      packageHolder.address, ", ",
                      packageHolder.city, ", ",
                      packageHolder.zipCode, ", ",
                      packageHolder.weight, ", ",
                      packStatus)
            else:
                print(packageHolder.ID, ", ",
                      packageHolder.address, ", ",
                      packageHolder.city, ", ",
                      packageHolder.zipCode, ", ",
                      packageHolder.weight, ", ",
                      packageHolder.status)
    test = 0
    # Ask if user would like to exit the program
    userInput4 = input("Exit the program (Enter Y or N): ")
    if userInput4 == "Y" or userInput4 == "N":
        test = 1
    while test != 1:
        userInput4 = input("Exit the program (Enter Y or N): ")
        if userInput4 == "Y" or userInput4 == "N":
            test = 1
    if userInput4 == "Y":
        exitProgram = 1