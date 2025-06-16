# Q)  

#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 


# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     for s in range(rows-i):
#         print(" ",end="")
        
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

#################################################################################################################

#  Q)

# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     val=1
#     for j in range(rows-i+1,0,-1):
#         print(val,end=" ")
#         val+= 1
#     print()

# other method
# rows = int(input("Enter rows: "))
# for i in range(rows,-1,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#################################################################################################################

# Q) 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     for s in range(i-1):
#         print(" ", end="")
#     for j in range(rows-i+1,0,-1):
#         print("*",end=" ")
#     print()

# rows = int(input("Enter rows: "))
# for i in range(rows,-1,-1):
#     print(" "(rows-i)+" "*i)

#    OR

# rows = int(input("Enter rows: "))
# for i in range(rows,-1,-1):
#     for s in range(rows-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#################################################################################################################


# Q)     
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 



# rows  =int(input("enter no. of rows: "))

# for i in range(1,rows+1):
#     print("  "* (rows-i), end="")
#     print("* "*i)
    # for j in range(1,i+1):
    #     print("* ",end="")
    # print()

#################################################################################################################
# Q)

# * * * * 
#   * * * 
#     * * 
#       * 


# rows = int(input("enter no. of rows: "))

# for i in range(rows,-1,-1):
#     print(" "*2*(rows-i),end="")
#     for j in range(1,i+1):
#         print("* ", end="")
#     print()

#################################################################################################################
# Q)  


#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     * 
#   *   *
#    * *
#     *



# step1:          
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# step2:
# for this use conditions j==1, i==j  (UPPER half)  i<=rows
# (LOWER half) conditions are j==1 and j==2*rows-i
# *
# * *
# *   *
# *     *
# *       *
# *     *
# *   *
# * *
# *


#  step3:
# add spaces in front of every row

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


# rows = int(input("enter: "))
# for i in range(1,2*rows):
#     spaces = rows-i if i<=rows else i-rows
#     print(" "*spaces,end="")
#     for j in range(1,2*rows):
#         if i<=rows:
#             if j==1 or i==j:
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#         else:
#             if j==1 or j==2*rows-i:
#                 print("* ",end="")
#             else:   
#                 print("  ",end="")
#     print()


# other method

# rows = int(input("enter: "))

# for i in range(1,2*rows):
#     stars = i if i<=rows else 2*rows-i
#     spaces = rows-i if i<=rows else i-rows
#     print(" "*spaces , end="")
#     for j in range(1,stars+1):
#         if j==1 or j==i or j+i==2*rows:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
            
#################################################################################################################


# 1       5 
#   2   4   
#     3     
#   2   4   
# 1       5 


# to print left=>right diagonal formula is i==j
# and to print right to left formula is j==rows-i+1
# otherwise just print space


# rows = int(input("enter: "))

# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i==j or j==rows-i+1:
#             print(j,end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#################################################################################################################
# Q) 


#         1 
#       * 2 * 
#     * * 3 * * 
#   * * * 4 * * * 
# * * * * 5 * * * * 



# rows = int(input("enter : "))

# for i in range(1,rows+1):
#     stars = i-1
#     spaces = rows-i
#     print("  "*spaces, end="")
#     print("* "*stars,end="")
#     print(i,end=" ")
#     print("* "*stars)


#################################################################################################################
# Q)
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


# rows = int(input("enter : "))

# for i in range(1,2*rows):
#     stars = i if i<=rows else 2*rows-i
#     spaces = rows-i if i<=rows else i-rows
#     if i<=rows:
#         print(" "*spaces,end="")
#         print("* "*stars)
#     else:
#         print(" "*spaces,end="")
#         print("* "*stars)


#################################################################################################################


# Q)

# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 



# rows = int(input("enter rows: "))

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if i%2==1:
#             if j%2==1:
#                 print(1,end=" ")
#             else:
#                 print(0,end=" ")
#         else:
#             if j%2==1:
#                 print(0,end=" ")
#             else:
#                 print(1,end=" ")
#     print()
            