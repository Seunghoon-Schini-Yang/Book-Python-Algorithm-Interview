# https://leetcode.com/problems/product-of-array-except-self/
# 리트코드 238. Product of Array Except Self
# 자기 자신 제외한 요소 곱셈 반환 (조건 : 나눗셈 안하고 O(n)에 풀어라)

from typing import List

test_case = [1, 2, 3, 4]


def product_except_self_my(nums: List[int]) -> List[int]:
    left_out = [1]
    for i in nums[:-1]:
        left_out.append(i * left_out[-1])

    p = 1
    for i in range(len(nums) - 1, 0, -1):
        p *= nums[i]
        left_out[i - 1] *= p

    return left_out


def product_except_self_sol1(nums: List[int]) -> List[int]:
    out = []
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


print(product_except_self_my(test_case))
print(product_except_self_sol1(test_case))
