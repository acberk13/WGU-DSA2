# Andrew Berkler Student ID 010479517

import datetime
from hash import *
from truck import *
from package import *


# A nearest neighbor algorithm is used to determine the closest next package for delivery.  Trucks are loaded manually,
# then the algorithm determines the closest stop to the hub for the first delivery, the closest stop to the first
# delivery and so on until all packages are delivered and the truck returns to the hub.  This algorithm has time
# complexity of O(n^2) as it uses nested for loops.
# O(n^2) quadratic time
def package_delivery_algorithm(truck):
    print("\nTruck", truck.truck_number, "Time left hub:", truck.time)

    # loop through each package on truck
    for i in truck.packages:
        next_package = None
        shortest_distance = 999  # initializes the shortest distance to an arbitrarily large number ensuring that the
        # first package checked will become the next package

        # loop through each package id on truck, update the address for Package 9 at 10:20 once the right information
        # has been received
        for package_id in truck.packages:
            if truck.time > datetime.timedelta(hours=10, minutes=20):
                p9.address = "410 S State St"

            # get the package information using search function from hash table
            package = hash_table.search(package_id)

            # stores the distance between 2 trucks address and the package destination
            distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary[package.address]]

            # nearest neighbor algorithm checks for closest address to current location
            # if the next package checked has a shorter distance and has not been delivered yet it becomes
            # the next package
            if distance < shortest_distance and package.time_delivered is None:
                next_package = package
                shortest_distance = distance

        # package with shortest distance becomes next package to be delivered
        package = next_package
        if package is not None:

            # calculates truck mileage and delivery times using constant speed of 18 miles per hour
            distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary[package.address]]
            truck.mileage += distance
            truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))

            truck.address = package.address
            package.time_delivered = truck.time
            package.delivery_status = True
            package.truckNumber = truck.truck_number
            print("\nPackage:", package.id, "\tTruck Number:", truck.truck_number,
                  "\nDistance from last stop:", distance, "\nTime Delivered:", package.time_delivered,
                  "\nDelivery Deadline:", package.delivery_deadline, "\nAddress Delivered to: ", package.address,
                  package.city, package.state, package.zip, "\nWeight:", package.weight, "\nSpecial Notes:", package.notes)
    distance = distance_2d_array[address_dictionary[truck.address]][address_dictionary["4001 South 700 East"]]
    truck.mileage += distance
    truck.time += datetime.timedelta(minutes=(distance / (18 * (1 / 60))))
    print("Truck", truck.truck_number, "Time returned to hub:", truck.time, "\tReturn distance:", distance)

# creates package objects and binds them to a variable
# O(1) constant time
p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30", 21, "")
p2 = Package(2, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 44, "")
p3 = Package(3, "233 Canyon Rd", "Salt Lake City", "UT", 84103, "EOD", 2, "Can only be on truck 2")
p4 = Package(4, "380 W 2880 S", "Salt Lake City", "UT", 84115, "EOD", 4, "")
p5 = Package(5, "410 S State St", "Salt Lake City", "UT", 84111,"EOD", 5, "")
p6 = Package(6, "3060 Lester St", "West Valley City", "UT", 84119, "10:30 AM", 88,
             "Delayed on flight--will not arrive to depot until 9:05 a.m.")
p7 = Package(7, "1330 2100 S", "Salt Lake City", "UT", 84106, "EOD", 8, "")
p8 = Package(8, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 9, "")
p9 = Package(9, "300 State St", "Salt Lake City", "UT", 84103, "EOD", 2, "Wrong address listed")
p10 = Package(10, "600 E 900 South", "Salt Lake City", "UT", 84105,"EOD", 1, "")
p11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "UT", 84118, "EOD", 1, "")
p12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "UT", 84119, "EOD", 1, "")
p13 = Package(13, "2010 W 500 S", "Salt Lake City", "UT", 84104, "10:30 AM", 2, "")
p14 = Package(14, "4300 S 1300 E", "Millcreek", "UT", 84117, "10:30 AM", 88, "Must be delivered with 15, 19")
p15 = Package(15, "4580 S 2300 E", "Holladay", "UT", 84117, "9:00 AM", 4, "")
p16 = Package(16, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 88, "Must be delivered with 13, 19")
p17 = Package(17, "3148 S 1100 W", "Salt Lake City", "UT", 84119, "EOD", 2, "")
p18 = Package(18, "1488 4800 S", "Salt Lake City", "UT", 84123, "EOD", 6, "Can only be on truck 2")
p19 = Package(19, "177 W Price Ave", "Salt Lake City", "UT", 84115, "EOD", 37, "")
p20 = Package(20, "3595 Main St", "Salt Lake City", "UT", 84115, "10:30 AM", 37, "Must be delivered with 13, 15")
p21 = Package(21, "3595 Main St", "Salt Lake City", "UT", 84115, "EOD", 3, "")
p22 = Package(22, "6351 South 900 East", "Murray", "UT", 84121, "EOD", 2, "")
p23 = Package(23, "5100 South 2700 West", "Salt Lake City", "UT", 84118, "EOD", 5, "")
p24 = Package(24, "5025 State St", "Murray", "UT", 84107, "EOD", 7, "")
p25 = Package(25, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "10:30 AM", 7,
              "Delayed on flight--will not arrive to depot until 9:05 am")
