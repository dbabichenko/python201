###################################################
# Caesar Cipher
###################################################
# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence. (https://en.wikipedia.org/wiki/Caesar_cipher)

# For example, if you wanted to shift 'A' by three spaces, the algorithm will be as follows: (1) Convert 'A' to its ASCII value (65). (2) Add 3 to 65, to get 68. (3) Convert the ordinal 68 back to a letter ('D')

# Concepts Illustrated
# * variables
# * string operations
# * list data structure
# * control structures
# * for loop


# Get plaintext - the text that you would like to encrypt
plaintext = input('Enter plain text message: ')

print("Plaintext: " + plaintext)

# Get the shift number - by how many characters would you like to shift the cipher
shift_text = input('By how many characters would you like to shift the cipher?')
print("Shift cipher by: " + shift_text)

# Values entered through user input are stored as strings (String data type).  We need to
# convert shift value from string to int
shift_value = int(shift_text)

# Declare and initialize the variable that will store the encrypted text
cipher = ''

# Basic error handling.
# Since English alphabet contains 26 letters - you cannot shift your cipher by more than 26
if shift_value < 1 or shift_value > 26:
    print("English alphabet contains 26 letters - you cannot shift your cipher by more than 26")
else:
    # Iterate (loop) through each letter of user-entered plaintext
    for letter in plaintext:
        # Shift each letter by specified shift value.
        # Note that the ord() function returns the ASCII value of a character
        c = (ord(letter) + shift_value) % 126

        # 32 is the ASCII code for space, the lowest ASCII code that represents a
        # character that may be used in text.
        if c < 32:
            c += 31

        # Append shifted letter to the encrypted result
        cipher += chr(c)

    # Print result
    print('Your encrypted message is: ' + cipher)