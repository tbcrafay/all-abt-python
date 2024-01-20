try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError(a,"That is not a positive number!")
    else:
        print(a,"is a positivemnumber")
except ValueError as ve:
    print(ve)
        