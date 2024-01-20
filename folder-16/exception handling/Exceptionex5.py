# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    try:
        raise ZeroDivisionError #
    except:
        print ("IN except block1")
except:
    print ("IN except block2")