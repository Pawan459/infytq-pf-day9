# A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, 
# the next list in the sequence is formed by taking the absolute differences of neighboring
# integers in the previous list.
# Start List: [0,653,1854,4063]

# Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]

# Assumption: The Ducci sequence ends with a list containing 0s and 
# the starting list contains four elements.

# Write a python function that takes a starting list of integers and a number ‘n’ as input, 
# and returns the nth element of the Ducci sequence.

# Sample Input	Expected Output
# test_list=[0,653,1854,4063]
# n = 1
# [548,1008,1854,3410]

#PF-Prac-20


def ducci_sequence(test_list, n):
    #start writing your code here
    final_list = []
    final_list.append(test_list)
    for i in range(n+1):
        temp_li = []
        j = 0
        while j < len(final_list[0]):
            diff = abs(final_list[i][j] - final_list[i][(j+1)%len(final_list[0])])
            temp_li.append(diff)
            j += 1
        final_list.append(temp_li)
    # print(final_list)

    return final_list[n+1]


ducci_element = ducci_sequence([0, 653, 1854, 4063], 3)
print(ducci_element)
