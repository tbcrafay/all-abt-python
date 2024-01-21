if __name__ == '__main__':
    N = int(input())  # Number of commands
    list1 = []  # Empty list

    for _ in range(N):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            i, e = int(command[1]), command[2]  # Index as int, element as string
            list1.insert(i, e)
        elif operation == "print":
            print(list1)
        elif operation == "remove":
            e = int(command[1])  # Assuming elements to remove are still integers
            list1.remove(e)
        elif operation == "append":
            e = command[1]  # Element as string
            list1.append(e)
        elif operation == "sort":
            list1.sort()
            
        elif operation == "pop":
            list1.pop()
        elif operation == "reverse":
            list1.reverse()    
        
