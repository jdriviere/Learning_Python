# Lesson 08 - Classes and Objects
# Classes are prototypes that contain attributes that characterize an object.
# The attributes are called data members, which can be instance variables
# or class variables, and methods (functions).
#
# CREATING A CLASS
# Classes are created as followed:
# class ClassName: # For easy reference, it's better to capitalize the class names
#     'Optional class documentation' # You can read the documentation of a class
#                                    # with the method call: ClassName.__doc__
#     class_suite # This is just to say 'body of class goes here'
class Employee:
    'This class only creates an Employee object'
    employee_count = 0

    # Constructor:
    # Creates an instance (copy) and initializes the values of an object.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1 # Fetches the global variable within the function
        print('New employee', self.name, 'was created!')
    
    # Destructor:
    # Destroys (removes) an object's memory upon the object's deletion to avoid garbage
    # memory accumulation (a process called garbage collection).
    def __del__(self):
        Employee.employee_count -= 1
        print(self.name, 'was removed!')

    def display_count(self):
        print("Current number of Employees: %d" % Employee.employee_count)
        # The above string is the same thing as print('Current number of Employees:', Employee.employee_count)

    def display_employee(self):
        print('Name:', self.name, '\tSalary:', self.salary)

# NOTE: The function __init__() is called the constructor. It allows to instantiate
#       a class object with initial values.
# NOTE: ALL CLASS methods have 'self' as their first mandatory parameter! Python creates it
#       for you by default; and you don't need to include it in your function call.
# NOTE: Ideally, for best coding practice, it is recommended to write your classes in
#       a separate file, and import the needed methods through the 'import' command.

# CREATING INSTANCES
# After you create a class, you can instantiate (create/initialize) an object with the
# following line:
# var = ClassName ([parameter]) # Notice that there is no 'new' keyword like other languages
emp1 = Employee('John Smith', 20000) # Creates a first instance (copy) of Employee
emp2 = Employee('Sara Connor', 25000) # Creates a second instance of Employee

# ACCESSING THE METHODS
# To access the methods/functions of a class, you simply call it through the dot-notation,
# as followed:
# var_name.class_name_method([parameter])
print('\nDisplaying the object instances before deletion...')
emp1.display_employee()
emp2.display_employee()
print('Current number of employees:', Employee.employee_count)

print('\nDisplaying the object instances after deletion...')
del emp1
del emp2
print('Current number of employees:', Employee.employee_count)

# print('\nSome Special Class Methods:')
# print("Employee.__doc__:", Employee.__doc__) # Prints the documentation of the class
# print("Employee.__name__:", Employee.__name__) # Prints the name of the class
# print("Employee.__module__:", Employee.__module__) # Prints the module name of the class (usually __main__)
# print("Employee.__bases__:", Employee.__bases__) # ???
# print("Employee.__dict__:", Employee.__dict__ ) # Prints a dictionary containing the class' namespace

# CLASS INHERITANCE
# In most programming languages, there are classes (Children Class) who can inherit attributes
# of other classes (Parent Class), a process known as class inheritance. Children class can
# also override data members and methods of their parent class.
#
# The following lines represents the syntaxes of class inheritance:
# class Child_Class (Parent_Class1[, Parent_Class2, ..., Parent_ClassN]):
#     'Documentation of the Class'
#     # Body of Class
class Parent_Class:
    'This is the documentation for the Parent Class.'

    parent_attr = 0

    def __init__(self):
        print('Parent Class created!')
    
    def parentMethod (self):
        print('Calling a Parent Method!')
    
    def set_parentAttr (self, attr):
        Parent_Class.parent_attr = attr
        print('Parent Attribute set to:', attr)

    def get_parentAttr(self):
        print('Parent Attribute:', Parent_Class.parent_attr)


class Child_Class(Parent_Class):
    'This is the documentation for the Child Class.'

    def __init__(self):
        print('Child Class created!')

    def childMethod(self):
        print('Calling a Child Method!')

print('\nTesting Class Inheritance...')
child = Child_Class() # Creating an instance of a Child object
child.childMethod() # Child object calling Child Class method
child.parentMethod() # Child object calling Parent Class method
child.get_parentAttr() # Child object calling and getting Parent Class attribute
child.set_parentAttr(20) # Child object calling and setting Parent Class attribute


# METHOD OVERRIDES
# Overriding a method allows a Child Class to use the same method as its Parent Class,
# but not necessarily produce the same result or have the same functionality.
class Parent_C:
    'A simple Parent Class'
    def __init__(self):
        print('Parent Class created!')
    
    def myMethod(self):
        print('Parent method called!')

class Child_C(Parent_C):
    'A simple Child Class'
    def __init__(self):
        print('Child Class created!')
    
    def myMethod(self):
        print('Child method called!')

# NOTE: Since both parent and child have the same method (myMethod()), the
#       Child Class object will call on its version of myMethod().
print('\nMore Class Inheritance...')
child2 = Child_C()
child2.myMethod()

# DATA HIDING
# Data Hiding is the equivalent of 'private' data members in other programming languages.
# They are easily recognizable from 'public' data members in that they have a double-underscore
# before its name: __var_name.
class Some_Class:
    'Some random documentation'
    
    __varA = 10 # Private variable can only be accessed within this class only

    def __init__(self):
        print('Random object created!')
    
    def some_method(self):
        print('Random method was called!')
    
    def get_var(self):
        print('Current random value:', self.__varA)
    
    def set_var(self, var):
        self.__varA = var
        print('Random value was set to', self.__varA)

print('\nTesting Data Hiding...')
some_var = Some_Class()
some_var.some_method() # Can call method
some_var.get_var() # Can call method
some_var.set_var(20) # Can call method
# some_var.__varA # Can't access private member directly
print('Private random value is:', some_var._Some_Class__varA) # Can access the private member directly now