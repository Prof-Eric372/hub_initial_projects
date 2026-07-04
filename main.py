print("--- WELCOME TO MY HUB OF TERMINAL PROJECTS ")
print("*** First project: ***" )
print("----IMC Calculator----")

print("--- Hey! We need some infos, could you answer the questions below? --- ")
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilos: "))

print("---Very nice! Now I´ll calculate your IMC")
imc = (weight/ height ** 2)

if imc < 18.5:
    print(f"Your are underweight, your IMC is:  {imc:.2f}")
elif imc < 25:
    print(f"You are at the expected weight, your IMC is:  {imc:.2f} ")
elif imc < 30:
    print(f"You are overweight, your IMC is:  {imc:.2f} ")
else:
    print(f"You need to pay attention on your health cause you are obese, your IMC is:  {imc:.2f}")

print("*** Second project: ***")
print("--- Discounts calculator ---")
#Presentation
print("Welcome to our store! Today we’re offering special discounts on selected products. Let’s take a look together.")
print("If you want to buy a t_shirt, today we offer 15% off")
print("If you want to buy a shorts, today we offer 20% off")
print("If you want to buy a sneakers, today we offer 10% off")

#Variables
t_shirt= 60.00
shorts = 45.00
sneakers = 200.00

#Program

price_tshirt = t_shirt - (t_shirt * 0.15)
price_shorts = shorts - (shorts * 0.2)
price_sneakers = sneakers - (sneakers * 0.1)

selection = input("Pick your clothing item: ")
if selection == "Tshirt":
    print(f"The price of t-shirt is {price_tshirt:.2f}")
elif selection == "shorts":
    print(f"The price of shorts is {price_shorts:.2f}")
elif selection == "sneakers":
    print(f"The price of sneakers is {price_sneakers:.2f}")
else:
    print("Please enter a valid selection.")

print("*** Third project: ***")
print("---Temperature Converter---")
print("This project consists of a temperature converter where the user inputs a value in Celsius to be converted into Fahrenheit and Kelvin.")

temp = float(input("Please enter your temperature in Celsius: "))

#Fahrenheit
temp_f = 9/5 * temp + 32

#Kelvin
temp_k = temp + 273.15
print(f"The temperature in Fahrenheit is:  {temp_f:.2f}")
print(f"The temperature in Kelvin is:  {temp_k:.2f}")
