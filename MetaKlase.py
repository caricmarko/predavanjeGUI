class Student:
    pass
stu_obj = Student()
 
# Print type of object of Student class
print("Type of stu_obj is:", type(stu_obj))
 
# Print type of Student class
print("Type of Student class is:", type(Student))

# Defined class without any
# class methods and variables
class test:pass
 
# Defining method variables
test.x = 45
 
# Defining class methods
test.foo = lambda self: print("Hello")
 
# creating object
myobj = test()
 
print(myobj.x)
myobj.foo()