"""
Approach:
For each string, check the characters from index 0 using two pointers.
For each character in t, if the character matches the character pointed currently in s, move the s pointer and check the next character.
If s pointer goes over the maximum index, return True
"""
