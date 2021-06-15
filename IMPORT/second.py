import first 
#accessing variables
print(first.x)
print(first.y)
#accessing functions
print(first.add(5,6))
print(first.sub(6,3))
print(first.mul(3,4))
print(first.div(50,5))

#accessing classes
x=first.wish("sravan")
print(x.cv)
print(x.greet())
 

                                # 2nd type RENAMEING
                                
import first  as sravan
#accessing variables
print(sravan.x)
print(sravan.y)
#accessing functions
print(sravan.add(5,6))
print(sravan.sub(6,3))
print(sravan.mul(3,4))
print(sravan.div(50,5))
#accessing classes
x=sravan.wish("sravan")
print(x.cv)


                    # when you need only one paticular fucntion not all the fucntion or classes
from first import add
add(10,20)    
from first import add,sub
from first import wish
# from first import greet
from first import *
