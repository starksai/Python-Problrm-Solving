num = input("enter a num: ")

sumNum = 0

for i in num :
    sumNum += int(i)



if int(num)%sumNum == 0 :
    print("Harshad Number")
else:
    print("Not a Harshad Number")