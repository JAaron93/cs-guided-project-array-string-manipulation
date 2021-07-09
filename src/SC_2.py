'''
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

csCheckPalindrome("racecar") -> true
csCheckPalindrome("anna") -> true
csCheckPalindrome("12345") -> false
csCheckPalindrome("12321") -> true
'''

def csCheckPalindrome(input_str):
    palindrome = input_str[::-1]
    if input_str == palindrome:
        return True
    else:
        return False

# Seeing as palindromes are reversed words such as "Hannah" that can be spelled the same way in the reverse, I opted for another reverse index slice. I made sure to assign it to a variable before confirming whether the input string and reversed index slice were equal or not. I concluded with a conditional statement to return the desired outputs predicated on the input_str being reversible in the form of a palindrome or not.

# It might not have been the most efficient approach. Using the Python in-built function 'reversed()' would have allowed me to complete the function in a single line. I just opted for another reverse index slice as I'm rather fond of them and would like to test their limits against the coding challenges in this Sprint.

# Considering my code utilizes a reverse index slice that is then validated by an if-else statement, my code doesn't run in a single step, not O(1), making it O(n), the same as the last function I wrote.

