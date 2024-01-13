'''(Display the ASCII character table) Write a program that displays the characters
in the ASCII character table from ! to ~. Display ten characters per line. The characters are separated by exactly one space.'''


start_char = ord('!')  # ASCII code for '!'
end_char = ord('~')    # ASCII code for '~'

count = 0  # Count characters per line

for char in range(start_char, end_char + 1):
    print(chr(char), end=" ")  # Print character with space
    count += 1

    if count % 10 == 0:  # Newline after every 10 characters
        print()
