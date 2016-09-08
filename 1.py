"""
Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True.
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""
def is_anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    return s1 == s2

def anagram_finder(s, t):
    match_length = len(t)
    pattern_length = len(s)
    for i in range(pattern_length - match_length + 1):
        #print (s[i: i+match_length], t)
        if is_anagram(s[i: i+match_length], t):
            return True
    return False

print anagram_finder("udacity", "cityuda")
