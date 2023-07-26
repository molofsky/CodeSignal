"""
Given an integer n, return the largest number that contains exactly n digits.
"""

def solution(n):
    result = "0"
    i = 0;
    while i < n:
        result = result + "9"
        i += 1
    
    return int(result)

