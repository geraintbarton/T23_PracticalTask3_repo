# A program to demonstrate the use of functions to calculate the total price of a holiday from flight, hotel and car rental components

# A function to return the cost of the flight depending on which city the user has selected
def calculate_plane_cost(selected_city):
    return(list(cities.values())[selected_city-1])

# A function to caluclate the cost of car rental defaults to £50/day
def calculate_car_rental(num_days,daily_rental_price=50):
    return(num_days * daily_rental_price)

# A function to caluclate the cost of car rental defaults to £100/night
def calculate_hotel_cost(num_hotel_nights, daily_hotel_price=100):
    return(num_hotel_nights * daily_hotel_price)

# A function to calculate the total cost of a holiday
def calculate_holiday_cost(flight_cost, car_rental_cost, hotel_cost):
    return(flight_cost + car_rental_cost + hotel_cost)

# A function to calculate the discounted cost of the holiday
def calculate_discount(holiday_amount, discount):
    return(holiday_amount*(1-(discount/100)))

# dict to hold list of cities and associated flight costs
cities = {
    "Paris": 100,
    "Lisbon": 150,
    "New York": 375,
    "Sydney": 999,
}

# get the users city selection
# NOTE: I used a standard for loop as I wanted to output the index number as the option for the user to type in and didn't want to use a counter
# However I found out that you can't index a dictory directly - is that the case?
# Is there a more elegant way of doing this that loops through the dictionary but doesn't use a counter?
print("\nPlease select the city you would like to fly to from the list below by entering an option between 1 to 4:")
for x in range(0,len(cities)):
    print("{}) {} (£{})".format(x+1,list(cities)[x],list(cities.values())[x]))

city_selection = int(input(":"))

#Check the selection
if city_selection > 0 and city_selection <= 4:
    print("You selected: "+list(cities)[city_selection-1])
else:
    input("Sorry, I didn't get that, please enter a value between 1 and 4: ")

# Get the number of nights at the hotel
num_nights = int(input("Please enter the number of nights you are staying at the hotel: "))

# check it's a number:
if not num_nights.is_integer():
    input("Sorry, I didn't get that, please enter the number of nights you would like to stay at the hotel: ")

#Get the number of days of car rental
rental_days = int(input("Please enter the number of days you would like to rent a car for: "))

#Check the days is a number:
if not rental_days.is_integer():
    input("Sorry, I didn't get that, please enter the number of days you would like to rent the car for: ")

#calculate the total hotel costs. 
total_holiday_cost = calculate_holiday_cost(calculate_plane_cost(city_selection),calculate_car_rental(rental_days),calculate_hotel_cost(num_nights))

#get the discount % and calculated the discounted cost
discount = int(input("Enter the discount percentage: "))
discounted_price = calculate_discount(total_holiday_cost,discount)


print("The total cost of your holiday will be: £{:,.2f}".format(total_holiday_cost))

#print out the discounted costs
print("The discounted price is: £{:,.2f}".format(discounted_price))

