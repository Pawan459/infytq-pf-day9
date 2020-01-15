# Write a python function to find and display the five digit number 
# in which the first digit is two more than the second, 
# the second digit is two more than the third, 
# the fourth digit is two less than the third, 
# and the last digit is two more than the fourth. 
# The sum of the third, fourth, and fifth digits equals the first. The sum of all the digits is 19.


'''
Pre-requisites:
Let's consider the the digits of five digit number be a , b, c, d, e respectively
1. sum of all digits is 19
    a + b + c + d + e = 19
2. last digit is two more than the fourth:
    e = d + 2
3. fourth digit is two less than the third:
    d = c - 2
4. the second digit is two more than the third:
    b = c + 2
5. the first digit is two more than the second:
    a = b + 2

6. Now watching all these condition solving this:
    from 5 min value of a = 2
    from 4 min value of b = 2 that's why a = 4
    from 3 min value of d = 0 and c = 2 that's why b = 4 and a = 6
    from 2 min value of e = 2

7. Minimum Five digit number with sum of digits less than 19
    with all condition satisfied
        6 4 2 0 2 => sum of digits is 14 that is 5 less than the required digit

        we have five digit too so adding 1 to each will satisfy all the required condition

8. Required Number is 7 5 3 1 3

'''

'''
    Another solution is that we can iterate through 10000 smallest five digit number to
    99999 largest five digit number inclusive and check the given condition considering the number as string.
'''

#PF-Tryout


def find_five_digit():
	#start writing your code here
    return 75313



print(find_five_digit())
