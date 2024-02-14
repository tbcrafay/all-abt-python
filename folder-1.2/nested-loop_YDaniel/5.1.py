'''
(Count positive and negative numbers and compute the average of numbers)
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the total
and average of the input values (not counting zeros). Your program ends with the
input 0. Display the average as a floating-point number.
'''

positiveInteger = 0
negativeInteger = 0
total = 0
count = 0

while True:
    number = eval(input('Enter numbers (to stop press Zero "0")::'))
    if number == 0:
        break
    total += number
    count +=1

    if number > 0:
        positiveInteger += 1
    elif number < 0:
        negativeInteger += 1

if count > 0:
    average = total / count
    print("Positive numbers:", positiveInteger)
    print("Negative numbers:", negativeInteger)
    print('count: ',count)
    print("Total:", total)
    print("Average:", average)
else:
    print("No non-zero numbers were entered.")

'''
we entered some numbers such as: 1,2,3,4

total = total + 1 +2 +3 +4 = 10
count = 4

positive integers  = 4
negative int = 0

count > 0
average = 10 / 4


'''






