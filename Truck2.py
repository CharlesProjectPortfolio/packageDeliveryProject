import math
import datetime
from PackageClass import Package

def delivery2(address, truck2, distancesList, truckSpeed, currentTimeTruck2, totalMiles, myHash):
    nextAddressIndex2 = 0  # Holds to index for the minimum distance in distancesAddressIndexTruck2
    nextIndexForDistances2 = 0  # Holds the value at that index position in addressIndexTruck2
    distancesAddressIndexTruck2 = list()  # List to determine which address on the truck (2) is the next closest address
    addressIndexTruck2 = list()
    moving = 0

    countInd = 0
    for i in truck2:  # O(n^2)
        for j in address:
            if i.address == j:
                addressIndexTruck2.append(countInd)
                break
            countInd = countInd + 1
        countInd = 0

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
                        package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight,
                                          status)
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
            nextAddressIndex2 = distancesAddressIndexTruck2.index(
                min(distancesAddressIndexTruck2))  # get index of minimum
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
                        package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight,
                                          status)
                        myHash.insert(i.ID, package)
                        truck2.remove(i)
                        break
                addressIndexTruck2.remove(nextIndexForDistances2)
            distancesAddressIndexTruck2.clear()
        moving = moving + 1

    returnValues = list()
    returnValues.append(totalMiles)
    returnValues.append(currentTimeTruck2)
    return returnValues