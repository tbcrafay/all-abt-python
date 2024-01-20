'''Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]'''

def friend(x):

    New_lists = []
    for i in x:
        if len(i) == 4:
            New_lists.append(i)
    return New_lists

if __name__=="__main__":
    x = ["Ryan", "Kieran", "Jason", "Yous"]
    print(friend(x))

# try another way
friends = ["Ryan", "Kieran", "Jason", "Yous"]

def friend_filter(x):
  """Filters a list of names, returning only those with 4 letters."""
  return [i for i in x if len(i) == 4]

filtered_friends = friend_filter(friends)

print(filtered_friends)

            