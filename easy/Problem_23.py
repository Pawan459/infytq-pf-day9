# Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.
# Sample Input	Expected Output
# 42	True
# 66	False

#PF-Prac-23
def sum_of_digit(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result


def divisible_by_sum(number):
    #start writing your code here
    sod = sum_of_digit(number)
    return number % sod == 0


number = 42
print(divisible_by_sum(number))
