#there are 100 cars

cars = 100

#there are 4 seats open in a car when the driver is driving

space_in_a_car = 4.000

#there are 30 drivers

drivers = 30

#there are 90 passengers

passengers = 90

#cars_not_driven are the amount of cars remaining minus the amount of total
#drivers

cars_not_driven = cars - drivers

#cars_driven are equal to the amount of drivers

cars_driven = drivers

# carpool_capacity is equal to the amount of cars_driven multiplied by the amount
# of space in a car

carpool_capacity = cars_driven * space_in_a_car

# the average amount of passengers per car is equal to the division of passengers
# by the cars that are being driven

average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
