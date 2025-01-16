num = [int(i) for i in input("enter: ").split()]
num.sort()
print("sorted array is : ",num)
incArr = []
decArr = []
res =" "

for i in range(0,len(num)//2):
    incArr.append(num[i])

for i in range(len(num)//2,len(num)):
    decArr.append(num[i])

temp = decArr
temp.reverse()
finalArray = incArr + decArr
print("finalarray  is : ",finalArray)
for i in finalArray:
    str_i = str(i)
    res += str_i+" "
print(res)