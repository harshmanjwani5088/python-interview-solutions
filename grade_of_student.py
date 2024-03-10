#grade of student
grade=float(input("Enter your percentage :"))
str="congratulations you got"
if(grade>=90.0):
        #print("Congratulation you got 'A+' grade")
        print(str,"A+ grade")
elif(grade>=80.0):
        #print("Congratulation you got 'A' grade")
        print(str,"A grade")
elif( grade>=70.0):
        #print("Congratulation you got 'B+' grade")
        print(str,"B+ grade")
elif( grade>=60.0):
        #print("Congratulation you got 'B' grade")
        print(str,"B grade")
elif( grade>=50.0):
        #print("Congratulation you got 'C' grade")
        print(str,"C grade")
elif( grade>=40.0):
        #print("Congratulation you got 'P' grade")
        print(str,"P grade")
else:
        print("Better luck next time")