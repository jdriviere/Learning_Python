# Lesson 07 - Modules
# A module is a file consisting of Python code. A module can define functions,
# classes, and variables. A module can also include runnable code (TutorialsPoint).

# IMPORT STATEMENT
# You can use any Python source file as a module by executing an import statement
# in some other Python source file. The import statement by itself will bring into
# the current file ALL classes, functions, and variables from the imported file.
#
# The import has the following syntax:
# import module1[, module2, ..., moduleN]
#
# And they are used like the following:
# # module1.imported_function() | module1.imported_variable
print('Import Statement:')
import import_test # You DON'T need to put the '.py' extension

# Now, call the module, and then its function/variable
import_test.print_str('I was imported from another file!')
import_test.print_name('Sally')
print('Printing a random value from import:', import_test.random_value)

# NOTE: A module is loaded only once, regardless of the number
#       of times it is imported. This prevents the module execution
#       from happening repeatedly, if multiple imports occur.

# FROM...IMPORT STATEMENT
# Python's from statement lets you import specific attributes
# from a module into the current namespace. The from...import
# has the following syntax:
# from module_name import attribute_name1[, attribute_name2, ..., attribut_nameN]
print('\nFrom...Import Statement:')
from tests.import_test import add
add(10, 30) # No need to write the module name before the function/variable

# FROM...IMPORT * STATEMENT
# It is also possible to import all the names from a module into
# the current namespace by using the following import statement:
# from module_name import *
#
# NOTE: Though it may sound very advantageous (write once and for all), it is
#       recommended to use it very sparingly.

# PACKAGES IMPORT
# Read more about the '__init__.py' modules.