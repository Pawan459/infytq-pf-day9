# Given a string, write a python function to 
# return True if the strings "mat" and "jet" 
# appear the same number of times in the given string, else return False.
# Note: Perform case insensitive string comparison wherever necessary.

# Sample Input	Expected Output
# Jet on the Mat but mat is too long	False
# mat jet Jet Mat	True

#PF-Prac-26


def check_occurence(string):
    #start writing your code here
    string = string.lower()
    mat, jet = 0, 0
    for i in string.split(' '):
        if i == 'mat':
            mat += 1
        elif i == 'jet':
            jet += 1
    return mat == jet


string = "Jet on the Mat but mat is too long"
print(check_occurence(string))
