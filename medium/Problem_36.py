# [Massachusetts Institute of Technology 6.00 Final Spring 2011]

# Part-1:
# Write a python function which accepts a string of words and a target word, 
# and returns the list of the positions of the target word in the string of words.

# Sample input	Expected output
# input String- we dont need no education we dont need no thought control no we dont
# target word- dont	[1, 6, 13 ]
# Part-2:
# Write a python function which accepts a string of words and returns a dict which contains the words in the input string as key and the list of positions of these words in the input string as value. Use the function written in part-1.

# Sample input	Expected output
# we dont need no education we dont need no thought control no we dont	{'no': [3, 8, 11], 'thought': [9], 'dont': [1, 6, 13], 'need': [2, 7], 'control': [10], 'we': [0, 5, 12], 'education': [4]}
# Note:
# 1.The words are separated by a single space.
# 2.There are no punctuation marks or upper case letters.

#PF-Prac-36


def find_target_positions(input_string, target_word):
    target_list = []
    #Start writing your code here
    li = list(map(str, input_string.split(' ')))
    for i in range(len(li)):
        if li[i] == target_word:
            target_list.append(i)
    return target_list


def find_inverted_index(input_string):
    target_dict = {}
    #Start writing your code here
    dic = dict()
    for i in input_string.split(' '):
        try:
            dic[i] += 1
        except:
            dic[i] = 1

    for i in dic.keys():
        temp_li = find_target_positions(input_string, i)
        target_dict[i] = temp_li

    return target_dict


input_string = "we dont need no education we dont need no thought control no we dont"
result_dict = find_inverted_index(input_string)
print(result_dict)
