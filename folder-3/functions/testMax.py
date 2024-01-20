def max(num1,num2):
    if num1 > num2:
        result = num1
    elif num1 == num2:
        result = "Numbers are equal"    
    else:
        result = num2    
    return result

def main():
    print(max(2,4))
main()           