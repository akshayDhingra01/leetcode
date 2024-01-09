# https://leetcode.com/problems/merge-two-sorted-lists/

# First Optimized Solution || Time O(N) || Space O(1) || Linked List

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if curr1 == None:
            return curr2
        if curr2 == None:
            return curr1
        head_main = curr1 if curr2.val > curr1.val else curr2
        if curr2.val > curr1.val:
            curr1 = curr1.next
        else:
            curr2 = curr2.next
        prev_head = head_main
        while curr1 and curr2:
            if curr1.val > curr2.val:
                prev_head.next  = curr2
                prev_head = curr2
                curr2 = curr2.next
            else:
                prev_head.next = curr1
                prev_head = curr1
                curr1 = curr1.next
        if curr1 == None:
            prev_head.next = curr2
        else:
            prev_head.next = curr1
        return head_main