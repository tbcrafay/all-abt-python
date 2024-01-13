for i in range(1, 7):
    for j in range(1, i+1 ):
        print('*', end=" ")
    print()   
#     Move to the next line after each row
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()  
    i += 1  
