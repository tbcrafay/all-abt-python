'''(Find numbers divisible by 5 and 6) Write a program that displays, ten numbers
per line, all the numbers from 100 to 1,000 that are divisible by 5 and 6. The numbers are separated by exactly one space'''




count = 0  # Count numbers per line

for num in range(100, 1001):
    if num % 5 == 0 and num % 6 == 0:
        print(num, end=" ")  # Print number with a space
        count += 1

        if count % 10 == 0:  # Newline after every 10 numbers
            print()

count = 0  
for num in range(100, 1001):
    if num % 5 != 0 or num % 6 != 0:
        continue  # Skips to the next iteration if the condition is true
    print(num,end=' ')  # This line executes only if the condition is false
    count += 1

    if count % 10 == 0:
        print()