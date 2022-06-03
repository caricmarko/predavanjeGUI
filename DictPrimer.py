class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__)
print(foo.__dict__)
print(bar.__dict__)