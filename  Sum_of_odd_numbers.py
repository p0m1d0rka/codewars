# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

# def row_sum_odd_numbers(n):
#     array_position = (n-1)*n/2
#     number = 2*array_position - 1
#     sum = 0
#     for i in range(1,n+1):
#         sum += 2*(array_position+i) - 1
#     return sum
    

# onerow with listcomprehansion
def row_sum_odd_numbers(n):
    return sum([2*((n-1)*n/2+i) - 1 for i in range(1,n+1)])
    

# best solution
# def row_sum_odd_numbers(n):
#     #your code here
#     return n ** 3