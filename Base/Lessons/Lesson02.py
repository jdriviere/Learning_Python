# Lesson 02 - Assignments and Variables
varA = 1 # Type number
varB = "Bob" # Type string
varC = 10.6 # Type float

print (varA)
print (varB)
print (varC)

# Strings - A series of characters, almost like an array
str = "Hello, world."

print (str) # Prints the entire string
print (str[0]) # Prints the string character at index 0
print (str[2:]) # Prints the string characters starting from index 2
print (str[3:7]) # Prints the string characters from index 3 to index 7 - also called substring
print (str * 2) # Prints the string 2 times
print (str + " How are you?") # Prints the entire string, then concatenates with another string

# Lists - Think of it like an array
listA = ['a', 'b', 'c']
listB = ['ab', 2, 'cd', 0.3]
listC = [] # Creates an empty list/array

print (listA) # Prints the entire listA
print (listB) # Prints the entire listB
print (listB[3]) # Prints 0.3
print (listA[0:1]) # Prints elements at index 0 all the way to index 1
print (listB[1:]) # Prints elements starting from index 1
print (listA * 2) # Prints listA elements 2 times
print (listA + listB) # Concatenates listA elements with listB elements

# Tuples - Like a list, but must be enclosed within parentheses, which the values cannot be changed
tupleA = ('a', 12, 2.03)
tupleB = ('b', 16, 10.9)
tupleC = () # Creates an empty tuple

print (tupleA)
print (tupleB)
print (tupleA[2])
print (tupleB[1:])
print (tupleA * 3)
print (tupleA + tupleB)

listA[1] = 1000 # Try changing a list item
# tupleA[1] = 16 # Try changing a tuple item

print (listA[1]) # Should change value
# print (tupleA[1]) # Shouldn't compile

# Dictionaries - Like a hash table and/or similar to JavaScript objects
dictA = {} # Creates an empty dictionary
dictA['one'] = 'Value for one'
dictA[2] = 'Value for 2'
dictB = { 'name': 'James', 'age': 32, 'job': 'Designer' }

print (dictA['one']) # Prints value for key's index of 'one'
print (dictA[2]) # Prints value for key's index of 2
print (dictB) # Prints keys and values
print (dictB.keys()) # Prints only keys
print (dictB.values()) # Prints only values