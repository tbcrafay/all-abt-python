file1 = open("D:\\Pfund_assigments, notes and PDFs\practices\\all about python\\all-abt-python\\file-handling-in-python\\file1.txt","w")

lines_to_write = ["Line 1\n", "Line 2\n"]
file1.writelines(lines_to_write)

file1.close()
