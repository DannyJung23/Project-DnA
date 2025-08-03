"""
Approach:
Add 1 to the last index digit. If it's not 10, just return the digits.
If it's 10, update it to 0 and add 1 to the left (carry).
Repeat this until the next digit doesn't add up to 10 or it's the first index (meaning '1' should be inserted at the first index).
"""
