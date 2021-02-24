# https://leetcode.com/problems/trapping-rain-water/
# 리트코드 42. Trapping Rain Water

from typing import List

test_case = [0, 1, 0, 2, 1, 0,
             1, 3, 2, 1, 2, 1]


# two pointer 활용 - 1층 부터 한 층씩 지워가며 탐색
def trapping_water_my(height: List[int]) -> int:
    if not height:  # 빈 list 일 경우
        return 0

    left = 0
    right = len(height) - 1
    water_cnt = 0

    while left != right:  # two pointer 가 서로 만나기 전까지
        while height[left] == 0:  # value 가 0이 아닐 때까지 left pointer 전진
            left += 1
        while height[right] == 0:  # value 가 0이 아닐 때까지 right pointer 후진
            right -= 1

        for i in range(left, right + 1):  # left 부터 right index 까지 탐색
            if height[i] == 0:  # 값이 0 이면, water_cnt 에 1 추가
                water_cnt += 1
            else:
                height[i] -= 1  # 값이 0 이 아니면, i index 에 해당하는 value 1 감소
    return water_cnt


print(trapping_water_my(test_case))
