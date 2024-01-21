# reversing the lists, Using bubble sorting;

#  sorting to see the sorting at once
l=[9,-2,123,3,4,9]
for i in range (len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp 
            print(l)


#  sorting to see the process of sorting each by each

l=[9,-2,123,3,4,9]
for i in range (len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
        print(l)

#  sorting the names

l=["Zubair","Khalid","Adeel","Danish"]
for i in range (len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]<l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
        print(l)