"""
Approach:
Strip the whitespaces at the start and the end.
Start a for loop from the last index and count the number of characters until finding a whitespace.
"""

# 0ms solution - O(n)

def lengthOfLastWord(self, s):
    striped_string = s.strip()
    count = 0

    for i in range(len(striped_string) - 1, -1, -1):
        if striped_string[i] != ' ':
            count += 1
        else:
            return count
        
    return count
