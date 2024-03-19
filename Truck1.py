import math
import datetime
from PackageClass import Package

class TruckOneDelivery:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    addressIndexTruck1 = list()
    def __init__(self, truck1, address, distancesList, truckSpeed, myHash, totalMiles, currentTimeTruck1, distBackToHub):
        self.truck1 = truck1
        self.address = address
        self.distancesList = distancesList
        self.truckSpeed = truckSpeed
        self.myHash = myHash
        self.totalMiles = totalMiles
        self.currentTimeTruck1 = currentTimeTruck1
        self.distBackToHub = distBackToHub


    def set_addressIndexTruck1(self):
        # Loop to match the addresses from truck1 and the addresses list and put them into addressIndexTruck1
        countInd = 0
        for i in self.truck1:  # O(n^2)
            for j in self.address:
                if i.address == j:
                    self.addressIndexTruck1.append(countInd)
                    break
                countInd = countInd + 1
            countInd = 0

    def delivery(self):
        nextIndexForDistances = 0  # Holds the value at that index position in addressIndexTruck1
        distancesAddressIndexTruck1 = list()  # List to determine which address on the truck is the next closest address
        placeHolder = list()
        moving = 0

        # while loop is O(n^3)
        while self.addressIndexTruck1:  # While loop to iterate through truck 1 and deliver the packages to the next closest address
            if moving == 0:  # If first iteration of the while loop get the closest address to the HUB
                for i in self.addressIndexTruck1:  # Loop through a list of index positions from address
                    for j in range(len(self.distancesList[moving])):  # Use the index to get the row in distancesList
                        # Since addressList and DistancesList are both ordered the index from addressList
                        # will match up to the distance in that row of distancesList
                        if j == i:  # Check if j and i math index values
                            # If they match put the distance into distancesAddressIndexTruck1
                            distancesAddressIndexTruck1.append(self.distancesList[moving][j])
                            break
                for i in self.truck1:
                    if i.ID != 15:
                        continue
                    for j in range(len(self.addressIndexTruck1)):
                        if i.address == self.address[self.addressIndexTruck1[j]]:
                            placeHolder.append(j)

                # force the delivery of package number 15 to meet the 9 AM deadline
                milesTraveled = distancesAddressIndexTruck1[
                    placeHolder[0]]  # Add the distance traveled to the next address to milesTraveled
                self.totalMiles = self.totalMiles + milesTraveled  # variable for total miles traveled
                nextAddressIndex = distancesAddressIndexTruck1.index(milesTraveled)  # get index of minimum
                nextIndexForDistances = self.addressIndexTruck1[
                    nextAddressIndex]  # Use that index to get the value for the next distance list

                # Calculate minutes and seconds taken by truck1 to get to next address
                minutes = math.floor(milesTraveled / self.truckSpeed)
                seconds = round(((milesTraveled / self.truckSpeed) - (math.floor((milesTraveled / self.truckSpeed)))) * 60)
                self.currentTimeTruck1 = self.currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

                placeHolderValue = self.addressIndexTruck1[placeHolder[0]]
                while milesTraveled in distancesAddressIndexTruck1:  # remove values for already delivered packages from truck1
                    for i in self.truck1:
                        if i.address == self.address[placeHolderValue]:
                            status = "Delivered " + str(self.currentTimeTruck1)
                            package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight,
                                              status)
                            self.myHash.insert(i.ID, package)
                            self.truck1.remove(i)
                            break
                    distancesAddressIndexTruck1.remove(milesTraveled)
                    self.addressIndexTruck1.remove(nextIndexForDistances)

                distancesAddressIndexTruck1.clear()
                placeHolder.clear()

            else:
                for i in self.addressIndexTruck1:
                    for j in range(len(self.distancesList[nextIndexForDistances])):
                        if j == i:
                            distancesAddressIndexTruck1.append(self.distancesList[nextIndexForDistances][j])
                            break

                milesTraveled = min(
                    distancesAddressIndexTruck1)  # Add the distance traveled to the next address to milesTraveled
                self.totalMiles = self.totalMiles + milesTraveled  # Variable for total miles traveled
                nextAddressIndex = distancesAddressIndexTruck1.index(
                    min(distancesAddressIndexTruck1))  # get index of minimum
                nextIndexForDistances = self.addressIndexTruck1[
                    nextAddressIndex]  # Use that index to get the value for the next distance list

                if len(self.addressIndexTruck1) == 1:
                    backToHub = nextIndexForDistances

                # Calculate minutes and seconds taken by truck1 to get to next address
                minutes = math.floor(min(distancesAddressIndexTruck1) / self.truckSpeed)
                seconds = round(((min(distancesAddressIndexTruck1) / self.truckSpeed) - (
                    math.floor((min(distancesAddressIndexTruck1) / self.truckSpeed)))) * 60)
                self.currentTimeTruck1 = self.currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)

                holder = self.addressIndexTruck1[nextAddressIndex]
                while nextIndexForDistances in self.addressIndexTruck1:  # remove values for already delivered packages
                    for i in self.truck1:
                        if i.address == self.address[nextIndexForDistances]:
                            status = "Delivered " + str(self.currentTimeTruck1)
                            package = Package(i.ID, i.address, i.city, i.state, i.zipCode, i.deliveryDeadline, i.weight,
                                              status)
                            self.myHash.insert(i.ID, package)
                            self.truck1.remove(i)
                            break
                    self.addressIndexTruck1.remove(nextIndexForDistances)
                distancesAddressIndexTruck1.clear()
            moving = moving + 1

        self.distBackToHub = self.distancesList[0][self.distBackToHub]  # Get the distance from the last address back to the hub
        self.totalMiles = self.totalMiles + self.distBackToHub  # Add the distance to totalMiles
        # Calculate the time to travel that distance and add it to the current time
        minutes = math.floor(self.distBackToHub / self.truckSpeed)
        seconds = round(((self.distBackToHub / self.truckSpeed) - (
            math.floor((self.distBackToHub / self.truckSpeed)))) * 60)
        self.currentTimeTruck1 = self.currentTimeTruck1 + datetime.timedelta(minutes=minutes, seconds=seconds)
