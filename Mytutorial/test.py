print("object literals")
x,y,z=10,20,30

print(y)
print(x)
print(z)

complexno= 6+9j

complexno =complexno +1j
print("no -->"+ str(complexno.imag))

sentence="Alaice in Wonderland with me"
sentence_without_vowel =""
for word in sentence:
    word=word.lower()
    #print(word)
    #for word[0] in "aeiou":
        #print("{0} is in vowel".format(word[0]))
