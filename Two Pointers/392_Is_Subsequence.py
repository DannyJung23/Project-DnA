"""
Approach:
For each string, check the characters from index 0 using two pointers.
For each character in t, if the character matches the character pointed currently in s, move the s pointer and check the next character.
If s pointer goes over the maximum index, return True
"""

# 0ms solution - O(n)

def isSubsequence(self, s, t):
    if s == "":
        return True
    
    check_index = 0
    last_index = len(s) - 1

    for character in t:
        if character == s[check_index]:
            check_index += 1
            if check_index > last_index:
                return True
            
    return False


# 0ms solution - O(n)

def isSubsequence(self, s, t):
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
