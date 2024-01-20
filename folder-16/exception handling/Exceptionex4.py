# Python program to demonstrate finally
 
# No exception Exception raised in try block

try:
    a=eval(input("enter a value"))
    b=eval(input("enter a value"))
    k = a//b # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
except:
     print("Other Exception")
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
    
print("Outside finally block")