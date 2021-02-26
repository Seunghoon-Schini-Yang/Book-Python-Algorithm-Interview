from typing import List

test_case = [0, 1, 0, 2, 1, 0,
             1, 3, 2, 1, 2, 1]

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
        print(left_max, right_max)
        if left_max <= right_max:  # 왼쪽 최대 벽 높이 <= 오른쪽 최대 벽 높이
            volume += left_max - height[left]  # 물이 쌓일 수 있는 최대 높이에서, 밑에 쌓인 벽 높이 빼주기
            left += 1  # pointer 이동
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


print(trapping_water_sol1(test_case))