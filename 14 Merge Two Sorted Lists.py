# https://leetcode.com/problems/merge-two-sorted-lists/
# 리트코드 21. Merge Two Sorted Lists
# 정렬된 2개의 연결 리스트 정렬되게 병합하기


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedLists:
    @staticmethod
    def sol_my(head1: ListNode, head2: ListNode) -> ListNode:
        pass

    @staticmethod
    def sol_recursive(l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = MergeTwoSortedLists.sol_recursive(l1.next, l2)
        return l1

    @staticmethod
    def check_result(result: ListNode) -> bool:
        while result.next:
            if result.val > result.next.val:
                return False
            result = result.next
        return True


test_case_1 = ListNode(1, ListNode(2, ListNode(4, None)))
test_case_2 = ListNode(1, ListNode(3, ListNode(4, None)))

ans = MergeTwoSortedLists.sol_recursive(test_case_1, test_case_2)
print(MergeTwoSortedLists.check_result(ans))
