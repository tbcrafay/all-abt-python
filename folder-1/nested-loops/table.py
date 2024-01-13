for i in range(2):
    for j in range(11):
        ans = i * j
        print(ans)
    print()

for i in range(1,10):
    print(i, "|", end = ' ')
    for j in range(1,10):
        print(format(i * j, "4d"), end=' ')
    print()    
