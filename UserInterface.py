import math
import datetime

def interface(totalMiles, myHash, finishedTruck1, combinedCorrectAddressTime, checkTruck3):
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
                packageHolder = myHash.search(i + 1)
                statusHolder = datetime.datetime.strptime(packageHolder.status[10:len(packageHolder.status)],
                                                          '%Y-%m-%d %H:%M:%S')
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