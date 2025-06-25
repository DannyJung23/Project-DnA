"""
Approach:
Make 3 pointers starting from the end of the valid numbers of nums1, the end of nums2, and the physical end of nums1.
Scanning from the back, compare the numbers in nums1 and nums2 and fill up the 0 at k with the larger number.
"""

# 0ms solution - O(n+m)

def merge(self, nums1, m, nums2, n):
    i = m - 1  # pointer for nums1 starting from the end
    j = n - 1  # pointer for nums2 starting from the end
    k = m + n - 1  # pointer for inserting position in nums1 starting from the end
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


# 3ms solution - O(n(n+m))

def merge(self, nums1, m, nums2, n):
    i = 0
    j = 0
    end_of_nums1 = 0
    
    while i < m + n and j < n:
        if nums1[i] > nums2[j] or i >= m + end_of_nums1:
            nums1.insert(i, nums2[j])
            nums1.pop(-1)
            i += 1
            j += 1
            end_of_nums1 += 1
        else:
            i += 1
