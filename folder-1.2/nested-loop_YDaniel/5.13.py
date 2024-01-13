'''(Find numbers divisible by 5 or 6, but not both) Write a program that displays, ten
numbers per line, all the numbers from 100 to 200 that are divisible by 5 or 6, but
not both. The numbers are separated by exactly one space.'''


count = 0

for num in range(100,200+1):
    
    if num % 5 == 0 and num % 6 == 0:
        continue
    elif num % 5 == 0 or num % 6 == 0:
        print(num,end=' ')
        count +=1
    if count % 10 == 0:
        print()                