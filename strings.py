#!/usr/bin/env python3
"""
Kenzie assignment: Strings!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Shavonne Carson"

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Example:
#   donuts(5) returns 'Number of donuts: 5'
#   donuts(23) returns 'Number of donuts: many'


def donuts(count):
    # your code here
    x =''
    if count< 10:
        x = 'Number of donuts: ' + str(count)
    else:
        x = 'Number of donuts: Many'
    
    print(x) 

donuts(4)
donuts(14)


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 characters of the original string.
# However, if the string length is less than 2, return
# an empty string instead.
# Example:
#   'spring' -> 'spng'



def both_ends(s):
    # your code here
    print(s[0:2] + s[-2:])
    # return
both_ends('spring')


# C. fix_start
# Given a string s, return a string where all occurrences
# of its first character have been changed to '*', except
# do not change the first character itself.
# Example:
#   'babble' -> 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    # your code here
    y = s.replace(s[:1], '*')
    x = s[:1]+ y[1:]

    print(x)


fix_start('babble')

# D. mix_up
# Given strings a and b, return a single string with a and
# b separated by a space '<a> <b>', except swap the first
# 2 characters of each string.
# Example:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    # your code here
    x = a[0:2]+ b[2:]
    y = b[0:2] + a[2:]
    

    print(x + ' ' + y)

mix_up('space', 'paul')


# E. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    # your code here
    x= s[-3:]
    y = 'ing'
    print(s)
    # print(x)
    if len(s)< 3:
        print(s+'ly')
    elif len(s) > 3:
        if x == y:
            print(s)
        else:
            print(s+y)
# come back and do a check to see if last letter is vowel
verbing('space')
verbing('spacing')
verbing('it')


# F. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'


def not_bad(s):
    # your code here
    is_bad = 'bad'
    is_not = 'not'

    if s.index(is_bad) > s.index(is_not):
        print(s.replace(s[s.index(is_not):s.index(is_bad)+3], 'good'))
    else:
        print(s)


not_bad('This dinner is not that bad!')
not_bad('She is giving off not bad vibes.')
not_bad('Trying bad before not.')

# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the extra
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back


def front_back(a, b):
    # your code here
    len_of_a = len(a)
    half_of_a = len_of_a//2

    len_of_b = len(b)
    half_of_b = len_of_b//2

    if len_of_a and len_of_b % 2 == 0:
        print(a[:half_of_a]+b[:half_of_b]+ ' ' +a[half_of_a:]+b[half_of_b:])
    else:
        print(a[:half_of_a+1]+b[:half_of_b+1]+ ' ' +a[1+half_of_a:]+b[1+half_of_b:])



front_back('hello', 'world')
front_back('bad', 'ideas')