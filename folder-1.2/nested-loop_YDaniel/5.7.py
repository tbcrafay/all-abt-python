'''
(Use trigonometric functions) Print the following table to display the sin value
and cos value of degrees from 0 to 360 with increments of 10 degrees. Round the
value to keep four digits after the decimal point.
Degree Sin    Cos
0     0.0000  1.0000
10    0.1736  0.9848
...
350  -0.1736  0.9848
360   0.0000  1.0000
'''
import math

# Define the range of degrees and increment
degrees_range = range(0, 361, 10)

# Print table header
print("Degree Sin    Cos")

# Loop through degrees and calculate sin and cos values
for degree in degrees_range:
    # Convert degree to radians for trigonometric functions
    radians = math.radians(degree)

    # Calculate sin and cos values with four decimal places
    sin_value = round(math.sin(radians), 4)
    cos_value = round(math.cos(radians), 4)

    # Print formatted output
    print(f"{degree:4d}  {sin_value:8.4f}  {cos_value:8.4f}")

    





