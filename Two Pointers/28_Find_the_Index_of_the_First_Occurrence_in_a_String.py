"""
Approach:
Loop through the haystack string from the first element.
For each element, run an inner loop (len(needle)) and compare each character if it matches the character of needle.
If not matching, break the inner loop and move onto the next element of haystack.
If the inner loop finishes without breaking, return the current pointer of the outer loop.
"""

# 0ms solution - O(n*m)

def strStr(self, haystack, needle):
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
        else:
            return i

    return -1
