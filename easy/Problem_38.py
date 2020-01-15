# University of Washington CSE140 Mid term 2015

# Write a function build_index_grid(rows, columns) that, given a number of rows and columns, 
# creates a list of lists of that shape that includes the 'row,column' of that location.

# For example, after the following code is executed: new_index_grid = build_index_grid(4, 3)
# new_index_grid would contain:
# [['0,0', '0,1', '0,2'],
#  ['1,0', '1,1', '1,2'],
#  ['2,0', '2,1', '2,2'],
#  ['3,0', '3,1', '3,2']]
# Note that these are strings.

# After the following code is executed: small_index_grid = build_index_grid(1, 1)
# small_index_grid would contain: [['0,0']]

#PF-Prac-38


def build_index_grid(rows, columns):
    result_list = []
    for i in range(rows):
        temp =[]
        for j in range(columns):
            temp.append(str(i)+","+str(j))
        result_list.append(temp)

    return result_list


rows = 4
columns = 3
result = build_index_grid(rows, columns)
print("Rows:", rows, "Columns:", columns)
print("The matrix is:", result)
for i in result:
    print(i)
