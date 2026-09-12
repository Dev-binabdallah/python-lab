from utils import square, is_even, celsius_to_fahrenheit, greet

#enter name
name = input("Enter your name: ")
print(greet(name))

number = float(input("Enter a number: "))

print(f"Square: {square(number)}")

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")

print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(number)}")
