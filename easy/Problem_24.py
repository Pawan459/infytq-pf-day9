# Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.
# Sample Input	Expected Output
# 14 and 35	7
# 800 and 2800	400

#PF-Prac-24


def find_gcd(num1, num2):
    #start writing your code here
    if num2 == 0:
        return num1
    return find_gcd(num2, num1%num2)


num1 = 45
num2 = 9
print(find_gcd(num1, num2))
