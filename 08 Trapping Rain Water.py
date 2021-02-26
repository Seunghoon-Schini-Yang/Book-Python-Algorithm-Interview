# https://leetcode.com/problems/trapping-rain-water/
# 리트코드 42. Trapping Rain Water

from typing import List

test_case = [0, 1, 0, 2, 1, 0,
             1, 3, 2, 1, 2, 1]


# two pointer 활용 - 1층 부터 한 층씩 지워가며 탐색
# O(n^2) 이상 ?
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


print(trapping_water_my(test_case))  # 6
print(test_case)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

test_case = [0, 1, 0, 2, 1, 0,
             1, 3, 2, 1, 2, 1]


# two pointer
# O(n)
def trapping_water_sol1(height: List[int]) -> int:
    if not height:  # empty list 일 경우 0 반환
        return 0
    # 초기값 설정
    volume = 0
    left, right = 0, len(height) - 1  # 각 pointer 초기 index 설정
    left_max, right_max = height[left], height[right]  # 초기 최대 벽 높이

    while left < right:  # two pointer 가 서로 만나기 전까지만 반복
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:  # 왼쪽 최대 벽 높이 <= 오른쪽 최대 벽 높이
            volume += left_max - height[left]  # 물이 쌓일 수 있는 최대 높이에서, 밑에 쌓인 벽 높이 빼주기
            left += 1  # pointer 이동
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


print(trapping_water_sol1(test_case))  # 6


# stack
# O(n)
def trapping_water_sol2(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점
        # stack 이 not empty 하고, 현재 index 블록 높이가 이전 index 보다 높을 때
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not stack:  # if stack is empty -> break
                break

            distance = i - stack[-1] - 1  # 벽 사이의 거리
            waters = min(height[i], height[stack[-1]]) - height[top]  # 양끝 벽 중 낮은 벽 높이 - 양끝 벽 사이 가장 높은 벽 높이

            volume += distance * waters

        stack.append(i)
    return volume


print(trapping_water_sol2(test_case))  # 6
