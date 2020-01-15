# Write a python function to identify and return the number name of a given number. 
# The number should be in the range 1 to 1000. If the number is invalid, return -1.

# Example:

# Sample input	Expected output
# 1	one
# 15	fifteen
# 45	forty five
# 125	one hundred and twenty five
# 999	nine hundred and ninety nine
# 1000	one thousand
# 1211	-1

#PF-Prac-33

#PF-Prac-33


def integer_to_english(number):
    #start writing your code here
    if number > 1000:
        return -1
    msg = ""
    num = str(number)
    l = len(num)

    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    two_digits = [" ", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens_multiple = [" ", " ", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]

    tens_power = ["hundred", "thousand"]
    if (l == 1):
        msg += single_digits[ord(num[0]) - '0']
        return msg
    x = 0
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                msg += (single_digits[ord(num[x]) - 48]+" ")
                msg += (tens_power[l - 3]+" ")
                l -= 1
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x]) - 48)
                msg += two_digits[sum]
                return msg
            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                msg += "twenty"
                return msg
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    msg += (tens_multiple[i]+" ")
                else:
                    msg += ""
                x += 1
                if(ord(num[x]) - 48 != 0):
                    msg += single_digits[ord(num[x]) - 48]
        x += 1
    return msg


number = 789
print(integer_to_english(number))
