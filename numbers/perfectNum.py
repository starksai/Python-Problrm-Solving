# WAP to find perfect num 

num = int(input("enter a num: "))

sumNum = 0

for i in range(1,(num//2)+1):
    if num%i == 0:
        sumNum += i
print(sumNum == num)


################################################################################################################

#find perfect numbers upto n number

# n = int(input())
# c=0
# for j in range(1,n+1):
#     res=0
#     for i in range(1,(j//2)+1):
#         if j%i==0:
#             res = res+i
#     if(j==res):
#         c+=1
# print("There are two perfect numbers: ",c)

# # method 2

# num = int(input("enter: "))


# def isPerfect(n):
#     res = 0
#     for i in range(1,n):
#         if n%i == 0 :
#             res += i
#     return res == n
    
# for j in range(1,num+1):
#     if (isPerfect(j)):
#         print(j, end=" ")


