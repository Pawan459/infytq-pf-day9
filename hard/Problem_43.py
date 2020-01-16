# CSE160-Midterm-2015 Spring

# You have a list of dictionaries with the following general structure:
# presidents =
# [ {'name':'George Washington', 'vp':'John Adams'},
# {'name':'John Adams', 'vp':'Thomas Jefferson'},
# {'name':'Zachary Taylor', 'vp':'Millard Fillmore'},
# {'name':'Dwight D. Eisenhower', 'vp':'Richard Nixon'},
# {'name':'Richard Nixon', 'vp':'Spiro Agnew'},
# {'name':'Richard Nixon', 'vp':'Gerald Ford'}, ....]

# For example, George Washington was a president who had John Adams serve as his Vice President ("vp").
# Note that if a president served for more than one term or had multiple vice presidents, 
# there could be multiple dictionaries listed for that president.

# promoted_vp_ (presidents) will return the list of all vice presidents that also served as president.
# E.g. if presidents consists of only the dictionaries listed above:
# It returns the list {'John Adams', 'Richard Nixon'}

#PF-Prac-43


def find_promoted_vp(presidents_dict):
    #start writing your code here
    
    return promoted_vp_list


def find_presidents_vp(presidents_dict, duration):
    #start writing your code here
    return promoted_vp_list


presidents_dict = [{'name': 'George Washington', 'vp': 'John Adams', 'period': '1990-1993'},
                   {'name': 'John Adams', 'vp': 'Thomas Jefferson',
                       'period': '1994-1996'},
                   {'name': 'Zachary Taylor', 'vp': 'Millard Fillmore',
                       'period': '1997-1999'},
                   {'name': 'Dwight D. Eisenhower',
                       'vp': 'Richard Nixon', 'period': '1999-2001'},
                   {'name': 'Richard Nixon', 'vp': 'Spiro Agnew',
                       'period': '2001-2002'},
                   {'name': 'Richard Nixon', 'vp': 'Gerald Ford', 'period': '2002-2004'}]

print("The president and vice president details:", presidents_dict)
output = find_promoted_vp(presidents_dict)
print("The list of vice presidents who also got promoted as presidents:", output)
duration = '1999-2005'
print("The president and vice president details:", presidents_dict)
print("Given duration:", duration)
output1 = find_presidents_vp(presidents_dict, duration)
print("The list of vice presidents who also got promoted as presidents in the given duration:", output1)
