# Lesson 09 - Assertions and Exceptions
# As in many programming languages, errors can occur. Python provides
# a way to catch some of these errors by catching them and debug them
# if possible.
# NOTE: Be familiar with some of the most common Exceptions found in
#       tutorialspoint.com/python3/python_exceptions.htm
# There are two types of debugging methods: Exceptions and Assertions.

# ASSERTIONS
# An assertion is a sanity-check that you can turn on or turn off when
# you are done with your testing of the program (TutorialsPoint.com).
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out by the assert statement:
#
# assert expression , arg1, ..., argN
#
# When it encounters an assert statement, Python evaluates the accompanying
# expression, which is hopefully true. If the expression is false, Python
# raises an AssertionError exception.


def kelvin_to_fahrenheit(temp):
    """A function that converts Kelvin temperature into Fahrenheit."""
    assert (temp >= 0), 'A temperature colder than zero cannot exist!'  # 'Assume this, or the other one is true'
    return int((temp - 273) * 1.8) + 32


print('Testing assertion...')
a = 480
b = 273
c = 0
print('If your temperature is', a, '...')
print('Your current Fahrenheit temperature is {0} if your Kelvin temperature is {1}'.format(kelvin_to_fahrenheit(a), a))
print('If your temperature is', b, '...')
print('Your current Fahrenheit temperature is {0} if your Kelvin temperature is {1}'.format(kelvin_to_fahrenheit(b), b))
print('If your temperature is', c, '...')
print('Your current Fahrenheit temperature is {0} if your Kelvin temperature is {1}'.format(kelvin_to_fahrenheit(c), c))


# EXCEPTIONS
# An exception is an event, which occurs during the execution of a
# program that disrupts the normal flow of the program's instructions.
# In general, when a Python script encounters a situation that it cannot
# cope with, it raises an exception. An exception is a Python object
# that represents an error.
#
# When a Python script raises an exception, it must either handle the
# exception immediately otherwise it terminates and quits.
#
# TRY... EXCEPT... ELSE BLOCKS
# This is the most basic form of exceptions. 'try:' means that the code
# will try to execute whatever is written within its block.
# 'except name_of_exception_error:' will try to execute whatever code is
# written in order to raise the error and/or handle it. And finally, the
# 'else:' block will execute no matter what, after the 'try:' block
# have been executed without errors.
#
# The basic syntax for a 'try...catch...else' block is as followed:
# try:
#     # Body of code
# except exception_error_name:
#     # Body of code
# else:
#     # body of code
# NOTE: You can raise multiple exceptions at the same time or separately.
def divide_it(num1, num2):
    """A simple division function."""
    try:
        total = num1 / num2
    except ZeroDivisionError:
        print('ERROR: You cannot divide by 0!')
    else:
        print('Dividing {0} by {1} is: {2}'.format(num1, num2, total))


print('\nTesting exceptions...')
var1 = 6
var2 = 4
print('If var1 is {0} and var2 is {1}...'.format(var1, var2))
divide_it(var1, var2)
print()
var3 = 3
var4 = 0
print('If var3 is {0} and var4 is {1}...'.format(var3, var4))
divide_it(var3, var4)

# TRY... FINALLY BLOCK
# You can use a finally: block along with a try: block. The 'finally:'
# block is a place to put any code that must execute, whether the try-block
# raised an exception or not.
#
# The syntax of the 'try...finally' statement is this:
# try:
#     # Block of code
# finally:
#     # Block of code
# NOTE: You can provide except clause(s), OR a finally clause, but NOT BOTH!
#       You cannot use else clause as well along with a finally clause!
print('\nTry-Finally test...')
try:
    print('I come from the TRY-Block!')
finally:
    print('I come from the FINALLY-Block!')

# You can read more about the list of exceptions on TutorialsPoint.com, as well
# as how to raise and customize exceptions.
