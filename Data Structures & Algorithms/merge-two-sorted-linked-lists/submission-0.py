# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # while the two lists both have values to compare
        while list1 and list2:
            if list1.val < list2.val:
                # add list1 node to the sorted list
                tail.next = list1
                # move the list1 pointer forward
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # we need to account for 1 list being longer than the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next