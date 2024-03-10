# vowel or consonent
chr=input("Enter a character :")
if(len(chr!=1)):
        print("Enter single character")
elif(chr=="A"or chr=="a" or chr=="E" or chr=="e" or chr=="I" or chr=="i" or chr=="O" or chr=="o" or chr=="U" or chr=="u"):
        print(chr,"is a vowel")
else:
        print(chr,"is a consonent")

