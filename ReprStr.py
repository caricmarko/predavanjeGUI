s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))

s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))

import datetime
today = datetime.datetime.now()
  
# Prints readable format for date-time object
print (str(today))
  
# prints the official format of date-time object
print (repr(today))  

# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
#assert b != 0
#assert b != 0, "Zero Division Error"
#print(a / b)

batch = [ 40, 26, 39, 30, 25, 21]
 
# initializing cut temperature
cut = 26
 
# using assert to check for temperature greater than cut
for i in batch:
    assert i >= 26, "Batch is Rejected"
    print (str(i) + " is O.K" )
