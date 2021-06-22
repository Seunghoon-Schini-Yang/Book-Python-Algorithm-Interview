# https://leetcode.com/problems/product-of-array-except-self/
# 리트코드 238. Product of Array Except Self
# 자기 자신 제외한 요소 곱셈 반환 (조건 : 나눗셈 안하고 O(n)에 풀어라)

from typing import List

test_case = [1, 2, 3, 4]


class ProductOfArrayExceptSelf:
    @staticmethod
    def sol_my(nums: List[int]) -> List[int]:
        left_out = [1]
        for i in nums[:-1]:
            left_out.append(i * left_out[-1])

        p = 1
        for i in range(len(nums) - 1, 0, -1):
            p *= nums[i]
            left_out[i - 1] *= p

        return left_out

    @staticmethod
    def sol1(nums: List[int]) -> List[int]:
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


a = ProductOfArrayExceptSelf
print(a.sol_my(test_case))
print(a.sol1(test_case))
