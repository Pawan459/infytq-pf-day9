# Write a python function which accepts a list of numbers 
# and returns true if the list contains a 2 next to a 2. Otherwise it should return false.
# Sample Input	Expected Output
# [1, 2, 1, 2, 3, 4, 5, 2, 2]	True
# [3, 2, 5, 1, 2, 1, 2]	False

#PF-Prac-15


def check_22(num_list):
    #start writing your code here
    for i in range(len(num_list) - 1):
        if num_list[i] == 2 and num_list[i+1] == 2:
            return True
    return False


print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))
