# https://leetcode.com/problems/group-anagrams/
# 리트코드 49. Group Anagrams

from typing import List
import collections

# Anagrams : ex) ['eat', 'ate', 'tea']
test_case = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams_my(words: List[str]) -> List[List[str]]:
    default_dict = collections.defaultdict(list)  # empty list 를 default value 로 갖는 defaultdict

    for word in words:
        counter = tuple(
            sorted(collections.Counter(word).items(), key=lambda x: x[0])
            # dict is unhashable -> dict key 로 사용될 수 없음
        )  # sorted(*) -> list -> unhashable -> tuple 로 변환 -> hashable -> dict key 로 사용 가능
        default_dict[counter].append(word)

    return list(default_dict.values())


print(group_anagrams_my(test_case))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def group_anagrams_sol1(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        # sorted('eat') = ['a', 'e', 't']
        # ''.join(['a', 'e', 't']) = 'aet'

    return list(anagrams.values())  # list 변환하지 않으면, dict_value object 반환


print(group_anagrams_sol1(test_case))
