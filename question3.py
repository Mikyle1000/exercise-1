# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
C = float(input("Enter the temperature in Degrees Celcius: "))

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Fahrenheit = float((C * 9/5) + 32)

# TODO: Print the result rounded to two decimal places
rounding = round(Fahrenheit, 2)
print("The temperature in Fahrenheit is " + str(rounding) )