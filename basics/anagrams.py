###################################################
# Anagrams
###################################################

# This program reads a word dictionary from a text file and uses that dictionary to find anagrams for words.
# An anagram is word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# For example, the word 'lives' is an anagram of 'elvis'

# The file containing English words can be downloaded from GitHub at https://github.com/dwyl/english-words

# Concepts Illustrated
# * variables
# * string operations
# * list data structure
# * control structures
# * for loop
# * text file I/O
# * dictionary data structure


# open function opens and reads a text file and stores the resulting data in a variable.
# This function takes two parameters:
# 1: the path to the file you wish to read and 
# 2: a flag denoting how you want to open the file.  In this case, 'r' indicates that we are opening the file as
#    read-only

words = open('words.txt', 'r')

# Now we need to read individual lines of the text file.  Each line contains a single word. 
# The result of the following statement is a list (an array) of individual words read from the text file
wordlist = words.readlines()
print(wordlist[0:10])

# You will notice that each word is followed by '\n' - a new line character.  
# In order to be able to find anagrams, we need to do two things - (1) remove the new line character from each word
# and (2) convert each word to lower case
# NOTE: The statement below uses a Python comprehension instead of a standard for loop.  
# If you are up to the challenge, can you rewrite this comprehension as a for loop?
wordclean = [word.strip().lower() for word in wordlist]

print(wordclean[:10])
# While this particular list only contains unique words, in real life we have to be concerned with duplicates.
# The easiest way to de-dupe a list in Python is to use a 'set'.  Sets are mathematical constructs that only 
# allow unique values.  Converting a list to a set will automatically remove all duplicates.
wordunique = set(wordclean)

# Now we need to convert our set back into a list
wordunique = list(wordclean)

# NOTE:  The same thing could be done in a single statement:
# wordunique = list(set(wordclean))
# Converting our list to a set and back to a list created an unsorted list.  
# We need to sort the list in lexiographic order
wordunique.sort()

# NOTE: Another way to sort a list is with sorted() function:
# sorted(wordunique)

print(wordunique[:10])

# Sorting a string is very similar to sorting a list.  Python takes individual characters
# that compose the original string and puts them in lexiographic order
print("The word 'lives' sorted in lexiographic order: ", sorted('lives'))
print("The word 'elvis' sorted in lexiographic order: ", sorted('elvis'))

# Let's compare two sorted strings.  If they match, Python will return True
# and we will know that they are anagrams of each other.
# Think back to boolean expressions:)
print("Matched sorted words: ", sorted('lives') == sorted('elvis'))

# These two do not match - Python will return False
print("Unmatched sorted words: " , sorted('alive') == sorted('dead'))

# Let's create a function that takes a string (in this case a signle word) as a parameter
# and returns a 'sorted' version of the word - all characters comprising the word in 
# lexiographic order
def signature(word):
    return ''.join(sorted(word))

# Let's test our function
signature('elvis')

# Now let's write a function that takes a word as a parameter,
# iterates through the entire list of words, and finds the first word
# that is an anagram of the one passed into the function.
def anagram(myword):
    print("Found the following anagrams for: ", myword)
    for word in wordunique:
        if(signature(word) == signature(myword)):
            print(word)
anagram('dictionary')

