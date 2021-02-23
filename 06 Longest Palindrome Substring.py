# https://leetcode.com/problems/longest-palindromic-substring/
# 리트코드 5. Longest Palindrome Substring

test_case_1 = "bzabadabab"
test_case_2 = "abcdddd"


# 가장 긴 palindrome string 찾기
def longest_palindrome_my(string: str) -> str:
    length = len(string)
    max_longest = 1  # 가장 긴 palindrome 철자 개수
    longest_palindrome = string[0]  # 가장 긴 palindrome
    i = 1

    # 홀수 개 탐색
    while i < length - (max_longest + 1) / 2:
        j = 1
        while i-j >= 0 and i+j < length:
            if string[i-j] != string[i+j]:
                break
            else:
                j += 1
        if max_longest < j*2 - 1:
            max_longest = j*2 - 1
            longest_palindrome = string[i-j+1:i+j]
        i += 1

    i = 1

    # 짝수 개 탐색
    while i < length - (max_longest - 1) / 2:
        j = 1
        if string[i-1] == string[i]:
            while i-j >= 1 and i+j < length:
                if string[i-j-1] != string[i+j]:
                    break
                else:
                    j += 1
            if max_longest < j*2:
                max_longest = j*2
                longest_palindrome = string[i-j:i+j]
        i += 1

    return longest_palindrome


print(longest_palindrome_my(test_case_1))  # 'abadaba'
print(longest_palindrome_my(test_case_2))  # 'dddd'


def longest_palindrome_sol1(s: str) -> str:
    # two pointer
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    # 특이 케이스 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # sliding window 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),  # 홀수 개 경우
                     expand(i, i + 2),  # 짝수 개 경우
                     key=len)
    return result


print(longest_palindrome_sol1(test_case_1))  # 'abadaba'
print(longest_palindrome_sol1(test_case_2))  # 'dddd'
