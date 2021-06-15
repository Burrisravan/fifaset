                               #postional argument-1
def add(a,b):
    # print('a=',a)
    # print('b=',b)
    result=a+b
    return(result)

x=add(4,5)
print(x)

 #seond method.

def add(a,b):
    result=a+b
    print(result)

add(6,7)    

                
 
                              #keyword argument-2
def add(a,b):
    result=a+b
    print(result)

x=add(a=10,b=20)          
x=add(b=9,a=5)            

                             #Default Argument-3

def add(a=2,b=20):
    result=a+b
    print(result)

add()    


                            #method 2
def add(a,b=14):
    result=a+b
    print(result)

add(4)    #or
add(a=13)                 

 
                           #variable length argument
def add(*numbers):
    result=0
    for i in numbers:
        result= result+i
        print(result)

add(5,6,7,8,9,10)          # to add multiple variables












                          

 
