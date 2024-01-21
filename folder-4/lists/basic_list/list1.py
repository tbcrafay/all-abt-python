if __name__ == '__main__':
    N = int(input("enter the number of commands::"))  # Read the number of commands
    list1 = []  # Initialize an empty list

    for _ in range(N):
        command = input("read each command and split it into words:").split()  # Read each command and split it into words
        operation = command[0]

        if operation == "insert":
            i, e = int(command[1]), int(command[2])  # Extract index and element
            list1.insert(i, e)
        elif operation == "print":
            print(list1)
        elif operation == "remove":
            e = int(command[1])
            list1.remove(e)
        elif operation == "append":
            e = int(command[1])
            list1.append(e)
        elif operation == "sort":
            list1.sort()
            print(list1)
        elif operation == "pop":
            list1.pop()
        elif operation == "reverse":
            list1.reverse()
        