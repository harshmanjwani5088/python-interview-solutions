start=int(input("enter the starting number of range :"))
end=int(input("enter the ending number of range :"))
sum=0
for start in range(start,end+1):
        sum+=start
print("sum of given range is :",sum)