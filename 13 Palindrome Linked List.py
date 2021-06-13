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
        rev = None  # reversed linked list
        slow = fast = head  # 두 개의 runner (init은 처음 값으로)

        while fast and fast.next:  # fast running (slow runner가 딱 연결 리스트 중간까지 도달하도록 함)
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:  # 연결리스트가 홀수의 원소를 갖는 경우, 가운데 원소를 palindrome 체크에서 배제하도록 함.
            slow = slow.next

        # palindrome 여부 체크
        while rev and slow.val == rev.val:
            rev, slow = rev.next, slow.next

        return not rev


a = PalindromeLinkedList()

head2 = ListNode(2)
head1 = ListNode(1, head2)

print(a.sol_list(head1))
print(a.sol_deque(head1))

ward1 = ListNode(1)
ward2 = ListNode(2, ward1)
node2 = ListNode(2, ward2)
node1 = ListNode(1, node2)

print(a.sol_list(node1))
print(a.sol_deque(node1))
