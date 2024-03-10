num=int(input("Enter the number :"))
temp=num
reverse=0
while(num>0):
        dig=num%10
        reverse=reverse*10+dig
        num=num//10
if(reverse==temp):
        print(temp,"is palindrom")
else:
        print(temp,"is not palindrom")