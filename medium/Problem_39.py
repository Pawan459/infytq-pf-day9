# Suppose you are given a data structure which is a list of dictionaries as follows:
# cities = [
# {'Name':'Vancouver','State':'WA','Population':161791},
# {'Name':'Salem','State':'OR','Population':154637},
# {'Name':'Seattle','State':'WA','Population':608660},
# {'Name':'Spokane','State':'WA','Population':208916},
# ...
# ]


# Complete the function max_in_state to return the city (as a dictionary) 
# with the highest population in a given state. 
# If the population is a tie then return the city that comes first alphabetically.

# If cities contained only the dictionaries above, a call to max_in_state(cities, 'WA') would return:
# {'Name':'Seattle','State':'WA','Population':608660}

#PF-Prac-39
def max_populated_state(cities_dict, state):
    #start writing your code here
    max_populated_city = cities_dict[0]
    for i in cities_dict:
        if i['State'] == state:
            if max_populated_city['State']!=state:
                max_populated_city = i
            else:
                if max_populated_city['Population']<=i['Population']:
                    if max_populated_city['Population'] == i['Population']:
                        max_populated_city = i if i['Name']<max_populated_city['Name'] else max_populated_city
                    else:
                        max_populated_city = i
        
    return max_populated_city


cities_dict = [
    {'Name': 'Vancouver', 'State': 'WA', 'Population': 161791},
    {'Name': 'Salem', 'State': 'OR', 'Population': 154637},
    {'Name': 'Seattle', 'State': 'WA', 'Population': 80885},
    {'Name': 'Bellingham', 'State': 'WA', 'Population': 608660},
    {'Name': 'Spokane', 'State': 'WA', 'Population': 208916},
    {'Name': 'Bellevue', 'State': 'WA', 'Population': 608660},
    {'Name': 'Portland', 'State': 'OR', 'Population': 583776}
]
state = "WA"
print("The city details are:", cities_dict)
print("State:", state)
output = max_populated_state(cities_dict, state)
print("The highest populated city in the given state is:", output)
