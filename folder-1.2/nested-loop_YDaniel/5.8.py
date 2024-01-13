'''
(Use the math.sqrt function) Write a program that prints the following table
using the sqrt function in the math module.
Number Square Root
0      0.0000
2      1.4142
...
18     5.2426
20     5.4721
'''

import math
print('Number   Square Root')
for Number in range(1,20+1,1):
    square_root = math.sqrt(Number)
    print(f'{Number}        {square_root}')







