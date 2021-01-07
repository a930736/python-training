# define cars variable which equals 100
cars = 100
# define how many seats insdie the car
space_in_a_car = 4.0
# define the number of drivers
drivers = 30
# define the number of passengers
passengers = 90
# define how many undriven cars 100 -30 = 70
cars_not_driven = cars - drivers
# define how many cars are driven 30
cars_driven =drivers
# define capacity
carpool_capacity = cars_driven * space_in_a_car
# define the rate of passengers and driven cars
average_passengers_per_car = passengers/ cars_driven
print("There are",cars,"cars available")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("we need to put about",average_passengers_per_car," in each cars.")
# 加分題  car_pool_capacity 沒有定義 所以出現錯誤
#採用4.0是為了計算出來會有小數，不然在除的時候是無條件捨去小數

