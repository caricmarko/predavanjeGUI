def foo(*args):
    for a in args:
        print(a)        

foo(1)
# 1

foo(1,2,3,"Nesto")
# 1
# 2
# 3

def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])  

bar(name='one', age=27, info='Nesto')
# name one
# age 27
# info Nesto

def foo(kind, *args, **kwargs):
    for a in args:
        print(a)  
    for a in kwargs:
        print(a, kwargs[a]) 

foo(1,2,3)
foo(1,2,3,name='aaa')
#foo(1,2,3,name='aaa',2)
foo(1,2,3,name='aaa',ime=7)