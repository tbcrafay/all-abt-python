'''(Find the smallest n such that n2 12,000) Use a while loop to find the smallest
integer n such that n2 is greater than 12,000'''


n = 1  # Start with n = 1

while n**2 <= 12000:  # Loop until n^2 is greater than 12,000
    n += 1  # Increment n by 1

print(f"The smallest n such that n^2 > 12,000 is: {n}")
