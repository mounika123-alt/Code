import math

# Step 1: Ask the user for input
number = int(input("Enter a number: "))

# Step 2: Perform calculations
square_root = math.sqrt(number)
log_natural = math.log(number)
sine_value = math.sin(number)  # number is in radians

# Step 3: Display results
print("\n--- Results ---")
print("Square Root of", number, "is:", square_root)
print("Natural Logarithm of", number, "is:", log_natural)
print("Sine of", number, "(in radians) is:", sine_value)