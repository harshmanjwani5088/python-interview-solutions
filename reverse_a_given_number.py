num=int(input("Enter the number :"))
while(num!=0):
        digit=num%10
        num=num//10
        print(digit,end="")