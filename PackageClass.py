# Package class to hold the data for the packages that will be put into the hash table
class Package:
    def __init__(self, ID, address, city, state, zipCode, deliveryDeadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.status = status

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID,
                                                   self.address,
                                                   self.city,
                                                   self.state,
                                                   self.zipCode,
                                                   self.deliveryDeadline,
                                                   self.weight,
                                                   self.status)
