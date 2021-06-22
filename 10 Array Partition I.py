# https://leetcode.com/problems/array-partition-i/
# 리트코드 561. Array Partition I
# n개의 페어로 만들 수 있는 min(a, b) 합 최대값

from typing import List

test_case = [1, 4, 3, 2]


def array_partition_i_my(input_list: List[int]) -> int:
    input_list.sort()  # 정렬
    sum_tot, n = 0, 0  # sum_tot : min 총합, n : pair 수
    i = len(input_list) - 2
    while i >= 0:
        sum_tot += input_list[i]
        n += 1
        i -= 2
    return n, sum_tot


def array_partition_i_sol2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


def array_partition_i_sol3(nums: List[int]) -> int:
    # pythonic way
    return sum(sorted(nums)[::2])


print(array_partition_i_my(test_case))
print(array_partition_i_sol2(test_case))
print(array_partition_i_sol3(test_case))
