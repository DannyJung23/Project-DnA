"""
Approach:
Use binary search to find the target number.
Make 2 pointers "low" and "high" which set the index boundary of the searching half, initially set to the first and last index.
Iterate through a while loop until the index of the low pointer exceeds the index of high.
Calculate the middle index in each iteration and check if it's the target number.
If not, update either low or high to focus on the correct half.
"""