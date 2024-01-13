'''(Find the largest n such that n3 12,000) Use a while loop to find the largest
integer n such that n3 is less than 12,000'''

n = 100  # Start with a reasonable guess for n

while n**3 >= 12000:  # Loop until n^3 is less than 12,000
    n -= 1  # Decrement n by 1

print(f"The largest n such that n^3 < 12,000 is: {n}")
   