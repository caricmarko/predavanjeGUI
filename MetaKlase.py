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
test.foo = lambda self: print('Hello')
 
# creating object
myobj = test()
 
print(myobj.x)
myobj.foo()

def test_method(self):
    print("This is Test class method!")
 
# creating a base class
class Base:
    def myfun(self):
        print("This is inherited method!")
 
# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))
 
# Print type of Test
print("Type of Test class: ", type(Test))
 
# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))
 
# calling inherited method
test_obj.myfun()
 
# calling Test class method
test_obj.my_method()
 
# printing variable
print(test_obj.x)