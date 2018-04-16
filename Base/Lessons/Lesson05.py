# Lesson 05 - Loop Controls

# WHILE LOOPS
# It's conditions and structure is similar to most programming languages.
# It repeats whatever statement(s) is found within its body indefinitely
# until the condition becomes false.
# While loops take the following form:
# while (expression):
#   statement(s)


count = 0
print('While-Loop starts:')

while (count < 5): # Parentheses are NOT required, but makes it cleaner
    print('Count is:', count)
    count = count + 1
print('While-Loop ended!')

# NOTE: Similar to If-Statements, While-Loops can also be written without the
#       parentheses and on one-line
#       while count = 0 : print('Count is', count)
#       But for clean coding purposes, it is best to write as the example above

# While-Loops can also create infinite loops if the condition never becomes false.
# They are generally useful when creating applications that need to constantly run,
# such as servers.
# To force-end an infinite loop, just type CTRL + C on the terminal (CTRL + Z in Windows)
# Here's an example:


var1 = 1
print('\nInfinite While-Loops')

while var1 <= 3: # Creates an infinite loop if left at 1
    num = int(input('Enter a number: ')) # The int() function converts a string number into an integer number
    print('You entered', num)           # The input() function allows the user to input a string
    var1 += 1
print('While-Loop ended!')

# WHILE-ELSE LOOPS
# You can also use the 'else' keyword on a While-Loop


count = 0
print('\nWhile-Else Loops')

while (count < 5):
    print(count, 'is less than 5!')
    count += 1
else:
    print(count, 'is now 5 or more.')
print('While-Loop ended!')

# FOR LOOPS
# For-Loops allow to loop through items within a sequence/range (e.g.: lists, strings).
# A For-Loop takes the following form:
# for iterating_variable in sequence:
#   statement(s)
# Of course, for cleaner code, you can surround the declaration in parentheses.
# The 'iterating_variable' is the variable that stores the current information contained
# within the range, as it loops through its items. Furthermore, the range() function is
# one of the best ways to iterate over a sequence of numbers.
# 
# Ex: range(5) creates a result of range(0, 5) in the command line, meaning a variable will
# iterate from 0 and increment 5 times (meaning 0 to 4). A range ranges from 0 to (n - 1).


range(5)
print('\nRange of 5 created...')

# You can typecast a range into a list() to obtain a list object.
print('The items within the current range are:', list(range(5)))

print('Using the For-Loop to loop through the list:')
for var in (list(range(5))):
    print('Iteration #', var + 1, ': ', var)

# For-Loops can also be used to go through a string sequence (series of characters).
print('\nLooping (traversing) through a string...')
for letter in 'Python':
    print('Current letter:', letter)
print('End of For-Loop!')

# For-Loops can also be used to go through a list.
print('\nLooping (traversing) through a list...')
fruits = ['apple', 'banana', 'cherry', 'kiwi']

print('The list contains:')
for fruit in fruits:
    print('Current fruit:', fruit)
print('End of For-Loop!')

# You can do the same thing as the above using the items' index by combining
# the range() function, which iterates the count from 0 to (n - 1), and the
# len() funtion, which returns the total amount of items within a list or tuple, as
# followed: range(len(some_list))


print('\nTraversing fruit list using index...')
for index in range(len(fruits)):
    print('Fruit at index', index, ':', fruits[index])
print('End of For-Loop!')

# Like a While-Loop, you can also implement an 'else' statement in a For-Loop.
# The difference between the two loops (FOR...ELSE and WHILE...ELSE) is that,
# for the While-Loops, the 'else' statement kicks in when the condition becomes
# false; whereas in a For-Loop, the 'else' statement kicks in only when the loop
# terminates normally (and not through a 'break' command).


numbers = [1, 5, 7]
print('\nCreating a list...')
print('List contains the following items:', numbers)
print('List contains', len(numbers), 'items!')

for number in numbers:
    if number % 2 == 0:
        print('There is an even number in the list!')
        break
else:
    print('There are NO even numbers in the list!')

# NOTE: Notice that the 'else' statement is written OUTSIDE of the For-Loop!

# BREAK STATEMENT
# This command is similar to most programming languages.
# The 'break' command forces a loop to terminate.


print('\nTesting \'break\' command...')
str = 'Python'
seek = 'h'
print('Test string is:', str, '; Loop breaks at:', seek)

for letter in str:
    if letter == seek:
        break
    print('Current letter:', letter)

# CONTINUE STATEMENT
# This command is similar to most programming languages.
# The 'continue' command makes the loop skip the remainder of its body
# and restart the loop at the next iteration.


print('\nTesting \'continue\' command...')
print('Test string is:', str, '; Loop skips at:', seek)
for letter in str:
    if letter == seek:
        continue
    print('Current letter:', letter)

# PASS STATEMENT
# "It is used when a statement is required syntactically but you do not
# want any command or code to execute.
#
# The pass statement is a null operation; nothing happens when it executes.
# The pass statement is also useful in places where your code will eventually
# go, but has not been written yet" (TutorialsPoint.com)


print('\nTesting \'pass\' command...')
print('Test string is:', str, '; Loop passes through:', seek)
for letter in str:
    if letter == seek:
        pass
        print('Just went through a pass block. Didn\'t execute anything.')
    print('Current letter:', letter)