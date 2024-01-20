import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    if n % 2 != 0:  # Check for odd numbers
        print("Weird")
    else:
        if 2 <= n <= 5:  # Check for even numbers in the range 2-5
            print("Not Weird")
        elif 6 <= n <= 20:  # Check for even numbers in the range 6-20
            print("Weird")
        else:  # All remaining even numbers greater than 20
            print("Not Weird")
