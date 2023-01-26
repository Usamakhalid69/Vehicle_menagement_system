import csv
from prettytable import PrettyTable
from tabulate import tabulate


class vehicle_inventory:
    all = []

    def __init__(self, type_car, make, name, model, variant, mileage, engine_type, cc, colour, rating,
                 registration, registered_city, chassis_no: str, price, purchasing_date, selling_date, purchasing_price,
                 selling_price, profit_loss):
        self.type_car = type_car
        self.make = make
        self.name = name
        self.model = model
        self.variant = variant
        self.mileage = mileage
        self.colour = colour
        self.engine_type = engine_type
        self.cc = cc
        self.rating = rating
        self.registration = registration
        self.registration_city = registered_city
        self.chassis_no = chassis_no
        self.price = price
        self.purchasing_date = purchasing_date
        self.selling_date = selling_date
        self.purchasing_price = purchasing_price
        self.selling_price = selling_price
        self.profit_loss = profit_loss
        vehicle_inventory.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        table = PrettyTable(
            ["type_car", "name", "make", "model", "variant", "mileage", "colour", "engine_type", " cc", "rating",
             "registration", "registration_city", "chassis_no", "price", "selling_date",
             "purchasing_date",
             "purchasing_price", "selling_price", "profit_loss"])
        with open('inventory.csv', 'a', newline="") as csvfile:
            fieldnames = ["type_car", "name", "make", "model", "variant", "mileage", "colour", "engine_type", "cc",
                          "rating",
                          "registration", "registration_city", "chassis_no", "price", "selling_date", "purchasing_date",
                          "purchasing_price", "selling_price", "profit_loss"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()

            while True:
                type_car = ''
                name = ''
                make = ''
                model = ''
                variant = ''
                mileage = ''
                engine_type = ''
                cc = ''
                colour = ''
                rating = ''
                registration_city = ''
                registration = ''
                chassis_no = ''
                price = ''
                purchasing_date = ''
                selling_date = ''
                purchasing_price = ''
                selling_price = ''
                profit_loss = ''
                option = input(
                    "YOu want to Add Vehicle or delete record of the vehicle\nPress 1 for Adding vehicle record\nPress 2 for Deleting vehicle record\nPress 3 to show complete inventory\nENTER: ")
                if option == "1":
                    print(
                        "WELCOME TO ELITE MOTORS\nYou CAN ADD VEHICLES DETAILS IN ELITE MOTORS PORTAL \nCategories\n1.car\n2.jeep\n3.pickup")
                    type_car = input("please enter the type of the car: ")
                    if type_car == "car":
                        name = input("Enter name of the car: ")
                    elif type_car == "jeep":
                        name = input("Enter name of the jeep: ")
                    elif type_car == "pickup":
                        name = input("Enter name of the pickup: ")
                    make = input("please enter the make of the car : ")
                    model = input('Please enter the model of the car: ')
                    variant = input('Please enter the variant of the car: ')
                    mileage = input('Please enter the mileage of the car: ')
                    engine_type = input('Please enter the engine_type of the car: ')
                    cc = input("Please enter the engine capacity: ")
                    colour = input('Please enter the colour of  the car: ')
                    rating = input("please enter the rating of the car: ")
                    registration_city = input("please enter the registration city: ")
                    registration = input("please enter the registration: ")

                    if registration == "" and registration_city == "":
                        print("Not REGISTERED please enter the chassis_no: ")
                        chassis_no = input("ENtER chassis no")

                    price = input("please enter the price: ")
                    purchasing_date = input('Please enter the purchasing_date of the vehicle: ')
                    selling_date = input('Please enter the selling date of the vehicle: ')
                    purchasing_price = input('Please enter the purchasing price of the vehicle : ')
                    selling_price = input("please enter the selling price of the vehicle: ")
                    profit_loss = float(selling_price) - float(purchasing_price)
                    if selling_price > purchasing_price:
                        print("profit", profit_loss)
                    elif purchasing_price > selling_price:
                        print("loss", profit_loss)
                    else:
                        print("no profit no loss")
                elif option == "2":
                    file = open("inventory.csv", "r")
                    reader = csv.reader(file)
                    l = []
                    uroll = input("enter the registration of the vehicle to delete : ")
                    found = False
                    for row in reader:
                        if row[10] == str(uroll):
                            found = True
                        else:
                            l.append(row)

                    file.close()
                    if not found:
                        print("vehicle not found")
                    else:
                        file = open("inventory.csv", "w+", newline="")
                        writer = csv.writer(file)
                        writer.writerows(l)
                        file.seek(0)
                        reader = csv.reader(file)
                        file.close()

                    with open("inventory.csv") as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        table.fieldnames = fieldnames
                        for row in reader:
                            table.add_row(row)
                    print(table)
                elif option == "3":
                    with open('inventory.csv', 'r') as f:
                        reader = csv.reader(f)
                        print(tabulate(reader))


                writer.writerow(
                    {"type_car": type_car, "name": name, "make": make, "model": model, "variant": variant,
                     "mileage": mileage,
                     "colour": colour,
                     "engine_type": engine_type, "cc": cc, "rating": rating, "registration": registration,
                     "registration_city": registration_city, "chassis_no": chassis_no, "price": price,
                     "purchasing_date": purchasing_date, "selling_date": selling_date,
                     "purchasing_price": purchasing_price,
                     "selling_price": selling_price, "profit_loss": profit_loss})
                break

class elite_motors_buyer(vehicle_inventory):

    def __init__(self, type_car, name, make, model, cc, engine_type, variant, mileage, colour, rating,
                 registration_city, price):
        self.type_car = type_car
        self.name = name
        self.make = make
        self.model = model
        self.cc = cc
        self.engine_type = engine_type
        self.variant = variant
        self.mileage = mileage
        self.colour = colour
        self.rating = rating
        self.registration_city = registration_city
        self.price = price

        elite_motors_buyer.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):

        table = PrettyTable(
            ["name", "make", "model", "variant", "cc", "mileage", "colour", "engine_type", "rating", "registration_city"
                , "price"])
        print("WELCOME TO ELITE MOTORS\nYOU WANT TO BUY WHICH VEHICLE: ")

        def searchbyname():
            all_: list = []
            headers = ["VEHICLE", "DETAILS"]
            name_car = input("Enter the name of the car: ")
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)
                csv.reader = reader
                for row in csv.reader:
                    if row[1] == name_car:
                        all_.append(row)
                        x = [["name", name_car], ["make", row[2]], ["model", row[3]], ["variant", row[4]],
                             ["mileage", row[5]], ["colour", row[6]], ["engine_type", row[7]], ["cc", row[8]],
                             ["rating", row[9]],
                             ["registration_city", row[11]], ["price", row[13]]]
                        print(tabulate(x,headers=headers))

        def searchbymake():
            all_: list = []
            headers = ["VEHICLE", "DETAILS"]
            make_car = input("Enter the name of the car: ")
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)
                csv.reader = reader
                for row in csv.reader:
                    if row[2] == make_car:
                        all_.append(row)
                        x = [["name", row[1]], ["make", make_car], ["model", row[3]], ["variant", row[4]],
                             ["mileage", row[5]], ["colour", row[6]], ["engine_type", row[7]], ["cc", row[8]],
                             ["rating", row[9]],
                             ["registration_city", row[11]], ["price", row[13]]]
                        print(tabulate(x,headers=headers))
        def searchbyregisterationcity():
            all_: list = []
            headers = ["VEHICLE", "DETAILS"]
            name_registration_city = input("Enter the registration city of the car: ")
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)
                csv.reader = reader
                for row in csv.reader:
                    if row[11] == name_registration_city :
                        all_.append(row)
                        x = [["name",row[1]], ["make", row[2]], ["model", row[3]], ["variant", row[4]],
                             ["mileage", row[5]], ["colour", row[6]], ["engine_type", row[7]], ["cc", row[8]],
                             ["rating", row[9]],
                             ["registration_city",name_registration_city ], ["price", row[13]]]
                        print(tabulate(x,headers=headers))

        print("Enter 1 to search by vehicle name: ")
        print("Enter 2 to search by vehicle brand :")
        print("Enter 3 to search by vehicle Registration_city")
        src = input("Enter : ")
        if src == "1":
            searchbyname()
        elif src == "2":
            searchbymake()
        elif src == "3":
            searchbyregisterationcity()
        else:
            print("sorry invalid input")



    def load_data(elitemotors_buyer):
        mylist = []
        with open("inventory.csv") as numbers:
            numbers_data = csv.reader(numbers, delimiter=",")
            next(numbers_data)
            for row in numbers_data:
                mylist.append(row)
            return mylist

def main():
    usertype = input("WELCOME TO ELITE MOTORS\n1.owner\n2.buyer\nEnter Please:")

    if usertype == "1":
        return vehicle_inventory.instantiate_from_csv()
    elif usertype == "2":
        return elite_motors_buyer.instantiate_from_csv()
    else:
        print("invalid")


main()

