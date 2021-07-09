'''
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
'''

def csRemoveDuplicateWords(input_str):
    # Convert input_str to list. Split on whitespace for each word, then use 'is in' to check if that word has been used or not
    words = input_str.split()
    unique = []
    
    for i in words:
        if i not in unique:
            unique.append(i)
    
    # Using join function with a string containing one whitespace to return my list of unique words
    return ' '.join(unique)

# I converted the input_str to a list with the .split() function, which split each word from one another on whitespace. I followed that up with a for loop, where I utilized an if statement with the 'is in' operator to confirm whether the words had been used once before or not before returning a list of unique characters that was then converted into a string with the join method.

# The only difficulty I had was in remember to use 'in' for my for loop. Totally slipped my mind. 

# This was the simplest way I could manage to return the desired output. It would take far longer than the time this Sprint Challenge has allotted to refactor.

# My algorithm is has a complexity of O(n). Nothing but constants. Doesn't logarithmically scale in proportion to outputs.