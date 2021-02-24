# https://leetcode.com/problems/two-sum/
# 리트코드 1. Two Sum

from typing import List
test_case = [2, 7, 11, 15]
test_target = 9


# Brute-Force
# O(n^2)
def two_sum_my(nums: List[int], target: int) -> tuple:  # two_sum_sol1 과 거의 같음
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


print(two_sum_my(test_case, test_target))  # (0, 1)


# enumerate, in 활용
# O(n^2) - 시간복잡도는 이중 for 문인 my 와 같지만, python 내부 함수인 in 활용이 상수항이 훨씬 작아서 빠름
def two_sum_sol2(nums: List[int], target: int) -> tuple:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + i + 1
    return ()


print(two_sum_sol2(test_case, test_target))  # (0, 1)


# dictionary 활용
# hash table 인 dict 에서의 조회 -> 분활 상환 분석 : O(1)
# O(n)
def two_sum_sol3(nums: List[int], target: int) -> tuple:
    nums_map = dict()
    for i, num in enumerate(nums):
        nums_map[num] = i  # key 를 value, value 를 index 로 하는 dict 생성

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:  # 자기 자신 찾는 것 방지
            return i, nums_map[target - num]
    return ()


print(two_sum_sol3(test_case, test_target))  # (0, 1)


# sol3 과 비교해 for 문 하나로 통합 -> 더 간결한 code
# O(n)
def two_sum_sol4(nums: List[int], target: int) -> tuple:
    nums_map = dict()
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return nums_map[target - num], i
        nums_map[num] = i
    return ()


print(two_sum_sol4(test_case, test_target))


# two pointer : O(n)
# Tim sort : O(nlogn)
# 문제가 index 반환을 요구하기 때문에, 입력이 sorted list 가 아니면 사용 불가
def two_sum_sol5(nums: List[int], target: int) -> tuple:
    nums.sort() # 먼저
    left = 0
    right = len(nums) - 1
    while right > left:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right
    return tuple()


print(two_sum_sol5(test_case, test_target))
