'''
(Conversion from miles to kilometers) Write a program that displays the following
table (note that 1 mile is 1.609 kilometers):
Miles Kilometers
1     1.609
2     3.218
...
9    15.481
10   16.090
'''
print('Miles   Kilometers')

for Miles in range(1,10+1,1):
    kilometers = Miles * 1.609
    print(f"{Miles:4} {kilometers:7}m")


