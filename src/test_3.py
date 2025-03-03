'''
You are given a parentheses sequence, check if it's regular.


Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;

For s = "()()())", the output should be
validParenthesesSequence(s) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string, consisting only of '(' and ')'.

Guaranteed constraints:
0 ≤ s.length ≤ 105.

[output] boolean

true is the sequence is regular and false otherwise.
'''


def validParenthesesSequence(s):
    counter = 0
    for item in s:
        if item == '(':
            counter += 1
        if item == ')' and counter > 0:
            counter -= 1
        elif item == ')' and counter == 0:
            return False
    return counter == 0


print(validParenthesesSequence("()()(())"))
print(validParenthesesSequence("()()())"))
print(validParenthesesSequence(""))
