num=int(input("Enter the number :"))
n1,n2,sum=0,1,0
if(num<=0):
        print("enter the positive number")
else:
        for i in range(1,num+1):
                print(sum,end=" ")
                n1=n2
                n2=sum
                sum=n1+n2