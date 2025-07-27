"""
Approach:
Make a pointer for the next non-val element.
Go through every element of the array and if it's not the value to remove, assign it to the pointer and increment the pointer by 1.
The pointer ends up being the count of elements that are not equal to the value to remove.
"""