# find prime numbers between 1 and 100 using nested loops, conditions.

# for i in range(1,100 + 1,1):
#     if i % 1 == 0 and i % i == 0:
#         print(i)
#     print()    

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

print("\n")
print(num ** 0.5)  # Print a newline after all primes are printed
