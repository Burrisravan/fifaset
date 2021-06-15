name='sravan'
age=25
height=5.8


print("my name is ",name, "my age is ",age,"my height is ",height)   # 1st method 
print("my name is %s my age is %d my height is %f " %(name,age,height)) # second method
print("My name is {} My age is {} My height is {}".format(name,age,height)) # 3rd methd easy one



'hello,{}'.format('sravan')                             # hello sravan
"{},{},{}".format("hi","hello","how are you")           # hi hello how are you
"{2},{0},{1}".format("hi","hello","how are you")        # hello how are you  hi
"{a},{b},{c}".format(a="hi",b="hello",c="how are you")  # giving key words
"{{{}}}".format("sravan")                               # gives {sravan}





















