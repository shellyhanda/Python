LetterNum=1
for Letter in "Howdy!!":
    print("Letter",LetterNum," is ",Letter)
    LetterNum+=1
 
value=input("Enter the Sting with less than 6 Character")

count=1
for Letter in value:
    print("Letter",count," is ",Letter)
    count+=1
    if(count>6):
        print("The String is too long")
        break
    
    
