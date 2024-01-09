# https://leetcode.com/problems/reverse-linked-list/

# First Optimized Solution || Time O(N) || Space O(1) || Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        if head.next is None:
            return head
        previousNode = head
        curr = head.next
        head.next = None
        while curr.next != None:
            newCurr = curr.next
            curr.next = previousNode
            previousNode = curr
            curr = newCurr

        curr.next = previousNode
        return curr
