# Given an integer n, write a python function to return true, 
# if it is possible to represent it as a sum of the squares of two different integers, 
# else return false.

#PF-Prac-32


def check_squares(number):
    #start writing your code here
    for i in range(number):
        for j in range(i+1, number):
            if i*i + j*j == number:
                return True
    return False


number = 68
print(check_squares(number))
