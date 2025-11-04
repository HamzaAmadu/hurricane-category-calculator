# Hurricane Category Calculator HmWk3.1

print("Hurricane Wind Speed Checker")

try:
    # Getting wind speed input from user
    wind_speed = int(input("Enter wind speed in mph please: "))

    # Checking for invalid input
    if wind_speed < 0:
        print("Error: Wind speed cannot be negative, please try again")

    # Classify wind speed
    elif wind_speed >= 157:
        print("Category 5: Catastrophic damage; high devastation")
    elif wind_speed >= 130:
        print("Category 4: Catastrophic damage will occur")
    elif wind_speed >= 111:
        print("Category 3: Devastating damage will occur")
    elif wind_speed >= 96:
        print("Category 2: Extremely dangerous winds will cause extensive damage")
    elif wind_speed >= 74:
        print("Category 1: Very dangerous winds will produce some damage")
    elif wind_speed >= 39:
        print("Tropical Storm: Strong winds, but not a hurricane")
    else:
        print("Not a tropical storm or hurricane")

except ValueError:
    print("Error: Please enter a valid integer number")
