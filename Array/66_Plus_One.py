"""
Approach:
Add 1 to the last index digit. If it's not 10, just return the digits.
If it's 10, update it to 0 and add 1 to the left (carry).
Repeat this until the next digit doesn't add up to 10 or it's the first index (meaning '1' should be inserted at the first index).
"""

# 0ms solution - O(n)

def plusOne(self, digits):
    i = len(digits) - 1

    digits[i] += 1  # add 1 to the last index digit
    
    while digits[i] == 10:
        digits[i] = 0  # if it adds to 10, update it to 0
        if i > 0:
            digits[i-1] += 1
            i -= 1
        else:
            digits.insert(0, 1)  # if the first digit was 9, insert 1 to the first index
    
    return digits
