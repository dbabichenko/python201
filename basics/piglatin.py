###################################################
# Pig Latin Translator
###################################################

# Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix.

# For example, "Wikipedia" would become "Ikipediaway" (the "W" is moved from the beginning and has "ay" appended to create a suffix).
# The objective is to conceal the words from others not familiar with the rules. The reference to Latin is a deliberate misnomer; Pig Latin is simply a form of argot or jargon unrelated to Latin, and the name is used for its English connotations as a strange and foreign-sounding language. It is most often used by young children as a fun way to confuse people unfamiliar with Pig Latin.

# https://github.com/rlvaugh/Impractical_Python_Projects/blob/master/Chapter_1/pig_Latin_practice.py

# Concepts Illustrated
# * Python variables
# * string operations
# * control structures
# * while loop
# * break statement

# This example is based on the implementation provided by Impractical Python Projects at https://github.com/rlvaugh/Impractical_Python_Projects

# Create a list of vowel characters
vowels_list = 'aeiouy'

# Create an infinite loop
while True:
    # Get user input
    word = input("Type a word and get its pig Latin translation: ")

    if word[0] in vowels_list:
        # If the first letter of the word is a vowel, add "way" to the end of the word
        pig_latin = word + 'way'
    else:
        # If the first letter of the word is a consonant, move the first letter to the end of the word
        # and add "ay" to the end of the word
        pig_latin = word[1:] + word[0] + 'ay'
    
    # Print the pig latin translation
    print(pig_latin)
    
    # Ask if the user wants to try again
    try_again = input("Try again? (Press Enter to stop)\n ")
    
    # If user enters "no", exit 
    if try_again.lower() == "no":
        break