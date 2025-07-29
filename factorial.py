# Task 1: Factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function with a sample input
sample_number=int(input("enter a number :"))

print("Factorial of", sample_number, "is:", factorial(sample_number))