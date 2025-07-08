# At first I define a "def" with two variables and use "while"
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Get input for the first and second numbers.
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# output the result
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")