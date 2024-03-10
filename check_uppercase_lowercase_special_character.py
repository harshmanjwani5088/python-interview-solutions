chr = input("enter the character :")
if(len(chr)!=1):
          print("Invalid input")
elif(ord(chr)>=65 and ord(chr)<=90):
        print("Character is uppercase")
elif(ord(chr)>=97 and ord(chr)<=122):
        print("Character is lowercase")
elif(ord(chr)>=48 and ord(chr)<=57):
         print("Character is digit")
elif(ord(chr)>=32 and ord(chr)<=47 or ord(chr)<=58 and ord(chr)>=64 or ord(chr)>=91 and ord(chr)<=96 or ord(chr)>=123 and ord(chr)<=126):
        print("Character is special character")
else:
        print("invalid input")
