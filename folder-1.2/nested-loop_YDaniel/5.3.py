'''
(Conversion from kilograms to pounds)
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms Pounds
1          2.2
3          6.6
...
197       433.4
199       437.8 
'''
# for kilogram in range(1,200,1):
#     pounds = kilogram * 2.2
#     print('kilogram',kilogram,'pounds',pounds)

print("Kilograms  Pounds")  # Print headings

for kilograms in range(1, 200, 2):  # Loop from 1 to 199 in steps of 2
    pounds = kilograms * 2.2  # Calculate pounds
    print(f"{kilograms:4}   {pounds:7.1f}")  # Print formatted output


