# CSE160-Midterm-2015 Spring

# Write a function maxvalue_in_column(pixel_grid)
# that, given a list of lists of integers, 
# creates a list of integers that includes the maximum value found in each column of pixel_grid.

# You can assume that pixel_grid will always contain at least one row and one column and 
# that the values in pixel_grid will be between 0 and 255 and 
# that each row will contain the same number of columns.

# Here are a few examples. After the following code is executed:
# If pixel_grid contains	Col_list will be
# [ [ 4, 2, 3],
# [16, 5, 0],
# [ 3, 200, 6],
# [ 0, 10, 12] ]	[ 16, 200, 12 ]
# [ [ 4 ],
# [ 16 ],
# [ 3 ],
# [ 0 ] ]	[ 16 ]
# [ [ 4, 2, 3] ]	[ 4, 2, 3 ]
# [ [6] ]	[ 6 ]

#PF-Prac-42


def maxvalue_in_column(pixel_grid):
    #start writing your code here
    result_list = [0 for i in range(len(pixel_grid[0]))]

    for i in pixel_grid:
        for j in range(len(i)):
            if result_list[j] < i[j]:
                result_list[j] = i[j]

    return result_list


pixel_grid = [[4, 2, 3],
              [16, 5, 0],
              [3, 200, 6],
              [0, 10, 12]]
pixel_grid1 = [[4],
               [16],
               [3],
               [0]]
pixel_grid2 = [[4, 2, 3]]
pixel_grid3 = [[6]]

print("Pixel grid is:")
for i in pixel_grid:
    print(i)
output = maxvalue_in_column(pixel_grid)
print("The maximum values of each column are:", output)
