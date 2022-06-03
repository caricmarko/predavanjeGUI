from functools import wraps
 
def debug(func):
    '''decorator for debugging passed function'''
     
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)
    return wrapper
 
def debugmethods(cls):
    '''class decorator make use of debug decorator
       to debug class methods '''
     
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls
 
class debugMeta(type):
    '''meta class which feed created class object
       to debugmethod to get debug functionality
       enabled objects'''
     
    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj
     
# base class with metaclass 'debugMeta'
# now all the subclass of this
# will have debugging applied
class Base(metaclass=debugMeta):pass
 
# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x+y
     
# inheriting Calc
class Calc_adv(Calc):
    def mul(self, x, y):
        return x*y
 
# Now Calc_adv object showing
# debugging behaviour
mycal = Calc_adv()
print(mycal.mul(2, 3))