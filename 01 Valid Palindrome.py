# https://leetcode.com/problems/valid-palindrome/
# 리트코드 125. Valid Palindrome

pal = "A man, a plan, a canal: Panama"


def is_palindrome_sol1(s: str) -> bool:  # 'list'
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_sol2(s: str) -> bool:  # 'deque'
    from typing import Deque  # 변수 선언을 위한 module
    import collections

    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_sol3(s: str) -> bool:  # 'slicing'
    import re
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)  # regular expressions

    return s == s[::-1]  # reverse


print(is_palindrome_sol1(pal))
print(is_palindrome_sol2(pal))
print(is_palindrome_sol3(pal))
