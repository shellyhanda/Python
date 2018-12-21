testdata=int(input("Enter value >0 and <10 ??"))


if testdata == 6:
    print("you Entered 6")
else:
    if testdata > 0 and testdata < 10:
        print("your Entered value=",testdata)
    else:
        print("incorrect value",testdata)

print("1. Red")
print("2. Orange")
print("3. Yellow")
print("4. Green")

Choice=int(input("Select ur favorite color:"))
if (Choice==1):
    print("u Chose Red !!")
elif(Choice==2):
    print("u Chose Orange !!")
elif(Choice==3):
    print("u chose Yelllo !!")
elif(Choice==4):
    print("u chose Green !!")
else:
    print("u made an invalid choice")


    
 
