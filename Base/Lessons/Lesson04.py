# Lesson 04 - Decision Making (Conditions)
age = 25
print('If your current age is', age, '...')

# IF- STATEMENTS
# In condition statements, in Python, instead of the curly braces ({}),
# you put a colon (:) after the statement, before the body of the condition
if (age >= 18):
    print('Yay! You made it to at least 18 years old!')
# Can also be written without the parentheses...
# if age >= 18:
#     print('You are old enough to drink.')
#
# or in one line...
# if (age >= 18) : print('You are old enough to drink.')
#
# or a combination of both...
# if age >= 18 : print('You are old enough to drink.')
#
# Unless you have multiple lines of code within the body of the condition,
# similarly to some programming languages. But it is best to write it like
# the first option for cleaner code.

# IF-ELSE STATEMENTS
if (age >= 18):
    print('You are allowed to drink.')
else:
    print('You are NOT allowed to drink.')

# IF-ELIF-ELSE STATEMENTS
# Unlike some programming languages, where secondary conditions are
# labeled as 'else if', in Python (and some other languages), it's
# labeled as 'elif' instead
if (age >= 21):
    print('You are a legal adult.')
elif (age >= 18 and age < 21):
    print('You are NOT a legal adult.')
else:
    print('You are still a minor.')

# NESTED CONDITIONS
# Similar to most programming languages, condition statements can be nested
if (age >= 18):
    if (age >= 21):
        print('You are old enough to drink AND you are a legal adult!')
    else:
        print('You are old enough to drink but you are NOT a legal adult!')
else:
    print('You are NOT old enough to drink and you are NOT a legal adult!')