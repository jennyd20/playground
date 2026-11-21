#!/usr/bin/env python3

from itertools import groupby

# Example whiteboard problems
# https://dev.to/karlybl/whiteboard-coding-interview-questions-tips-examples-and-solutions-4i1m


################################################################################
# 1. Reverse a string
# Problem: Write a function that reverses a string. For example, “hello” should
# become “olleh”.
def reverse_string(s):
    """Reverse an input string"""
    return s[::-1]


assert reverse_string("hello") == "olleh"
assert reverse_string("") == ""


################################################################################
# 2. Palindrome
# Problem: Determine if a string is a palindrome. A string is a palindrome if it
# reads the same backward as forward. For example, "madam" and "racecar" is a
# palindrome, while "banana" is not.
def is_palindrone(s):
    """Return true if the string is a palindrome"""
    return s == s[::-1]


assert is_palindrone("racecar")
assert not is_palindrone("banana")


################################################################################
# 3. FizzBuzz
# Problem: Write a function that prints the numbers from 1 to 100. For multiples
# of three, print "Fizz" instead of the number. For multiples of five, print
# "Buzz" instead of the number. For numbers which are multiples of both three
# and five, print "FizzBuzz" instead of the number.
def fizzbuzz():
    """FizzBuzz"""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz()

################################################################################
# 4. First non-repeating character
# Problem: Find the first non-repeating character in a string
# Note: in the _whole_ string, not just adjacent characters

# # For each char in the string, see if the count of that char in the string is
# # exactly 1. O(n^2)
# def non_repeated(s):
#     """ Return first non-repeating char in a string """
#     for i in range(len(s)):
#         if s.count(s[i]) == 1:
#             return s[i]
#     return "" # or, return None

# # Using enumerate rather than range(len())
# def non_repeated(s):
#     """ Non-repeating char using enumerate """
#     for i, char in enumerate(s):
#         if s.count(char) == 1:
#             return char
#     return ""


# Skipping range(len()) and just using for (char) in (str) notation
def non_repeated(s):
    """Non-repeating char using just i in str"""
    for c in s:
        if s.count(c) == 1:
            return c
    return ""


assert non_repeated("abcba") == "c"
assert non_repeated("aabbcde") == "c"
assert non_repeated("aabbcc") == ""

# Better time complexity options (O(n)):
# - Create a map of characters and their counts. Creating a dictionary preserves
#   insertion order
#   - Option 1: use collections.count (faster, uses compiled C)
#   - Option 2: iterate over the string using a standard Python for loop
# - Iterate over the dict in order to find the first char whose count is 1
# - Note: could also iterate back through the string and do a dictionary lookup,
#   but there's no advantage to doing so when dict preserves order.


################################################################################
# 5. Find the missing number
# Problem: Given an array of n-1 integers in the range of 1 to n, find the
# missing number.

# # Approach #1 (naive): given a sorted list of numbers, see which is missing
# from the array
# # This is O(n^2)
# def missing_num(num_array):
#     """ Find the missing number in an array of size n """
#     for i in range(1, len(num_array) + 1):
#         if i not in num_array:
#             return i
#     return None

# Approach #2: use a hash array. Create a hash array of the size of the full
# range (O(1)), then go through the original array once and count the instances
# of each value. Then go through the hash array once and find the value with 0
# instances.
# NOT IMPLEMENTED HERE


# Approach #3 (better): Calculate the expected sum of the values and find what
# is missing from the actual sum. O(n)
def missing_num(num_array):
    """Find the number missing from an array of numbers 1-n"""
    # FOR EXPECTED SUM: THIS IS WRONG DON'T DO IT THIS WAY
    # expected_sum = sum(range(1, len(num_array) + 2))
    # DO IT THIS WAY
    n = len(num_array) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num_array)
    return expected_sum - actual_sum


assert missing_num([1, 2, 4, 5]) == 3
assert missing_num([9, 5, 3, 1, 8, 6, 4, 2]) == 7


# Approach #4: XOR operation. I admit, it is harder for me to grok using the
# bitwise operator. The basic underlying component is that a number XORed with
# itself is zero, so if you XOR the two lists together everything that matches
# cancels out and leaves just the missing number behind.
def missing_num_xor(num_array):
    """
    XOR the value of the full array and the input array to find what doesn't get
    cancelled out
    """
    xor_input = 0
    xor_expected = 0

    # xor the input array
    for i in num_array:
        xor_input ^= i

    # xor the the full array
    for i in range(1, len(num_array) + 2):
        xor_expected ^= i

    # Missing number is whatever is left over after xoring those together
    return xor_input ^ xor_expected


