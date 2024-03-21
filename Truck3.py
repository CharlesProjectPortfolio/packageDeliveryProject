import math
import datetime
from PackageClass import Package

def delivery3(address, truck3, distancesList, truckSpeed, currentTimeTruck1, totalMiles, myHash):
    nextAddressIndex3 = 0  # Holds to index for the minimum distance in distancesAddressIndexTruck3
    nextIndexForDistances3 = 0  # Holds the value at that index position in addressIndexTruck3
    distancesAddressIndexTruck3 = list()  # List to determine which address on the truck is the next closest address
    addressIndexTruck3 = list()
    placeHolder = list()
    moving = 0

    countInd = 0
    for i in truck3:  # O(n^2)
        for j in address:
            if i.address == j:
                addressIndexTruck3.append(countInd)
                break
            countInd = countInd + 1
        countInd = 0

    # While loop is O(n^3)
    while addressIndexTruck3:  # While loop to iterate through truck3 and deliver the packages to the next closest address
        if moving == 0:  # If first iteration of the while loop, get the closest address to the HUB
            for i in addressIndexTruck3:  # Loop through a list of index positions from address
                for j in range(len(distancesList[moving])):  # Use the index to get the row in distancesList
                    # Since addressList and DistancesList are both ordered the index from addressList
                    # will match up to the distance in that row of distancesList
                    if j == i:  # Check if j and i math index values
                        # If they match put the distance into distancesAddressIndexTruck3
                        distancesAddressIndexTruck3.append(distancesList[moving][j])
                        break
            for i in truck3:  # Start with package 25 to 10:30 delivery deadline
                if i.ID != 25:
                    continue
                for j in range(len(addressIndexTruck3)):
                    if i.address == address[addressIndexTruck3[j]]:
                        placeHolder.append(j)

            # force the delivery of package number 25 to meet the 10:30 AM deadline
            milesTraveled3 = distancesAddressIndexTruck3[placeHolder[0]]  # Add the distance traveled to the next address to milesTraveled

        elif moving == 1:
            for i in addressIndexTruck3:  # Loop through a list of index positions from address
                for j in range(
                        len(distancesList[nextIndexForDistances3])):  # Use the index to get the row in distancesList
                    # Since addressList and DistancesList are both ordered the index from addressList
                    # will match up to the distance in that row of distancesList
                    if j == i:  # Check if j and i math index values
                        # If they match put the distance into distancesAddressIndexTruck1
                        distancesAddressIndexTruck3.append(distancesList[nextIndexForDistances3][j])
                        break
            for i in truck3:  # force next delivery to address 6 to meet 10:30 AM delivery deadline
                if i.ID != 6:
                    continue
                for j in range(len(addressIndexTruck3)):
                    if i.address == address[addressIndexTruck3[j]]:
                        placeHolder.append(j)
            # force the delivery of package number 6 to meet the 10:30 AM deadline
            milesTraveled3 = distancesAddressIndexTruck3[placeHolder[0]]  # Add the distance traveled to the next address to milesTraveled
        else:
            for i in addressIndexTruck3:
                for j in range(len(distancesList[nextIndexForDistances3])):
                    if j == i:
                        distancesAddressIndexTruck3.append(distancesList[nextIndexForDistances3][j])
                        break

            milesTraveled3 = min(distancesAddressIndexTruck3)  # Add the distance traveled to the next address to milesTraveled

        totalMiles = totalMiles + milesTraveled3  # Variable for total miles traveled
        nextIndexForDistances3 = addressIndexTruck3[distancesAddressIndexTruck3.index(milesTraveled3)]  # Use that index to get the value for the next distance list

        # Calculate minutes and seconds taken by truck1 to get to next address
        minutes = math.floor(milesTraveled3 / truckSpeed)
        seconds = round(((milesTraveled3 / truckSpeed) - (
            math.floor((milesTraveled3 / truckSpeed)))) * 60)
        currentTimeTruck1 = currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

        while nextIndexForDistances3 in addressIndexTruck3:  # remove values for already delivered packages
            for i in truck3:
                if i.address == address[nextIndexForDistances3]:
                    status = "Delivered " + str(currentTimeTruck1)
                    package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight, status)
                    myHash.insert(i.ID, package)
                    print(i.ID, "   ", i.address, "   ", address[nextIndexForDistances3])
                    truck3.remove(i)
                    break
            addressIndexTruck3.remove(nextIndexForDistances3)
        distancesAddressIndexTruck3.clear()
        moving = moving + 1

    returnValues = list()
    returnValues.append(totalMiles)
    returnValues.append(currentTimeTruck1)
    return returnValues