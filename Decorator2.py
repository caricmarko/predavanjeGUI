# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())

# A Python program to demonstrate that a function
# can be defined inside another function and a
# function can be passed as parameter.
  
# Adds a welcome message to the string
def messageWithWelcome(str):
  
    # Nested function
    def addWelcome():
        return "Welcome to "
  
    # Return concatenation of addWelcome()
    # and str.
    return  addWelcome() + str
  
# To get site name to which welcome is added
def site(site_name):
    return site_name
  
print(messageWithWelcome(site("GeeksforGeeks")))

# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
  
    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)
  
    # Decorator returns a function
    return addWelcome
  
@decorate_message
def site(site_name):
    return site_name
  
# Driver code 
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks"))