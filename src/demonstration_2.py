"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""


def pivot_index(nums):
    # Create a total sum variable from the sum of all items in the nums
    total_sum = sum(nums)
    # set sum to zero
    # iterate over nums
    # increment sum by num

    # create a left sum variable starting at zero
    left_sum = 0

    # iterate over nums extracting the index and the value
    for idx, num in enumerate(nums):
        # check if the left_sum is equal to the total sum - the left sum - num Value
        if left_sum == (total_sum - left_sum - num):
            # return the index to the caller
            return idx

    # increment the left sum by the pivot index (num)
    left_sum += num

    return -1


print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
