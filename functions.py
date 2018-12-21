def Hello():
    print("I am in Hello")

Hello()

def Hello2(greetings = "No value"):
    print("I am in Hello2..",greetings)

Hello2("Hello Motto")
Hello2("Another Msg")

def addIt(value1,value2):
    print(value1,"+",value2,"=",(value1+value2))

addIt(5,3)
Hello2() # automatically compansates for the the value when it is not supplied

'''
Creating functions with a
variable no of arguments
'''

def Hello3(argCount,*varArgs):
    print("u passed",argCount,"arguments. below r they")
    for Arg in varArgs:
        print(Arg)

Hello3(2,"bg","cg")

def doAdd(val1,val2):
    return val1 + val2

result=doAdd(3,9)

print("result",result)

print("comparison result =",doAdd(5,3)==doAdd(0,5))

Name=input("What is your Name")
print("My Name is",Name)

number=float(input("Enter a float no"))

print("the value is",number)

