'''(Find the factors of an integer) Write a program that reads an integer and displays
all its smallest factors, also known as prime factors. For example, if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5'''


# User_input = eval(input("enter any integer::"))

n = eval(input("Enter any integer::"))  # Change this to your desired number

divisor = 2
while n > 1:
  while n % divisor == 0:
    print(divisor, end=", ")
    n //= divisor
  divisor += 1

print("")  # Add a newline after the last factor




