'''Sum of integers between two numbers:- '''

def sum(i,j):
    result = 0
    for num in range(i,j+1):
        result += num
    # print(result)
    return result
# Output :

'''
Enter an integer::1
Enter an integer::10
55
here is the sum= None

'''




i = eval(input("Enter an integer::"))
j = eval(input("Enter an integer::"))
sum = sum(i,j)
print('here is the sum=',sum)

def sum(i,j):
    result = 0
    for num in range(i,j+1):
        result += num
    print(result)
    # return result

i = eval(input("Enter an integer::"))
j = eval(input("Enter an integer::"))
sum = sum(i,j)
print('here is the sum=',sum)


# Output :

'''
Enter an integer::1
Enter an integer::11
here is the sum= 66

'''


'''Key points:

Use return to provide a function's output as a usable value.
Use print only for displaying information, not for returning values.'''