import math
import datetime
from PackageClass import Package


def delivery(address, truck1, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash):
    nextIndexForDistances = 0  # Holds the value at that index position in addressIndexTruck1
    distancesAddressIndexTruck1 = list()  # List to determine which address on the truck is the next closest address
    placeHolder = list()
    addressIndexTruck1 = list()
    backToHub = 0
    moving = 0

    countInd = 0
    for i in truck1:  # O(n^2)
        for j in address:
            if i.address == j:
                addressIndexTruck1.append(countInd)
                break
            countInd = countInd + 1
        countInd = 0

    # while loop is O(n^3)
    while addressIndexTruck1:  # While loop to iterate through truck 1 and deliver the packages to the next closest address
        if moving == 0:  # If first iteration of the while loop get the closest address to the HUB
            for i in addressIndexTruck1:  # Loop through a list of index positions from address
                for j in range(
                        len(distancesList[moving])):  # Use the index to get the row in distancesList
                    # Since addressList and DistancesList are both ordered the index from addressList
                    # will match up to the distance in that row of distancesList
                    if j == i:  # Check if j and i math index values
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
            milesTraveled = distancesAddressIndexTruck1[placeHolder[0]]  # Add the distance traveled to the next address to milesTraveled
            totalMiles = totalMiles + milesTraveled  # variable for total miles traveled
            nextIndexForDistances = addressIndexTruck1[distancesAddressIndexTruck1.index(milesTraveled)]  # Use that index to get the value for the next distance list

        else:
            for i in addressIndexTruck1:
                for j in range(len(distancesList[nextIndexForDistances])):
                    if j == i:
                        distancesAddressIndexTruck1.append(distancesList[nextIndexForDistances][j])
                        break

            milesTraveled = min(distancesAddressIndexTruck1)  # Add the distance traveled to the next address to milesTraveled
            totalMiles = totalMiles + milesTraveled  # Variable for total miles traveled
            nextIndexForDistances = addressIndexTruck1[distancesAddressIndexTruck1.index(milesTraveled)]  # Use that index to get the value for the next distance list

        if len(addressIndexTruck1) == 1:
            backToHub = nextIndexForDistances

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(min(distancesAddressIndexTruck1) / truckSpeed)
        seconds = round(((min(distancesAddressIndexTruck1) / truckSpeed) - (
            math.floor((min(distancesAddressIndexTruck1) / truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes,
                                                                                 seconds=seconds)
        while nextIndexForDistances in addressIndexTruck1:  # remove values for already delivered packages
            for i in truck1:
                if i.address == address[nextIndexForDistances]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline,
                                      i.weight,
                                      status)
                    myHash.insert(i.ID, package)
                    truck1.remove(i)
                    break
            addressIndexTruck1.remove(nextIndexForDistances)
        distancesAddressIndexTruck1.clear()
        moving = moving + 1

    distBackToHub = distancesList[0][backToHub] # Get the distance from the last address back to the hub
    totalMiles = totalMiles + distBackToHub  # Add the distance to totalMiles
    # Calculate the time to travel that distance and add it to the current time
    minutes = math.floor(distBackToHub / truckSpeed)
    seconds = round(((distBackToHub / truckSpeed) - (
        math.floor((distBackToHub / truckSpeed)))) * 60)
    currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)
    returnValues = list()
    returnValues.append(totalMiles)
    returnValues.append(currentTimeTruck1)
    return returnValues