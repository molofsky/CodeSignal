"""
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.

You have s cents on your account before the call. 
What is the duration of the longest call (in minutes 
rounded down to the nearest integer) you can 
have?
"""

def solution(min1, min2_10, min11, s):
    mins = 0

    s -= min1 
    if s >= 0: mins += 1
    
    for i in range(9):
        if (s > 0): 
            s -= min2_10
            if (s >= 0): mins += 1
            
    while (s > 0):
        s -= min11
        if (s >= 0): mins += 1

    return mins
