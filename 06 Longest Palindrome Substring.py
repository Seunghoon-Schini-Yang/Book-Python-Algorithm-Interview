# https://leetcode.com/problems/longest-palindromic-substring/
# 리트코드 5. Longest Palindrome Substring

test_case_1 = "bzabadabab"
test_case_2 = "abcdddd"


# 가장 긴 palindrome string 찾기
def longest_palindrome_substring_my(string: str) -> str:
    length = len(string)
    max_longest = 1
    longest_palindrome = string[0]
    i = 1

    while i < length - (max_longest + 1) / 2:  # 홀수 개 탐색
        j = 1
        while i - j >= 0 and i + j < length:
            if string[i - j] != string[i + j]:
                break
            else:
                j += 1
        if max_longest < j * 2 - 1:
            max_longest = j * 2 - 1
            longest_palindrome = string[i - j + 1:i + j]
        i += 1

    i = 1

    while i < length - (max_longest - 1) / 2:  # 짝수 개 탐색
        j = 1
        if string[i - 1] == string[i]:
            while i - j >= 1 and i + j < length:
                if string[i - j - 1] != string[i + j]:
                    break
                else:
                    j += 1
            if max_longest < j * 2:
                max_longest = j * 2
                longest_palindrome = string[i - j:i + j]
        i += 1

    return longest_palindrome


print(longest_palindrome_substring_my(test_case_1))
print(longest_palindrome_substring_my(test_case_2))


def longest_palindrome_substring_sol1():
    return 1
