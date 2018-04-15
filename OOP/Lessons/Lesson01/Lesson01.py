"""
Lesson 1 - Python Classes

-- 1-1 CREATING AND ACCESSING CLASSES AND THEIR ATTRIBUTES --
Python classes are easy to create. It takes the following form:

    class ClassName:
        pass # This indicates to the compiler it won't do anything

Then, once created, a class can be accessed through the following
statement:

    var = ClassName()

NOTE: You can access the class memory location by simply printing
      its object:

      print (var) # Prints <__main__.ClassName object at 0xSomeRandomNum
"""


class ClassName:
    """Empty class."""
    pass


var1 = ClassName()
var2 = ClassName()

print(var1)
print(var2)

"""
-- 1-2 ADDING ATTRIBUTES --
In Python, unlike some other programming languages, it seems you can
create attributes on the fly:

class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 6
p2.y = 3

print (p1.x, p1.y) # Should print 5 4
print (p2.x, p2.y) # Should print 6 3

As you can tell, the syntax to access a class' attribute(s) is the following:

    object.attributeName = value
"""


class Point:
    """Class creates new instance of Point."""

    def reset(self):
        """Function resets coordinate points back to origin."""
        self.x = 0
        self.y = 0


print('\nTesting attribute accessing...')
p1 = Point()
p1.reset()
print('X:', p1.x, 'Y:', p1.y)

"""
This same few lines of code could have been written as the following:
p = Point()
Point.reset(p) # 'p' represents a copy of a Point() object
print ('X:', p.x, 'Y:', p.y)
"""
