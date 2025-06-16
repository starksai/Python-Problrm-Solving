#  WAP to print matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         res += str(mat[i][j])+" "
#     print(res)


####################################################################################################################

# WAP to transpose the matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         res += str(mat[j][i])+" "
#     print(res)

####################################################################################################################
#  Q)  WAP to print sum of diagonals of matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)

# res = 0
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if i==j or (i+j)==row-1:
#             res += mat[i][j]
# print(res)


####################################################################################################################


# Q) WAP to print outer layer of a matrix

# row,clo = [int(i) for i in input().split()]
# mat =[]
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# print(mat)


# for i in range(len(mat)):
#     res = ''
#     for j in range(len(mat[i])):
#         if i==0 or j==0 or i==row-1 or j==clo-1:
#             res += str(mat[i][j])+" "
#         else:
#             res += "  "
#     print(res)
        
####################################################################################################################
# Q) WAP to print max number in each row of matrix

# input: [[1,2,3],[4,3,2],[10,5,4]]
# output: 
# row1 max: 3
# row2 max: 4
# row3 max: 10

# row,col = [int(i) for i in input().split()]
# mat = []
# for i in range(row):
#     ele = [int(i) for i in input().split()]
#     mat.append(ele)
# # print(mat)

# for i in range(len(mat)):
#     print(f"row{i+1} max: {max(mat[i])}")

####################################################################################################################

        

# u have a matrix of n x n like

#    1 2 3
#    4 5 6
#    7 8 9   the output is => 7 4 1 5 9 6 3  it is like N shape


mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

def fn(m):
    
    for i in range(len(mat)):
        for j in range(len(m[i])-1,-1,-1):
            if i==j or i==0 or i==len(m[i])-1:
                print(m[j][i],end=" ")
    
    
fn(mat)
