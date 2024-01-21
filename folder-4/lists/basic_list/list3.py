if __name__ == '__main__':
    # n = int(input())
    integer_list = map(int,input().split())
    t = tuple(integer_list)
    hash_value = hash(t)
    print(t)
    print(hash_value)

'''

Here's a breakdown of the problem, explanation of hash(), and solution:

Problem Statement:

Receive input:
An integer n representing the number of integers to follow.
n space-separated integers.
Create a tuple:
Store these n integers in a tuple named t.
Apply hash():
Calculate the hash value of the tuple t using the hash() function.
Print the result:
Display the computed hash value.
What is hash()?

It's a built-in Python function that takes an object as input and returns an integer hash value representing the object's contents.
It's often used for:
Efficiently storing and retrieving objects in data structures like dictionaries.
Comparing objects quickly (since checking hash values is faster than comparing entire contents).
Important points:
Hash values are not guaranteed to be unique, but collisions are rare.
Hash values can change between Python versions.

'''    