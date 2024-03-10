# Code for alphabet
chr = input("Enter an alphabet :") 
if(len(chr)>1):
        print("Invalid input!!!")
elif(chr >= "a" and chr <= "z"):
        print("It is an alphabet")
elif(chr >= "A" and chr <= "Z"):
        print("It is an alphabet")
else:
        print("NOt an alphabet")