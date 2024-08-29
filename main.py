# nested if/else statements

print("Welcome the the roller coaster Fun Fare!")
age= int(input("What is your age in years? "))
height = int(input("What is your height in cm? "))

if age >= 7 and height >=120:
    print("You can ride the roller coaster")
    if 7 <=age <12:
        print("Please pay $5")
    elif 12 <=age <18:
        print("Please pay $7")
    else:
        print("Please pay $12")

else:
    print("Sorry you've to grow taller before you can ride.")
