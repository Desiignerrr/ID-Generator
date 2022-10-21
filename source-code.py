# ID Generator

# Imports the random module
import random


# List of lowercase characters
lowercase_characters = [
'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'k',
'j', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y',
'z'
]

# List of uppercase characters
uppercase_characters = [
'A', 'B', 'C', 'D', 'E',
'F', 'G', 'H', 'I', 'K',
'J', 'L', 'M', 'N', 'O',
'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y',
'Z'
]

# List of numbers
numbers = [
'0', '1', '2', '3', '4',
'5', '6', '7', '8', '9'
]


# Stores length of lowercase characters in this variable
lowercaseLen = len(lowercase_characters) - 1

# Stores length of uppercase characters in this variable
uppercaseLen = len(uppercase_characters) - 1

# Stores length of number in this variable
numberLen = len(numbers) - 1


# Variable with random numbers based on length
# For each string
numLower = random.randint(0,lowercaseLen)

numUpper = random.randint(0,uppercaseLen)

numNumber = random.randint(0,numberLen)


numLower1 = random.randint(0,lowercaseLen)

numUpper1 = random.randint(0,uppercaseLen)

numNumber1 = random.randint(0,numberLen)


numLower2 = random.randint(0,lowercaseLen)

numUpper2 = random.randint(0,uppercaseLen)

numNumber2 = random.randint(0,numberLen)


numLower3 = random.randint(0,lowercaseLen)

numUpper3 = random.randint(0,uppercaseLen)

numNumber3 = random.randint(0,numberLen)


# Stores random based data in these variables
first = f'{lowercase_characters[numLower]+uppercase_characters[numUpper]+numbers[numNumber]}'

second = f'{lowercase_characters[numLower1]+uppercase_characters[numUpper1]+numbers[numNumber1]}'

third = f'{lowercase_characters[numLower2]+uppercase_characters[numUpper2]+numbers[numNumber2]}'

fourth = f'{lowercase_characters[numLower3]+uppercase_characters[numUpper3]+numbers[numNumber3]}'


# Combines all of them into one string
output = f'{first+second+third+fourth}'


# Prints the token in the terminal
print(f'Token key is : {output}')
