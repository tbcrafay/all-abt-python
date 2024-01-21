'''
Generates 100 lowercase letters randomly and assigns them to a list of characters,
named chars Counts the occurrences of each letter in the list. To do so, it creates a list named counts
that has 26 int values, each of which counts the occurrences of a letter
'''

import RandomCharacter
def main():
    chars=createlist()
    print("The lower letter case are:")
    displayList(chars)
    
    count=countLetters(chars)
    print("The occurence of each letters are:")
    displayCounts(chars)
    

def createlist():
    chars = []
    for i in range(100):
        chars.append(RandomCharacter.getRandomLowerCaseLetter())
    return chars

def displayList(chars):
    for i in range(len(chars)):
        if (i+1) % 20 == 0:
            print(chars[i])
    else:
        print(chars[i],end =" ")

def countLetters(chars):

    counts = 26 * [0]

    for i in range(len(chars)):
        counts[ord(chars[i]) - ord('a')] += 1 
    return counts

def displayCounts(counts):
    for i in range(len(counts)):
        if (i + 1) % 10 == 0:
            print(counts[i], chr(i + ord('a')))
        else:
            print(counts[i], chr(i + ord('a')),end=" ")           




main()


#  display the number of repeatetion of the same characters