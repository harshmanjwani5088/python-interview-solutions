arm=int(input("Enter the number"))
orgarm=arm
sum=0
while(arm!=0):
        digit=arm%10
        sum=sum+digit**len(str(orgarm))
        arm=arm//10
if(orgarm==sum):
        print(orgarm,"is an armstrong number")
else:
        print(orgarm,"is not an armstrong number")