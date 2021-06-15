x=20
y=2

# we have functions
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)   
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)       

# we also have class in the file

class wish:
    cv=56
    def __init__(self,name):
        self.my_name = name

    def greet(self):
        print("hello good morning!".format(self.my_name))        