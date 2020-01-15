# Given a list of numbers, write a python function to 
# exchange the first n/2 elements of a list with the last n/2 elements. 
# The function should return the new list.
# n represents the number of elements in the list. Assume that it will always be even.


# Sample Input	Expected Output
# [1,2,3,4,5,6,7,8,9,10]	[10,9,8,7,6,1,2,3,4,5]

#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    n = len(number_list)
    return number_list[n//2:][::-1] + number_list[:n//2]


number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))
