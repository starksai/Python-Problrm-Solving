# # given a array of ints, every array element appers twice except for one element. find that element

# num = input().split()

# temp = []

# x = False

# for i in num:
#     if i not in temp:
#         temp.append(i)

# for i in temp:
#     if num.count(i) ==1:
#         x =True
#         break

# if x:
#     print(i)
# else:
#     print("there is no single time elemnts")


################################## USING FUNCTION ###############################################################

def repeted(num):
    temp =[]
    x = False
    for i in num:
        if i not in temp:
            temp.append(i)
    for i in temp:
        if num.count(i) == 1:
            return i
    return "there is no single element"

num  = input().split()
print(repeted(num))