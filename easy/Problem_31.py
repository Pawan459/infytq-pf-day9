# Given a list of integers and a number. Write a python function to find 
# and return the sum of the elements of the list.
# Note: Don't add the given number 
# and also the numbers present before and after the given number in the list .
# Sample input	Expected output
# list=[1,2,3,4], number=2	4
# list=[1,2,2,3,5,4,2,2,1,2],number=2	5
# list=[1,7,3,4,1,7,10,5],number=7	9
# list=[1,2,1,2],number=2	0

#PF-Prac-31


#PF-Prac-31
def sum_of_elements(num_list, number):
    result_sum = 0
    index, i = 0, 0
    n = len(num_list)
    while i < n-1:
        if num_list[i] == number:
            index = i
            i += 2
            continue
        # print(i)
        if num_list[i] != number and num_list[i+1] != number:
            result_sum += num_list[i]
        i += 1
    if n - index > 2 and num_list[n-1] != number:
        result_sum += num_list[n-1]

    return result_sum


num_list = [1, 2, 3, 2, 4, 5, 7, 2]
number = 2
print(sum_of_elements(num_list, number))
