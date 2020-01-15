# Write a python function which accepts a list of strings
# containing details of deposits and withdrawals made in a bank account 
# and returns the net amount in the account.
# Suppose the following input is supplied to the function
# ["D:300", "D:300", "W:200", "D:100"] where D means deposit and W means withdrawal,
# then the net amount in the account is 500.


# Sample Input	Expected Output
# ["D:300", "D:200", "W:200", "D:100"]	400
# ["D:350", "W:100", "W:500", "D:1000"]	750

#PF-Prac-8
def calculate_net_amount(trans_list):
    #start writing your code here
    net_amount = 0
    for i in trans_list:
        a, b = i.split(':')
        if a == 'D':
            net_amount += int(b)
        else:
            net_amount -= int(b)

    return net_amount


trans_list = ["D:300", "D:200", "W:200", "D:100"]
print(calculate_net_amount(trans_list))
