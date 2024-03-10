num=int(input("Enter the number :"))
x=num
sq=x**2
t=10
flag=0
while(num>0):
        rem=sq%t
        if(rem==x):
                flag=1
        num=num//10
        t=t*10
if(flag==1):
        print(x,"is an automorphic number")
else:
        print(x,"is not an automorphic number")
