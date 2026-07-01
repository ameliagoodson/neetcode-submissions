# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            nextNode = current.next #store link to next node
            current.next = prev # reverse
            prev = current # move previous forward
            current = nextNode # move current forward
        return prev
            # need to store the way of traversing the list

            
        