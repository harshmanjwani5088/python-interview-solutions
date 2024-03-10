# find the number in tuple
num=(1,3,2,4,5,3,5,3,6,3,7,8,5,8,5,9,0)
x=int(input("Find the integer :"))
i=0
while(i<(len(num))):
        if(x==num[i]):
                print (x, "is found")
        print("Finding...")
        i+=1
