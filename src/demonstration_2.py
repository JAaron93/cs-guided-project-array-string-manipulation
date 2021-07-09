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
