# laboratory

import collections
from typing import List
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
def most_common_word_sol1(sentence: str, ban: List[str]) -> List[str]:  # 'list comprehension', 'defaultdict', 'Counter'
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
    print(counts)

most_common_word_sol1(paragraph,banned)