p26 = Package(26, "5383 S 900 East #104", "Salt Lake City", "UT", 84117, "EOD", 25, "")
p27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 5, "")
p28 = Package(28, "2835 Main St", "Salt Lake City", "UT", 84115, "EOD", 7,
              "Delayed on flight--will not arrive to depot until 9:05")
p29 = Package(29, "1330 2100 S", "Salt Lake City", "UT", 84106, "10:30 AM", 2, "")
p30 = Package(30, "300 State St", "Salt Lake City", "UT", 84103, "10:30 AM", 1, "")
p31 = Package(31, "3365 S 900 W", "Salt Lake City", "UT", 84119, "10:30 AM", 1, "")
p32 = Package(32, "3365 S 900 W", "Salt Lake City", "UT", 84119, "EOD", 1,
              "Delayed on flight--will not arrive to depot until 9:05 am")
p33 = Package(33, "2530 S 500 E", "Salt Lake City", "UT", 84106, "EOD", 1, "")
p34 = Package(34, "4580 S 2300 E", "Holladay", "UT", 84117, "10:30 AM", 2, "")
p35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "UT", 84104, "EOD", 88, "")
p36 = Package(36, "2300 Parkway Blvd", "West Valley City", "UT", 84119, "EOD", 88, "Can only be on truck 2")
p37 = Package(37, "410 S State St", "Salt Lake City", "UT", 84111, "10:30 AM", 2, "")
p38 = Package(38, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", 9, "Can only be on truck 2")
p39 = Package(39, "2010 W 500 S", "Salt Lake City", "UT", 84104, "EOD", 9, "")
p40 = Package(40, "380 W 2880 S", "Salt Lake City", "UT", 84115, "10:30 AM", 45, "")


# hash table instance
hash_table = ChainingHashTable()

# insert package objects into hash table
# O(1) constant time
hash_table.insert(1, p1)
hash_table.insert(2, p2)
hash_table.insert(3, p3)
hash_table.insert(4, p4)
hash_table.insert(5, p5)
hash_table.insert(6, p6)
hash_table.insert(7, p7)
hash_table.insert(8, p8)
hash_table.insert(9, p9)
hash_table.insert(10, p10)
hash_table.insert(11, p11)
hash_table.insert(12, p12)
hash_table.insert(13, p13)
hash_table.insert(14, p14)
hash_table.insert(15, p15)
hash_table.insert(16, p16)
hash_table.insert(17, p17)
hash_table.insert(18, p18)
hash_table.insert(19, p19)
hash_table.insert(20, p20)
hash_table.insert(21, p21)
hash_table.insert(22, p22)
hash_table.insert(23, p23)
hash_table.insert(24, p24)
hash_table.insert(25, p25)
hash_table.insert(26, p26)
hash_table.insert(27, p27)
hash_table.insert(28, p28)
hash_table.insert(29, p29)
hash_table.insert(30, p30)
hash_table.insert(31, p31)
hash_table.insert(32, p32)
hash_table.insert(33, p33)
hash_table.insert(34, p34)
hash_table.insert(35, p35)
hash_table.insert(36, p36)
hash_table.insert(37, p37)
hash_table.insert(38, p38)
hash_table.insert(39, p39)
hash_table.insert(40, p40)

# distance arrays between delivery locations
# Western Governors University
dist_to_WGU = [0, 7.2, 3.8, 11, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7,
               7.6, 2, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4, 2.4, 5, 3.6]
# International Peace Gardens
dist_to_IPG = [7.2, 0, 7.1, 6.4, 6, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3, 4.6, 4.5, 7.4,
               6, 5, 4.8, 9.5, 10.9, 8.3, 6.9, 10, 4.4, 13]
# Sugar House Park
dist_to_SHP = [3.8, 7.1, 0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3, 5.3, 6.5, 5.6, 5.8, 5.7,
               4.1, 3.6, 4.3, 3.3, 5, 6.1, 9.7, 6.1, 2.8, 7.4]
# Taylorsville-Bennion Heritage
dist_to_TBHC = [11, 6.4, 9.2, 0, 5.6, 6.9, 8.6, 4, 11.1, 7.3, 1, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2,
                5.3, 6, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1]
# Salt Lake City Division of Health Services
dist_to_SLCDHS = [2.2, 6, 4.4, 5.6, 0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4,
                  0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6, 4.2, 5.4, 5.5]
# South Salt Lake Public Works
dist_to_SSLPW = [3.5, 4.8, 2.8, 6.9, 1.9, 0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3, 3.8, 5.7,
                 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9, 5.9, 3.5, 7.2]
# Salt Lake City Streets and Sanitation
dist_to_SLCSS = [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0, 4, 4.2, 8, 8.6, 6.9, 4.2, 4.2, 8, 5.8, 7.2, 7.7,
                 6.6, 3.2, 11.2, 12.7, 10, 8.2, 11.7, 5.1, 14.2]
# Deker Lake
dist_to_DL = [8.6, 2.8, 6.3, 4, 5.1, 4.3, 4, 0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1,
              4.6, 6.7, 8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7]
# Salt Lake City Ottinger Hall
dist_to_SLCOH = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2,
                 5.9, 5.4, 1, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1]
