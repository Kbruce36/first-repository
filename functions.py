#a collection of code
#a collection of instructions

def function1():
    print("within the function")
    print("also within")
print("outside the function")

function1()

#mapping
def function2(x):
    return 2*x
a = function2(3)
#the answer will be assigned to a and it is called a return value.
 
print(a)
b = function2(4)
c  = function2(2)
print(b)
print(c)

def USD():
    ugx = int(input("enter amount in ugx: "))
    x = 3500
    value = ugx / x
    print("the amount in dollars is: ",value,"dollars")
    return value

USD()




















'''

def greeting():
    hello = "hello"
    print(hello)
 

def say(saying):
    #saying = input("what do you want to say? ")
    print(saying)


greeting()
saying = 'kamugisha'
say(saying+"bruce")

'''