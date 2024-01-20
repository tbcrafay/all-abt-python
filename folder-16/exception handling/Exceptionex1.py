a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[0]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[1]))
    print ("Fourth element = %d" %(a[2]))
    print ("Fourth element = %d" %(a[2]))
except:
    print ("An error occurred")
else:
    print("In else block")
finally:
    print("In finally block")
    
print("Program terminates")