# Columbus Library
dist_to_CL = [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8, 9.3, 4.8, 0, 9.4, 1.1, 5.1, 4.6, 3.7, 4, 6.7, 2.3,
              1.8, 4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6]
# Taylorsville City Hall
dist_to_TCH = [6.4, 7.3, 10.4, 1, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0, 7.3, 12, 4.9, 5.2, 5.4, 8.1, 6.2,
               6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11, 6.8]
# South Salt Lake Police
dist_to_SSLP = [3.2, 5.3, 3, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2,
                1, 3.7, 4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4]
# Council Hall
dist_to_CH = [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12, 4.7, 0, 7.3, 7.8, 6.6, 7.2, 5.9,
              5.4, 1, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1]
# Redwood Park
dist_to_RP = [5.2, 3, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0, 1.3, 1.5, 4, 3.2,
              3, 6.9, 6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5]
# Salt Lake County Mental Health
dist_to_SLCMH = [4.4, 4.6, 5.6, 4.3, 2.4, 3, 8, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0, 0.6, 6.4,
                 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8]
# Salt Lake County/United Police Dept
dist_to_SLCUPD = [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4, 5.4, 2.9, 6.6, 1.5, 0.6, 0, 5.6,
                  1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4]
# West Valley Prosecutor
dist_to_WVP = [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4, 6.4, 5.6, 0, 7.1,
               6.1, 7.2, 10.6, 12, 9.4, 7.5, 11.1, 6.2, 13.6]
# Housing Auth. of Salt Lake County
dist_to_HASLC = [2, 6, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0,
                 1.6, 4.9, 3, 5, 2.3, 5.5, 4, 5.1, 5.2]
# Utah DMV Administrative Office
dist_to_UDMV = [3.6, 5, 3.6, 6, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1, 5.4, 3, 2.2, 1.7, 6.1, 1.6, 0,
                4.4, 4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9]
# Third District Juvenile Court
dist_to_TDJC = [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1, 4.1, 11.5, 3.7, 1, 6.9, 6.8, 6.4, 7.2,
                4.9, 4.4, 0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1]
# Cottonwood Regional Softball Complex
dist_to_CRSC = [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6,
                3, 4.6, 7.5, 0, 2, 2.9, 6.4, 2.8, 6, 4.1]
# Holiday City Office
dist_to_HCO = [3.4, 10.9, 5, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12,
               5, 6.6, 9.3, 2, 0, 4.4, 7.9, 3.4, 7.9, 4.7]
