num=int(input("enter the number :"))
temp=num
sum=0
while(num>0):
        rem=num%10
        fact=1
        for i in range(1,rem+1):
                fact*=i
        sum=sum+fact
        num=num//10
if(temp==sum):
        print(temp,"is strong number")
else:
        print(temp,"is not a strong number")