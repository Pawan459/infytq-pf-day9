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


#PF-Prac-34
def check_well_formatted(input_item, list_label):
    #Start writing your code here
    # Condition 1
    if type(input_item) == list:
        # Condtion 2
        if len(input_item) >= 2:
            # Condition 3
            if input_item[0] in list_label:
                # Condition 4
                for i in input_item[1:]:
                    if type(i) == str or check_well_formatted(i, list_label):
                        continue
                    else:
                        return False
                return True
    return False


input_list1 = ['Ant', ['Apple', 'Mango'], ['Orange']]
list_label1 = ['Ant', 'Apple', 'Orange']
result = check_well_formatted(input_list1, list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")