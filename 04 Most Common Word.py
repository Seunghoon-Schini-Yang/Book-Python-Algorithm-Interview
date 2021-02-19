# https://leetcode.com/problems/most-common-word/
# 리트코드 819. Most Common Word

from typing import List
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# hit 을 제외하고 가장 많이 사용된 word 찾기


def most_common_word_my(sentence: str, ban: List[str]) -> List[str]:  # 가장 많이 사용된 word 모두 찾기 -> list 로 반환
    sentence = re.sub('[^a-z ]', '', sentence.lower())  # a-z 뒤에 공백 존재 이유 : 공백 남겨놔야 word 간 구별 가능
    word_list = sentence.split()
    word_set = set()
    word_dict = dict()

    for word in word_list:
        if word in ban:  # ban 안에 들어있는 word 일 경우 다음 루프 진행
            continue
        elif word in word_set:  # word_set 안에 들어있는 word 일 경우 해당 word 를 키로 가지는 word_dict[word] 값 1 증가
            word_dict[word] += 1
        else:  # word_set 에 없는 경우 추가하고, word_dict 키 생성 후 값으로 1 설정
            word_set.add(word)
            word_dict[word] = 1

    max_num = max(word_dict.values())  # 가장 많이 사용된 word 의 출현 횟수
    most_common_words = []

    for word, value in word_dict.items():
        if value == max_num:
            most_common_words.append(word)

    return most_common_words


print(most_common_word_my(paragraph, banned))  # ['ball']


def most_common_word_sol1(sentence: str, ban: List[str]) -> str:  # 'list comprehension', 'defaultdict', 'Counter'
    words = [word for word in re.sub(r'[^\w]', ' ', sentence)  # regex 에서 'r' : raw strings - ignore escapes
             .lower().split()
             if word not in ban]

    '''
    counts = collections.defaultdict(int)  # 기본값 0
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)  # value 가 가장 큰 key 반환, dict.get 는 lambda x: dict[x] 와 같은 효과
    '''

    counts = collections.Counter(words)
    # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
    return counts.most_common()[0][0]


print(most_common_word_sol1(paragraph, banned))  # ball
