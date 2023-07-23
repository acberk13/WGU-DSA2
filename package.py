# creates a class for a Package object
class Package:
    def __init__(self, id, address, city, state, zip, delivery_deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.time_delivered = None
        self.delivery_status = False
        self.truck_number = 0

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s ,%s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                   self.delivery_deadline, self.weight, self.notes)
