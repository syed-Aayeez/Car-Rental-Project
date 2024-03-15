class Car:
    def __init__(self, carId, brand, model, basePricePerDay):
        self.carId = carId
        self.brand = brand
        self.model = model
        self.basePricePerDay = basePricePerDay
        self.isAvailable = True

    def getCarId(self):
        return self.carId

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def calculatePrice(self, rentalDays):
        return self.basePricePerDay * rentalDays

    def isAvailable(self):
        return self.isAvailable

    def rent(self):
        self.isAvailable = False

    def returnCar(self):
        self.isAvailable = True


class Customer:
    def __init__(self, customerId, name):
        self.customerId = customerId
        self.name = name

    def getCustomerId(self):
        return self.customerId

    def getName(self):
        return self.name


class Rental:
    def __init__(self, car, customer, days):
        self.car = car
        self.customer = customer
        self.days = days

    def getCar(self):
        return self.car

    def getCustomer(self):
        return self.customer

    def getDays(self):
        return self.days


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []

    def addCar(self, car):
        self.cars.append(car)

    def addCustomer(self, customer):
        self.customers.append(customer)

    def rentCar(self, car, customer, days):
        if car.isAvailable:
            car.rent()
            self.rentals.append(Rental(car, customer, days))
        else:
            print("Car is not available for rent.")

    def returnCar(self, car):
        car.returnCar()
        rentalToRemove = None
        for rental in self.rentals:
            if rental.getCar() == car:
                rentalToRemove = rental
                break
        if rentalToRemove:
            self.rentals.remove(rentalToRemove)
        else:
            print("Car was not rented.")

    def menu(self):
        while True:
            print("===== Car Rental System =====")
            print("1. Rent a Car")
            print("2. Return a Car")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\n== Rent a Car ==\n")
                customerName = input("Enter your name: ")

                print("\nAvailable Cars:")
                for car in self.cars:
                    if car.isAvailable:
                        print(car.getCarId(), "-", car.getBrand(), car.getModel())

                carId = input("\nEnter the car ID you want to rent: ")
                rentalDays = int(input("Enter the number of days for rental: "))

                newCustomer = Customer("CUS" + str(len(self.customers) + 1), customerName)
                self.addCustomer(newCustomer)

                selectedCar = None
                for car in self.cars:
                    if car.getCarId() == carId and car.isAvailable:
                        selectedCar = car
                        break

                if selectedCar:
                    totalPrice = selectedCar.calculatePrice(rentalDays)
                    print("\n== Rental Information ==\n")
                    print("Customer ID:", newCustomer.getCustomerId())
                    print("Customer Name:", newCustomer.getName())
                    print("Car:", selectedCar.getBrand(), selectedCar.getModel())
                    print("Rental Days:", rentalDays)
                    print("Total Price: $%.2f" % totalPrice)

                    confirm = input("\nConfirm rental (Y/N): ")
                    if confirm.upper() == "Y":
                        self.rentCar(selectedCar, newCustomer, rentalDays)
                        print("\nCar rented successfully.")
                    else:
                        print("\nRental canceled.")
                else:
                    print("\nInvalid car selection or car not available for rent.")

            elif choice == '2':
                print("\n== Return a Car ==\n")
                carId = input("Enter the car ID you want to return: ")

                carToReturn = None
                for car in self.cars:
                    if car.getCarId() == carId and not car.isAvailable:
                        carToReturn = car
                        break

                if carToReturn:
                    customer = None
                    for rental in self.rentals:
                        if rental.getCar() == carToReturn:
                            customer = rental.getCustomer()
                            break

                    if customer:
                        self.returnCar(carToReturn)
                        print("Car returned successfully by", customer.getName())
                    else:
                        print("Car was not rented or rental information is missing.")
                else:
                    print("Invalid car ID or car is not rented.")

            elif choice == '3':
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        print("\nThank you for using the Car Rental System!")


def main():
    rentalSystem = CarRentalSystem()

    car1 = Car("C001", "Toyota", "Camry", 60.0)
    car2 = Car("C002", "Honda", "Accord", 70.0)
    car3 = Car("C003", "Mahindra", "Thar", 150.0)
    rentalSystem.addCar(car1)
    rentalSystem.addCar(car2)
    rentalSystem.addCar(car3)

    rentalSystem.menu()


if __name__ == "__main__":
    main()