# Murray City Museum
dist_to_MCM = [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3,
               3.9, 6.8, 2.9, 4.4, 0, 4.5, 1.7, 6.8, 3.1]
# Valley Regional Softball Complex
dist_to_VRSC = [6.4, 6.9, 9.7, 0.6, 6, 9, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5,
                6.5, 11.4, 6.4, 7.9, 4.5, 0, 5.4, 10.6, 7.8]
# City Center of Rock Springs
dist_to_CCRS = [2.4, 10, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4,
                5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0, 7, 1.3]
# Rice Terrace Pavilion Park
dist_to_RTPP = [5, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1,
                4.3, 1.8, 6, 7.9, 6.8, 10.6, 7, 0, 8.3]
# Wheeler Historic Farm
dist_to_WHF = [3.6, 13, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2,
               6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0]

# 2D array containing the distance arrays between addresses
distance_2d_array = [dist_to_WGU, dist_to_IPG, dist_to_SHP, dist_to_TBHC, dist_to_SLCDHS, dist_to_SSLPW, dist_to_SLCSS,
                     dist_to_DL, dist_to_SLCOH, dist_to_CL, dist_to_TCH, dist_to_SSLP, dist_to_CH, dist_to_RP,
                     dist_to_SLCMH, dist_to_SLCUPD, dist_to_WVP, dist_to_HASLC, dist_to_UDMV, dist_to_TDJC,
                     dist_to_CRSC, dist_to_HCO, dist_to_MCM, dist_to_VRSC, dist_to_CCRS, dist_to_RTPP, dist_to_WHF]


# dictionary associating an address to a member location in the 2d distance array
# O(1) constant time
address_dictionary = {"4001 South 700 East": 0, "1060 Dalton Ave S": 1, "1330 2100 S": 2, "1488 4800 S": 3,
                      "177 W Price Ave": 4, "195 W Oakland Ave": 5, "2010 W 500 S": 6, "2300 Parkway Blvd": 7,
                      "233 Canyon Rd": 8, "2530 S 500 E": 9, "2600 Taylorsville Blvd": 10, "2835 Main St": 11,
                      "300 State St": 12, "3060 Lester St": 13, "3148 S 1100 W": 14, "3365 S 900 W": 15,
                      "3575 W Valley Central Station bus Loop": 16, "3595 Main St": 17, "380 W 2880 S": 18,
                      "410 S State St": 19, "4300 S 1300 E": 20, "4580 S 2300 E": 21, "5025 State St": 22,
                      "5100 South 2700 West": 23, "5383 S 900 East #104": 24, "600 E 900 South": 25,
                      "6351 South 900 East": 26}

# manually load truck 1
truck1_packages_id = [p1.id, p13.id, p14.id, p15.id, p16.id, p19.id, p20.id, p29.id, p30.id, p31.id, p34.id, p37.id, p40.id]

# truck 1 object
truck1_departure_time = datetime.timedelta(hours=8, minutes=0)
truck1 = Truck(truck1_packages_id, "4001 South 700 East", 0, truck1_departure_time, 1)

# manually load truck 2
truck2_packages_id = [p3.id, p6.id, p18.id, p22.id, p23.id, p25.id, p27.id, p28.id, p32.id, p33.id,
                      p35.id, p36.id, p38.id]

# truck 2 object
truck2_departure_time = datetime.timedelta(hours=9, minutes=5)  # Truck 2 waits at hub until 9:05 to wait for package 6,
# 25, 28, and 32 which were delayed on flight
truck2 = Truck(truck2_packages_id, "4001 South 700 East", 0, truck2_departure_time, 2)

# manually load truck 3
truck3_packages_id = [p2.id, p4.id, p5.id, p7.id, p8.id, p9.id, p10.id, p11.id, p12.id, p17.id,
                      p21.id, p24.id, p26.id, p39.id]

# truck 3 object
truck3_departure_time = datetime.timedelta(hours=10, minutes=20)  # Truck 1 returned to the hub at 9:53, driver waits
# at Hub until 10:20 to get the correct address information for Package 9 then leaves in Truck 3 at 10:20
truck3 = Truck(truck3_packages_id, "4001 South 700 East", 0, truck3_departure_time, 3)

