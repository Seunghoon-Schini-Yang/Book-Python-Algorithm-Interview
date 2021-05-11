# https://leetcode.com/problems/3sum/
# 리트코드 15. 3Sum
# 3개의 수 합해서 0 만드는 조합 찾기

from typing import List
from bisect import bisect_left  # 정렬된 리스트 탐색 -> 이진 탐색

test_1 = [-4, -1, -4, 0, 2, -2, -4, -3, 2, -3, 2, 3, 3, -4]
test_2 = [0, 0, 0]
test_3 = [-1, -1, -1]
test_4 = [-1, 0, 0, 0, 1, 2]
test_5 = [-1]


def three_sum_my(nums: List[int]) -> List[List[int]]:
    # initialize
    output = []
    i, j = 0, len(nums)

    # input list 길이 3보다 작을 경우
    if j < 3:
        return output

    # sort
    nums.sort()

    # 최대값이 0보다 작을 때
    if nums[j - 1] < 0:
        return output  # 빈 리스트 반환

    # 투 포인터 활용
    while nums[i] < 0:
        left = i + 1  # 왼쪽 포인터
        right = j  # 오른쪽 포인터
        while right > left + 1:
            sums = nums[i] + nums[left] + nums[right - 1]
            if sums == 0:  # 세 수 합 0일 때
                output.append([nums[i], nums[left], nums[right - 1]])  # output 추가
                right -= 1  # 오른쪽 포인터 왼쪽으로 한칸 이동
                while nums[right - 1] == nums[right]:  # if 이동 후 포인터 값 == 이동 전 포인터 값
                    right -= 1  # then 왼쪽으로 한칸 더 이동
            elif sums < 0:  # 세 수 합 0보다 작을 때
                # 왼쪽 포인터 이진탐색으로, 세 수 합 0 만드는 수 위치로 보이는 인덱스 이동
                left += bisect_left(nums[left:right-1], 0 - nums[i] - nums[right-1])
            else:  # 세 수 합 0보다 클 때
                # 오른쪽 포인터 이진탐색으로, 세 수 합 0 만드는 수 위치로 보이는 인덱스 이동
                right_2 = left + bisect_left(nums[left:right-1], 0 - nums[i] - nums[left]) + 1
                if right_2 == left + 1 and nums[left] == nums[left + 1]:
                    right_2 += 1  # if 왼쪽 포인터 == 오른쪽 포인터 and 왼쪽 값 == 왼쪽+1 값 then 오른쪽 포인터 += 1
                if right_2 == right:  # if 이동 후 인덱스 == 이동 전 인덱스
                    right_2 -= 1  # then 포인터 왼쪽으로 한 칸 이동
                right = right_2
        i += 1
        while nums[i] == nums[i-1]:
            i += 1

    # [0, 0, 0] 처리
    zero_cnt = 0  # initialize
    while zero_cnt < 3:  # 3되면 자동 종료
        if i == j:  # i 가 인덱스 범위 벗어나면
            break  # 종료
        elif nums[i] != 0:  # 포인터 값이 0이 아니면
            break  # 종료
        zero_cnt += 1
        i += 1
    if zero_cnt == 3:
        output.append([0, 0, 0])

    return output


def three_sum_sol2(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) -2):
        # 중복값 skip
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 포인터 간격 좁히기
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # 중복값 skip
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


print(three_sum_my(test_1))
print(three_sum_sol2(0, test_3))
