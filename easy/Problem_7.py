'''
Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

For example, 123 is a seed of 738 as 123*1*2*3 = 738.


Sample Input	Expected Output
123,738	True
45,1000	False
'''

#PF-Prac-7
def seed_no(number,ref_no):
    result = number
    for i in str(number):
        result *= int(i)

    return result == ref_no
    
number=123
ref_no=738
print(seed_no(number,ref_no))
