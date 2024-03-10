num=int(input("Enter the number :"))
i,sum=1,0
while(num>i):
        if(num%i==0):
                sum=sum+i
        i+=1
if(num==sum):
        print(num,"is a perfect number")
else:
        print(num," is not a perfect number")
