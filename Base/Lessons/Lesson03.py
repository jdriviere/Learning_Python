# Lesson 03 - Operations and Arithmetics
a = 3
b = 2

# ARITHMETIC OPERATORS
# These operators are the same through most programming languages
# Performs basic arithmetic operations and yields a value
print('If a = 3 and b = 2...')
print('a + b: ', a + b) # Addition: adds a + b
print('a - b: ', a - b) # Subtraction: subtracts a - b
print('a * b: ', a * b) # Multiplication: multiplies a * b
print('a / b: ', a / b) # Division: divides a / b
print('a % b: ', a % b) # Modulus: returns remainder after dividing a / b
print('a // b: ', a // b) # Floor Division: divides a // b, then rounds to LOWEST number
print('a ** b: ', a ** b) # Exponentation: performs a to the b power

# COMPARISON OPERATORS (returns True/False)
# These operators are the same through most programming languages
# Checks if both elements are similar on both sides of the operator
print('\nIs a == b: ', a == b) # Is a equal to b
print('Is a != b: ', a != b) # Is a NOT equal to b
print('Is a <= b: ', a <= b) # Is a less than or equal to b
print('Is a >= b: ', a >= b) # Is a greater than or equal to b
print('Is a < b: ', a < b) # Is a less than b
print('Is a > b: ', a > b) # Is a greater than b

# ASSIGNMENT OPERATORS
# These operators are the same through most programming languages
# Performs an operation on the left operand after setting it
c = 0
c = a + b
print('\nIf c = a + b...')
print('c: ', c)

# NOTE: Value of c will NOT reset back to a + b, but take on its NEW value after each operation
c += a
print('c += a: ', c, '(similar to c = c + a)')
c -= a
print('c -= a: ', c, '(similar to c = c - a)')
c *= a
print('c *= a: ', c, '(similar to c = c * a)')
c /= a
print('c /= a: ', c, '(similar to c = c / a)')
c %= a
print('c %= a: ', c, '(similar to c = c % a)')
c **= a
print('c **= a: ', c, '(similar to c = c ** a)')
c //= a
print('c //= a: ', c, '(similar to c = c // a)')

# LOGICAL OPERATORS
# The 'and' operator is similar to '&&' in some programming languages
# The 'or' operator is similar to '||' in some programming languages
# The 'not(expression)' operator is similar to '!(expression)' in some programming languages
x = 2
y = 3

print('\nIf x = 2 and y = 3...')

print('Is x = 2 AND y = 3? ', (x == 2 and y == 3)) # If BOTH are TRUE
print('Is x = 2 OR y = 3? ', (x == 2 or y == 3)) # If EITHER is TRUE
print('Is x != 2 AND y != 3?', not (x == 2 and y == 3)) # REVERSE of what's expected

# MEMBERSHIP OPERATORS (IN, NOT IN)
# 'in' looks for a specified element that exists in list or tuple
# 'not in' looks for a specified element that does NOT exist in list or tuple
v = 5 # Element to look for
w = 6 # Element to look for
list = [1, 2, 3, 4, 6] # List in which element will be compared to

print('\nIf v = 5 and list consists of [1, 2, 3, 4, 6]...')
if (v in list):
    print('v was found in list!')
else:
    print('v was NOT found in list!')

print('If w = 6 and list consists of [1, 2, 3, 4, 6]...')
if (w in list):
    print('w was found in list!')
else:
    print('w was NOT found in list!')

# This is the 'not in' operator, which is the contrary of 'in'
print('If v = 5 and w = 6, and list contains 1, 2, 3, 4, and 6...')
if (v not in list):
    print('v was NOT found in list!')
else:
    print('v was found in list!')

if (w not in list):
    print('w was NOT found in list!')
else:
    print('w was found in list!')

# IDENTITY OPERATORS (IS, IS NOT)
# They compare the MEMORY LOCATION (identity) of the values compared on both sides of the operator
# You can use Python's id(variable) function to look at the memory location of a variable
d = 20
e = 20
f = 25

print('\nIf d = 20, e = 20, and f = 25...')
print('d location/identity: ', id(d))
print('e location/identity: ', id(e))
print('f location/identity: ', id(f))

if (d is e):
    print('d and e have the same identity!')
else:
    print('d and e do NOT have the same identity!')

if (d is f):
    print('d and f have the same identity!')
else:
    print('d and f do NOT have the same identity!')

if (e is f):
    print('e and f have the same identity!')
else:
    print('e and f do NOT have the same identity!')