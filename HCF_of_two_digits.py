num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))
minnum=min(num1,num2)
for i in range(1,minnum+1):
        if(num1%i==0) and (num2%i==0):
                hcf=i
print("HCF is",hcf)