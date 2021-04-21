# Hotel costs for different cities
# Cost is in Rands

def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):

    if "cape_town" == city:

        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800
# car rental cost
# in rands

def rental_car_cost(days):

    car_cost = 40 * days
    if days >= 7:
        car_cost = car_cost - 50

    elif days >= 3 and days <7:

        car_cost = car_cost - 20
    return car_cost

# trip cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + spending_money

city = input("city travelled to " )
hotel = int(input("days spent in hotel "))
spending = float(input("amount used for spending money "))

print(trip_cost(city, hotel,  spending))






