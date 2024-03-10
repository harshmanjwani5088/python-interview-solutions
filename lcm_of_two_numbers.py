# Code for LCM
def lcm(num1,num2,maxnum):
        while(True):
                if(maxnum%num1==0 and maxnum%num2==0):
                        print("lcm of",num1,"and",num2,"is",maxnum)
                        break
                maxnum+=1

num1=int(input("Enter the number :"))
num2=int(input("Enter the number :"))
maxnum=max(num1,num2)
lcm(num1,num2,maxnum) 