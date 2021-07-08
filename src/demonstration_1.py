"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


# def plus_one(digits):
#     # get the len of the list and set it to a variable n
#     n = len(digits)

#     # iterate over the digits using the index of i
#     for i in range(n):
#         # create an index from n - 2 - i to reverse the conceptual flow of the data
#         idx = n - 1 - i

#         # check if the digits at the index are equal to 9
#         if digits[idx] == 9:
#             # set the digits at the index to zero
#             digits[idx] = 0
#         # otherwise
#         else:
#             # increment the digits at index
#             digits[idx] += 1
#             # return the digits to the caller
#             return digits

#     # return the digits with a 1 perpended to them
#     # Doesn't matter how many 9s, we're just pushing 1 to the front of the list
#     return [1] + digits


# Devin's method
# def plus_one(digits):
#     strArr = [str(digit) for digit in digits]
#     num = int(''.join(strArr))
#     num += 1
#     numArr = [int(digit) for digit in str(num)]
#     return numArr

# Justin's method
def plus_one(digits):
    output_str = [str(i) for i in digits]
    output_num = int(''.join(output_str)) + 1
    return list(map(int, str(output_num)))


print(plus_one([1, 3, 2]))
print(plus_one([3, 2, 1, 9]))
