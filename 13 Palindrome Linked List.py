# https://leetcode.com/problems/palindrome-linked-list/
# 리트코드 234. Palindrome Linked List
# 연결 리스트 개념 익히는 문제

from typing import List, Deque
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PalindromeLinkedList:
    @staticmethod
    def sol_my(head: ListNode) -> bool:
        pass

    @staticmethod
    def sol_list(head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    @staticmethod
    def sol_deque(head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    @staticmethod
    def sol_runner(head: ListNode) -> bool:
        rev = None
        slow = fast = head  # slow, fast 둘 다 head 로 할당

        while fast and fast.next:  # fast runner 가 끝에 도착할때까지 반복
            fast = fast.next.next  # 노드 2 개씩 run
            rev, rev.next, slow = slow, rev, slow.next  # 다중 할당 (Multiple Assignment)

        if fast:  # 홀수 개일 때 slow runner 앞으로 한 칸 더
            slow = slow.next

        # palindrome 체크
        while rev and slow.val == rev.val:
            rev, slow = rev.next, slow.next

        return not rev


a = PalindromeLinkedList()

node2 = ListNode(2)
node1 = ListNode(1, node2)


print(a.sol_list(node1))
print(a.sol_deque(node1))
print(a.sol_runner(node1))

node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print(a.sol_list(node1))
print(a.sol_deque(node1))
print(a.sol_runner(node1))
