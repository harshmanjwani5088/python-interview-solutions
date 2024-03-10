num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
sum1,sum2=0,0
for i in range(1,num1):
        if(num1%i==0):
                sum1+=i  
for i in range(1,num2):
        if(num2%i==0):
                sum2+=i
if(num1==sum2 and num2==sum1):
        print(num1,"and",num2,"are amicable number")
else:
        print(num1,"and",num2,"are not a amicable number")