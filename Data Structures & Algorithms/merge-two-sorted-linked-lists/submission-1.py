# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # starting node (fake head)
        tail = dummy

        while list1 and list2:
            # if list1 value is smaller, add it to the end of the list
            if list1.val < list2.val:
                tail.next = list1  # add to the list
                list1 = list1.next # move list1 pointer forward
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # move tail forward
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
        