print("Truck 1 packages: ", truck1_packages_id)
print("Truck 2 packages: ", truck2_packages_id)
print("Truck 3 packages: ", truck3_packages_id)

# run the nearest neighbor algorithm on packages in each truck
package_delivery_algorithm(truck1)
package_delivery_algorithm(truck2)
package_delivery_algorithm(truck3)

# list of all package ids
# O(1) constant time
all_packages = [p1.id, p2.id, p3.id, p4.id, p5.id, p6.id, p7.id, p8.id, p9.id, p10.id, p11.id, p12.id, p13.id, p14.id,
                p15.id, p16.id, p17.id, p18.id, p19.id, p20.id, p21.id, p22.id, p23.id, p24.id, p25.id, p26.id,
                p27.id, p28.id, p29.id, p30.id, p31.id, p32.id, p33.id, p34.id,
                p35.id, p36.id, p37.id, p38.id, p39.id, p40.id]


# for loop that iterates through package ids on each truck
# O(n) linear time
for i in all_packages:
    package = hash_table.search(i)
    print("Package:", package.id, "Delivery Time:", package.time_delivered)

print("Truck 1 mileage: ", truck1.mileage)
print("Truck 2 mileage: ", truck2.mileage)
print("Truck 3 mileage: ", truck3.mileage)
total_mileage = (truck1.mileage + truck2.mileage + truck3.mileage)
print("Total Miles Traveled: ", total_mileage)

# loops through all packages to display status at 9:24
# O(n) linear time
testTime1 = datetime.timedelta(hours=9, minutes=24)
testPackageDeliveryStatusMessage = ""
print("\nStatus of packages at", testTime1)

for i in all_packages:
    package = hash_table.search(i)

    delivery_status_message = ""

    if package.truckNumber == 1:
        if testTime1 <= truck1_departure_time:
            delivery_status_message = "at the hub"
        elif truck1_departure_time < testTime1 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime1 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 2:
        if testTime1 <= truck2_departure_time:
            delivery_status_message = "at the hub"
        elif truck2_departure_time < testTime1 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime1 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 3:
        if testTime1 <= truck3_departure_time:
            delivery_status_message = "at the hub"
        elif truck3_departure_time < testTime1 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime1 >= package.time_delivered:
            delivery_status_message = "delivered"
    print("Package:", package.id, "Status:", delivery_status_message)


# loops through all packages to check status at 10:24
# O(n) linear time
testTime2 = datetime.timedelta(hours=10, minutes=24)
print("\nStatus of packages at", testTime2)

for i in all_packages:
    package = hash_table.search(i)

    delivery_status_message = ""

    if package.truckNumber == 1:
        if testTime2 <= truck1_departure_time:
            delivery_status_message = "at the hub"
        elif truck1_departure_time < testTime2 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime2 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 2:
        if testTime2 <= truck2_departure_time:
            delivery_status_message = "at the hub"
        elif truck2_departure_time < testTime2 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime2 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 3:
        if testTime2 <= truck3_departure_time:
            delivery_status_message = "at the hub"
        elif truck3_departure_time < testTime2 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime2 >= package.time_delivered:
            delivery_status_message = "delivered"
    print("Package:", package.id, "Status:", delivery_status_message)

# loops through all packages to check status at 13:11
# O(n) linear time
testTime3 = datetime.timedelta(hours=13, minutes=11)
print("\nStatus of packages at", testTime3)

for i in all_packages:
    package = hash_table.search(i)

    delivery_status_message = ""

    if package.truckNumber == 1:
        if testTime3 <= truck1_departure_time:
            delivery_status_message = "at the hub"
        elif truck1_departure_time < testTime3 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime3 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 2:
        if testTime3 <= truck2_departure_time:
            delivery_status_message = "at the hub"
        elif truck2_departure_time < testTime3 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime3 >= package.time_delivered:
            delivery_status_message = "delivered"
    if package.truckNumber == 3:
        if testTime3 <= truck3_departure_time:
            delivery_status_message = "at the hub"
        elif truck3_departure_time < testTime3 < package.time_delivered:
            delivery_status_message = "en route"
        elif testTime3 >= package.time_delivered:
            delivery_status_message = "delivered"
    print("Package:", package.id, "Status:", delivery_status_message)

