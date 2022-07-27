###################################################
# Palindromes
###################################################

# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. (https://en.wikipedia.org/wiki/Palindrome). This program accepts a single word without spaces or punctuation characters as user input and checks if that word is a valid palindrome

# Get user input
user_input = input("Please enter a single word with no spaces or punctuation characters:")
		
# In order to determine whether a word is a palindrome or not, we need to read it in reverse order,
# starting with the last character.  The position of the last character is the length of the word minus 1
# because Python counts starting from zero.
		
# The line of code below identifies the position, or the index, of the last character in the word
start = len(user_input) - 1
# Since we are counting from end to start (reversing the word), the last character to check
# will be the first character of the original word.  Since Java counts starting at zero,
# the position (index) of the first character in the original word is zero (0)
# However, because we will be iterating through the original word in reverse order using
# Python's for loop with range() function, we have to keep in mind that range() includes
# the first argument (the starting argument), but does not include the ending argument.
# In other words, range(0, 5) will give you numbers from 0 to 4.  If we want the range
# to start at some number and end at 0, we have to actually end it at -1

end = -1;
# Convert user input to lower case
user_input = user_input.lower()
# Store reversed string in a new variable
reversedText = "";
				
# Loop (iterate) through the word character-by-character starting from the end
# and stopping at the beginning.
for i in range(start, end, -1):
	# Find a character in position of i
	currentCharacter = user_input[i]

	# Append character to reversed string
	reversedText = reversedText + currentCharacter
# Check if entered word is indeed a palindrome:
if user_input == reversedText:
	print(user_input + " is a palindrome")
else:
	print(user_input + " is NOT a palindrome")