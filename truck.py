# creates a class for a Truck object
class Truck:
    def __init__(self, packages, address, mileage, time, truck_number):
        self.packages = packages
        self.address = address
        self.mileage = mileage
        self.time = time
        self.truck_number = truck_number

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s" % (self.packages, self.address, self.mileage, self.time)
