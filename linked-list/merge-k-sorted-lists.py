# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKListsBruteForce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        nodes.sort()
        result = ListNode(0)
        cur = result
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return result.next

    # merge sort
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
