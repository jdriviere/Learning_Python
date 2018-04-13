# Lesson 06 - Functions
# Functions are like methods in some programming languages, meaning a block
# of codes containing information about the function. They are defined by
# putting the word 'def' before a name.
#
# DEFINING A FUNCTION
# Defining a function takes the following form:
# def function_name (optional_parameter):
#   "Some text that describes the funtion" # Optional
#   function body
#   return (expression) # Optional
print ('Created print_str function...')

def print_str (str):
    "This function simply prints the string put within its parameter"
    print (str)
    return # Returns nothing

# CALLING A FUNCTION
# To call a function, you simply write its name, along with parameters, if it contains any
# in its definition
print_str ('This is a print_str function call!')
print_str ('This is another print_str function call!')

# PASS-BY-VALUE vs PASS-BY-REFERENCE
# By default, in Python, values are passed by reference, meaning that if the value you are
# referring to (a parameter's reference) is changed, it will also reflect in the calling function.
#
# In contrast, pass by value only affects variables contained locally within a function. This means
# that, once that variable is called outside of a function, it will revert back to its original value.
print ('\nPass-By-Reference Example:')
def change_list (list):
    print ('List before the change, INSIDE the function call:', list)
    print ('Changing item...')
    list[1] = 23 # Change through reference
    print ('List after the change, INSIDE the function call:', list)
    return # Returns nothing

my_list = [1, 4, 5, 10, 7]
change_list (my_list)
print ('Printing the list OUTSIDE of function call:', my_list)

print ('\nPass-By-Value Example:')
def change_list_again (list):
    print ('List before the change, INSIDE the function:', list)
    print ('Changing items...')
    list = [1, 2, 3, 4] # Change through values (?)
    print ('List after the change, INSIDE the function:', list)
    return # Returns nothing

my_list_again = [2, 3, 4, 10]
change_list_again (my_list_again)
print ('Printing the list OUTSIDE the function call:', my_list_again)

# ARGUMENT TYPES
# 1. Required Arguments: The most popular of them. They are simply the parameters
#                        you put inside the parentheses, which you put in order,
#                        when you define a function. When calling that function,
#                        the number of arguments you put should match that of the
#                        parameters of the function.
# def print_str (str):
#     print (str)
#     return
# print_str ('This is a simple function')

# 2. Keyword Arguments: During a function call, you put the arguments within the function's
#                       parentheses. When you have multiple parameters in a function, in a
#                       Keyword Arugment type of function call, the order of the parameters,
#                       through its arguments, does not matter.
# def print_str (str):
#     print (str)
#     return
# print_str (str = 'This is a simple function')
#
# def print_info (name, age):
#     print (name, 'is', age, 'years old!')
#     return
# print_info (age = 50, name = 'John')

# 3. Default Arguments: When creating a function, you can give default values to a function's
#                       parameters. When done so, if you call that function without that specific
#                       argument, the default argument will be given.
# def print_info (name = 'John', age = 40):
#     print (name, 'is', age, 'years old!')
#     return
# print_info () # Prints the default 'John is 40 years old!'
# print_info ('James', 45) # Prints 'James' is 45 years old!'
# print_info (age = 22) # Prints 'John is 22 years old!'
# print_info (name = 'Suzie') # Prints 'Suzie is 40 years old!'

# 4. Variable-Length Arguments: This type of argument is useful when you have
#                               to pass more arguments in a function than you
#                               initially intended to. They are NOT named in the
#                               function definition. The syntax is as followed:
# def function_name (formal_var, *var_args_tuple):
#     "Function documentation"
#     function body
#     return [expression]
# NOTE: The asterisk (*) is placed before the variable-length argument. As a tuple
#       (meaning, a list whose items cannot be changed), it remains empty if no
#       additional arguments were passed down to the function.
print ('\nVariable-Length Arguments:')

def print_num (num, *more_nums):
    print ('Output:')
    print (num)

    for extra in more_nums:
        print (extra)
    
    return # Returns nothing
print_num (10)
print_num (10, 20, 30, 50, 45)

# ANONYMOUS (LAMBDA) FUNCTIONS
# They are called like this because they are not invoked in the same manner as the regular
# functions. Instead of the word 'def' to declare a function, the word 'lambda' is used instead.
# Anonymous functions can only return ONE value in the form of an expression, though they can contain
# multiple arguments. Since they only return an expression, they cannot be directly called.
#
# Lambda functions have their own local namespace and cannot access variables other than those in
# their parameter list and those in the global namespace.
#
# The syntax of lambda functions contains only a single statement, which is as follows:
# value = lambda arg1, arg2, ..., argN : espression
# Example:
print ('\nLambda (Anonymous) Functions...')
sum = lambda num1, num2 : num1 + num2
# Then, you can use another method to get the results:
a = 10
b = 20
print ('If a is', a, 'and b is', b, 'then the sum is...', sum (a, b))

# RETURN STATEMENT
# The statement return [expression] exits a function, optionally passing back an expression to the caller.
# A return statement with no arguments is the same as return None.
# Example:
print ('\nReturn Statements:')

def sum (num1, num2):
    "Returns the sum of two numbers"
    total = num1 + num2
    print ('Returning', total, 'from function...')
    return total

print (sum (10, 20))

# OR

total = sum (10, 20)
print (total)


# VARIABLE SCOPES
# There are two types of scopes: local and global. Variables that are
# defined inside a function body have a local scope, and those defined
# outside have a global scope. This means that local variables can be
# accessed only inside the function in which they are declared, whereas
# global variables can be accessed throughout the program body by all
# functions. When you call a function, the variables declared inside it
# are brought into scope.
#
# Example:
print ('\nGlobal vs Local Variables:')

total = 0
print ('If global total is', total)

def sum (num1, num2):
    "This prints the total sum of 2 numbers"

    total = num1 + num2
    print ('Total, INSIDE function (local):', total)
    return total

sum (10, 20)
print ('Total, OUTSIDE function (global):', total)