assert missing_num_xor([1, 2, 4, 5]) == 3
assert missing_num_xor([9, 5, 3, 1, 8, 6, 4, 2]) == 7


# Compressed approach with enumerate. Since enumerate gives the index, which is
# a shortcut to get the numbers in the full array, we can just use that as the
# comparison array.
def missing_num_xor_mask(num_array):
    """Use enumerate against a list of indices (1 - n)"""
    # Starting at 1 and going to full non-missing array length, which is input
    # array len + 1. This is the final value that would be missing from the
    # enumerate.
    x = len(num_array) + 1

    for i, num in enumerate(num_array, 1):
        x ^= i ^ num
    return x


assert missing_num_xor_mask([1, 2, 4, 5]) == 3
assert missing_num_xor_mask([9, 5, 3, 1, 8, 6, 4, 2]) == 7


################################################################################
# 6. Counting duplicates
# Problem: Given a string, return the count of the number of duplicates.
# NOTE: The goal of the function isn’t to count the number of repeat characters
# but to count the number of characters that have duplicates.


# Approach #1: alphebetize the (lower-cased) string, divide letters into groups,
# count the number of groups that have more than one member
def count_duplicated_letters(s):
    """Count how many characters in the string have any number of duplicates"""
    # Start by sorting the string alphabetically
    sorted_input = sorted(s.lower())
    # Advance through each group until the character is different, add 1 to the
    # final answer if that group has more than one item

    # NOT KNOWING ABOUT THE PYTHON LIBRARY, here's an awkward manual
    # implementation of grouping and counting within each group
    group_c = sorted_input[0]
    duplicate = False
    ans = 0
    for c in sorted_input[1:]:
        if c != group_c:
            group_c = c
            duplicate = False
        elif not duplicate:
            ans += 1
            duplicate = True
    return ans

    # # OTHER OPTION USING PYTHON LIBRARY: itertools.groupby
    # # Add another to the sum if the length of the iterator (found by converting
    # # the iterator items to a list and then checking that length) is greater
    # # than one.
    # return sum(1 for _, g in groupby(sorted_input) if len(list(g)) > 1)


assert count_duplicated_letters("abcde") == 0
assert count_duplicated_letters("aabbcde") == 2
assert count_duplicated_letters("aabBcde") == 2
assert count_duplicated_letters("indivisibility") == 1
assert count_duplicated_letters("Indivisibilities") == 2
assert count_duplicated_letters("aA11") == 2
assert count_duplicated_letters("ABBA") == 2

# Other approaches:
# - Use collections.Counter: create a dictionary of keys (characters) to
#   frequency (count in the string), then count the dictionary keys with a
#   value greater than 1
# - Build a frequency map over the string
# - Use two sets: add a character to one set the first time it is seen, then
#   add it to a separate set if it already exists in the first set. This uses
#   a single pass on the input
# - Bitmask Tracking: Create a 26 character long binary number bitmap where each
#   position corresponds to a letter.  Create two binary numbers, "seen" and
#   "dupe", each starting at 000...000. For each char in the string, apply that
#   bitmap to "seen". Use bitwise AND to determine if the bit is already flipped
#   in "seen" - if so, flip that bit in "dupe". Otherwise, flip the bit in
#   "seen". At the end of the string, each bit in "dupe" corresponds to a letter
#   that had more than one instance, and the result is dupe.bit_count(). NOTE:
#   this gets more complicated if including non-alpha characters.


################################################################################
# 7. Fibonacci sequence
# Problem: Write a function that calculates the nth Fibonacci number. Fibonacci
# is a sequence of numbers where each number is the sum of the two preceding
# numbers, starting from 0 and 1. The sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21,
# 34, and so on. In this problem, you should return the nth number in the
# Fibonacci sequence. So if the input is 1, the output should be 0, because 0 is
# the first number in the Fibonacci sequence.


################################################################################
# 8. Two Sum
# Problem: Given an array of integers, return indices of the two numbers such
# that they add up to a specific target.


################################################################################
# 9. Armstrong
# Problem: Write a function that determines if a number is an Armstrong number -
# the sum of each digit raised to the number's length is equal to the number
# itself.


################################################################################
# 10. Remove duplicates
# Problem: Remove duplicate members of an array.