# command line interface menu of options to check status, mileage or exit program
# O(1) constant time
while 1:
    check_continue = ''
    print('\nPlease select an option:')
    menu_choice = int(input('(1) Check Package Status '
                            '\n(2) Check All Packages '
                            '\n(3) Check Truck Mileage'
                            ' \n(4) Exit Program \n'))

    # allows user to check status of a package at a given time
    if menu_choice == 1:
        while check_continue != 'n':
            user_package_id = int(input('\n\nPlease Enter a Package ID:\n'))

            # allows user to enter a time
            user_time = input('Please enter a time using HH:MM format: ')
            (h, m) = user_time.split(':')

            user_time = datetime.timedelta(hours=int(h), minutes=int(m))

            user_package = hash_table.search(user_package_id)
            userPackageDeliveryStatusMessage = ""

            # assigns delivery status to user inputs
            if user_package.truckNumber == 1:
                if user_time <= truck1_departure_time:
                    userPackageDeliveryStatusMessage = "at the hub"
                elif truck1_departure_time < user_time < user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "en route"
                elif user_time >= user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "delivered"
            if user_package.truckNumber == 2:
                if user_time <= truck2_departure_time:
                    userPackageDeliveryStatusMessage = "at the hub"
                elif truck2_departure_time < user_time < user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "en route"
                elif user_time >= user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "delivered"
            if user_package.truckNumber == 3:
                if user_time <= truck3_departure_time:
                    userPackageDeliveryStatusMessage = "at the hub"
                elif truck3_departure_time < user_time < user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "en route"
                elif user_time >= user_package.time_delivered:
                    userPackageDeliveryStatusMessage = "delivered"

            print("\n\nUser Time:", user_time, "\nPackage:", user_package.id, "\tStatus:",
                  userPackageDeliveryStatusMessage, "\n\tDelivery Time:", user_package.time_delivered,
                  "\tDeadline:", user_package.delivery_deadline, "\n\tAddress Delivered to: ", user_package.address,
                  user_package.city, user_package.state, user_package.zip, "\n\tPackage Weight:", user_package.weight,
                  "\n\tSpecial Notes:", user_package.notes, "\n\tTruck Number:", user_package.truckNumber)

            check_continue = (input('Would you like to check another package(y/n)?'))

    if menu_choice == 2:
        user_time = input('Please enter a time using HH:MM format: ')
        (h, m) = user_time.split(':')

        user_time = datetime.timedelta(hours=int(h), minutes=int(m))

        print("\nStatus of packages at", user_time)

        for i in all_packages:
            package = hash_table.search(i)

            delivery_status_message = ""

            if package.truckNumber == 1:
                if user_time <= truck1_departure_time:
                    delivery_status_message = "at the hub"
                elif truck1_departure_time < user_time < package.time_delivered:
                    delivery_status_message = "en route"
                elif user_time >= package.time_delivered:
                    delivery_status_message = "delivered"
            if package.truckNumber == 2:
                if user_time <= truck2_departure_time:
                    delivery_status_message = "at the hub"
                elif truck2_departure_time < user_time < package.time_delivered:
                    delivery_status_message = "en route"
                elif user_time >= package.time_delivered:
                    delivery_status_message = "delivered"
            if package.truckNumber == 3:
                if user_time <= truck3_departure_time:
                    delivery_status_message = "at the hub"
                elif truck3_departure_time < user_time < package.time_delivered:
                    delivery_status_message = "en route"
                elif user_time >= package.time_delivered:
                    delivery_status_message = "delivered"
            print("Package:", package.id,
                  "\tAddress:", package.address,
                  "\nDeadline:", package.delivery_deadline,
                  "\nCity:", package.city,
                  "\tZip:", package.zip,
                  "\nWeight:", package.weight,
                  "\nStatus:", delivery_status_message)
            if delivery_status_message == "delivered":
                print("Delivery Time:", package.time_delivered)






    # prints mileage to the console
    if menu_choice == 3:
        print("\nTruck 1 mileage: ", truck1.mileage)
        print("Truck 2 mileage: ", truck2.mileage)
        print("Truck 3 mileage: ", truck3.mileage)
        total_mileage = (truck1.mileage + truck2.mileage + truck3.mileage)
        print("Total Miles Traveled: ", total_mileage)

    if menu_choice == 4:
        break

    else:
        print('\n Please enter a number 1-4:')
