# CSE 140 Winter 2014

# Part 1
# You are given a dictionary of dictionaries (as shown below),
# that maps pollsters to stateEdges (remember that a stateEdge is a dictionary that maps states to edges).
# Write a function wa_edges that 
# returns a list of tuples 
# where each tuple holds the name of the pollster as the first element 
# and the edge corresponding to WA (Washington) as the second element.
# If that pollster does not have an edge for WA, store its value as None.

# input_data = { "Gallup": { "WA": 7, "CA": 15, "UT": -30 },
# "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 },
# "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 } }

# For example, calling get_edges(input_data) with input_data as ‘WA’ 
# returns a list containing these tuples (the order of the tuples may differ):
# [ ("Gallup", 7), ("SurveyUSA", None), ("Omniscient", -2.3) ]

# Part 2
# Given a dictionary of dictionaries (as used in the previous problem),
# write a function pollster_states that returns a dictionary that maps pollsters to a list of the states shown in their associated stateEdge.

# For example, calling pollster_states() returns a new dictionary containing these values (the order of the values may differ):
# { "Gallup": [ "WA", "CA", "UT" ],
# "SurveyUSA": [ "CA", "CO", "CT", "FL" ],
# "Omniscient": [ "AK", "WA", "CA" ] }

#PF-Prac-41
#PF-Prac-41
# Part-1


def get_edges(pollsters_stateedge_dict, state):
    #start writing your code here
    result_list = []
    for i in pollsters_stateedge_dict.keys():
        li = []
        li.append(i)
        if state in pollsters_stateedge_dict[i].keys():
            li.append(pollsters_stateedge_dict[i][state])
        else:
            li.append(None)
        result_list.append(tuple(li))
    return result_list

# Part-2


def find_pollster_states(pollsters_stateedge_dict):
    #start writing your code here
    result_dict = dict()
    for i in pollsters_stateedge_dict.keys():
        result_dict[i] = list(pollsters_stateedge_dict[i].keys())
    return result_dict


pollsters_stateedge_dict = {
    "Gallup": {"WA": 7, "CA": 15, "UT": -30},
    "SurveyUSA": {"CA": 14, "CO": 2, "CT": 13, "FL": 0},
    "Omniscient": {"AK": -14.0, "WA": -2.3, "CA": 20.9}
}
state = 'WA'
print("Pollsters, States and its edge details:", pollsters_stateedge_dict)
print("Given State:", state)
output = get_edges(pollsters_stateedge_dict, state)
print("Pollster Edge details for the given state:", output)

output1 = find_pollster_states(pollsters_stateedge_dict)
print("Pollster and their entire state details:", output1)
