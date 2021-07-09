'''Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

Examples:

csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
Notes:

Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified input, in this case you should.
You should try using a "two-pointers approach".
Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to implement your own method).
'''

def csReverseString(chars):
    return chars[::-1]


# I had no difficulties at all. I simply recalled from class that we could index slice via [::] and then use -1 to perform the slicing from the back. Without the -1, it would default to performing the index slicing from the front, with 0.



# Index slicing with [::-1] is definitely the most efficient approach. It only takes one line of code to execute in just three steps. 

# Considering the slicing is being done twice and reversed, it isn't just one step, thus its time/space complexity can be denoted as O(n).