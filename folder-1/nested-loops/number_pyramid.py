num_rows = 5 # Change this to adjust the number of rows

for i in range(1, num_rows + 1):
    # Calculate starting number for each row
    start_num = i *2  # Correct calculation for start_num
    for j in range(1, i + 1):  # Loop from 1 to i to include i elements in each row
        # Print the current number with a space
        print(start_num, end=" ")
        # Increment the number for the next iteration
        start_num += num_rows
    # Print a new line after each row
    print()
