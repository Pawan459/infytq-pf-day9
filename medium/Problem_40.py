# University of Washington CSE140 Final 2015
# Given a list of lists of integers, write a python function, index_of_max_unique, 
# which returns the index of the sub-list which has the most unique values.

# For example:
# index_of_max_unique([[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12]]) 
# would return 2 since the sub-list at index 2 has the most unique values in it(6 unique values).

# index_of_max_unique([[4, 5], [12]]) 
# would return 0 since the sub-list at index 0 has the most unique values in it(2 unique values).

# You can assume that neither the list_of_lists nor any of its sub-lists will be empty.

# If there is a tie for the max number of unique values between two sub-lists, return the index of the first sub-list encountered(when reading left to right) that has the most unique values.

#PF-Prac-40

#PF-Prac-40


def findUniqueValue(li):
    dic = dict()
    for i in li:
        try:
            dic[i] += 1
        except:
            dic[i] = 1
    return len(dic)


def index_of_max_unique(num_list):
    #start writing your code here
    index = 0
    max_len = -1
    for i in range(len(num_list)):
        unique_values = findUniqueValue(num_list[i])
        if max_len < unique_values:
            index = i
            max_len = unique_values
    return index


num_list = [[1, 3, 3], [12, 4, 12, 7, 4, 4],
            [41, 2, 4, 7, 1, 12], [1, 2, 3, 4, 5, 6]]
num_list1 = [[4, 5], [12], [3, 8]]
print("Number list:", num_list)
output = index_of_max_unique(num_list)
print("The index of sub list containing maximum unique elements is:", output)
