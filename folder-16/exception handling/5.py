def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        raise ValueError("can't divide by zero")
    return x / y
while True:
    try:
        num1 = eval(input("Enter no 1:"))
        op=input("Enter operator (+,-,*,/):")
        num2 = eval(input("Enter no 2:"))
        
        if op == '+':
            result=add(num1,num2)
        elif op == '-':
            result=sub(num1,num2)
        elif op == '*':
            result=mul(num1,num2)
        elif op == '/':
            result=div(num1,num2)
        else:
            raise ValueError("Invalid Operator")
        print(f"Result:{num1} {op} {num2} = {result}")
    
    except ValueError as e:
        print(f" Error:{e}. enter valid no and values")
    except ZeroDivisionError as e:
        print(f" Error:{e}.enter non zero digit")
    except Exception as e :
        print(f"an unexpected error occured:{e} ")
    ano_cal=input("Do you want to run program again(yes/no)")
    if ano_cal!= "yes":
        break    