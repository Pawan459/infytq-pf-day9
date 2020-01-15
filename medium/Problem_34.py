# Write a recursive python function which 
# returns True if the input is well-formatted with respect to the list labels. 
# Else it should return False.

# We say that an input is well-formatted with respect to the labels if:
# (a) input item is a list
# (b) input item has length at least two
# (c) input’s first item is in the list labels
# (d) each of the remaining items in input is either a string or a well-formatted list

# Sample input	Expected output
# input item	list label
# ['VP', ['V', 'eat']]	['VP', 'V']	True
# ['NP', ['N', 'a', 'or', 'b'], 'c']	['NP', 'V', 'N']	True
# [1, [2, 'oui', [1, 'no']], 'no']	[1,2]	True
# ['VP', ['V', 'eat']]	['VP']	False
# ['VP', ['V']]	['VP', 'V']	False

#PF-Prac-34


def check_well_formatted(input_item, list_label):
    #Start writing your code here
    if len(input_item) == 0:
        return True
    


input_list1 = ['VP', ['V', 'eat']]
list_label1 = ['VP', 'V']
result = check_well_formatted(input_list1, list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")
