# University of Washington CSE140 Final Exam 2014
# Complete given function such that it returns the sum of the elements in num_list where num_list is a list of numbers.
# Do not alter the statements already provided.

#PF-Prac-37
def sum_of_list(num_list):
    #Start writing your code here
    if len(num_list) == 0:
        return 0
    lst = num_list
    #Do not alter the below line
    return lst[0] + sum_of_list(lst[1:])


num_list = [44, 23, 77, 11, 89, 3]
result = sum_of_list(num_list)
print("Sum of the elements:", result)
