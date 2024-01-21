def linearSearch(lst, key):

    for i in range(len(lst)):
        if key == lst[i]:  # here key is the value to be search in the list, and lst[i] is indicating the index
            return i
    return -1

def main():
    lst = [1,2,3,4,3,5,10,9,8,7,20]

    i = linearSearch(lst, -4)
    j = linearSearch(lst, 4)
    k = linearSearch(lst, -3)
    l = linearSearch(lst, 3)

    print(lst)
    print(len(lst))

    print(i)
    print(j)
    print(k)
    print(l)

main()    

# Task : search for index of repeated elements in the list along with their number of occurence.