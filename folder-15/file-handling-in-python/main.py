file1 = open("D:\\All about SSUET\semester-1\\Pfund_assigments, notes and PDFs\\practices\\all about python\\all-abt-python\\folder-15\\file-handling-in-python\\file1.txt","w")

# lines_to_write = ["Line 1\n", "Line 2\n",'2\n']
# file1.writelines(lines_to_write)
file1.writelines("I love Programming Fundamentals!")
file1.close()

matter = open("D:\\All about SSUET\semester-1\\Pfund_assigments, notes and PDFs\\practices\\all about python\\all-abt-python\\folder-15\\file-handling-in-python\\matter.txt","w")

alphabets = [chr(i) for i in range(97, 123)]
for letter in alphabets:
    matter.write(letter)




matter.close()

def count_hash():
    file = open("D:\\All about SSUET\semester-1\\Pfund_assigments, notes and PDFs\\practices\\all about python\\all-abt-python\\folder-15\\file-handling-in-python\\matter.txt", "r")  # Open in read mode
    data = file.read()
    count = 0
    for letter in data:
        count +=1
        print(count, end=" #")
        
    file.close()

# count_hash()  

'''
mention error:

used w to access file instead of w+
use count variable and give it iteration, to count the hash.
print count for the hash for the letters in the file.

'''



# 2 
    
def count_letter():

    with open("D:\\All about SSUET\semester-1\\Pfund_assigments, notes and PDFs\\practices\\all about python\\all-abt-python\\folder-15\\file-handling-in-python\\file1.txt","r") as file:
        data = file.read()
    count = 0
    for letter in data:
        if letter.isupper():
            count +=1
            print(count,end=" ")

count_letter()  

'''mention error:

replace Close with open, in order to open the file and use "with open(filename) as file:;

file.append has been used instead of file.read

while loop has been used instead of for loop.

file.append() has been used instead of file.close()

letter() has been used to invoke instead of count_letter()

'''

    # return count

# if __name__=="__main__":
    # filename = "D:\\All about SSUET\semester-1\\Pfund_assigments, notes and PDFs\\practices\\all about python\\all-abt-python\\folder-15\\file-handling-in-python\\file1.txt"


    # count_letter = count_letter(filename)

    # print(count_letter)



# 3
    








