# global variable : variable declared outside the functions
# local varivale : variable declared inside  the fucntion

                               #global 

wish="good morning"    #global variable declared outside the fucntion
def greet():
    print(wish)        #possible to access

print(wish)           # possible to access

greet()               # call the fucntion


                               #local
def greet():
    wish="good evening"   #local variable declared inside the fucntion
    print(wish)           #possible to access

print(wish)               # not possible to access

greet()              # call the fucntion
                               

