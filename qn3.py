
try:  
    a = 10/0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Error exception raised." )
else:  
    print ("Success.")

try:
    a=10
    b=20
    assert a==b
except AssertionError:
        print("Asertion Error exception raised")

try:
    abc=[10,20,50]
    print(abc[6])
except IndexError:
        print("Index Error exception raised")
else:
        print("Success")

try:
    a=int(5)
    b=str
    c=a+b
except TypeError:
    print ('Type Error exception raised')
else:
    print ('No exception')

