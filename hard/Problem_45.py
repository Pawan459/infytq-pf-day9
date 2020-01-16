# UC Berkley CS61A Fall 2011 Midterm 2

# Write a function longest_common_substring that takes two strings word1 and word2 
# and returns the maximum overlap between the strings.


# Sample Input	Expected Output
# 'pirate', 'teepee'	'te'
# 'fish', 'bowl'	''
# 'assured', 'measured'	'sured'
# 'catenation', 'concatenation'	'catenation'



#PF-Prac-45

def longest_common_substring(string1, string2):
    X = string1
    Y = string2
    m = len(X)
    n = len(Y)
    LCSuff = [[0 for i in range(n + 1)]
           for j in range(m + 1)]
    length = 0
    row, col = 0, 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if length < LCSuff[i][j]:
                    length = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0
    if length == 0:
        return ''

    resultStr = ['0'] * length
    while LCSuff[row][col] != 0:
        length -= 1
        resultStr[length] = X[row - 1]
        row -= 1
        col -= 1
    return ''.join(resultStr)

output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)
