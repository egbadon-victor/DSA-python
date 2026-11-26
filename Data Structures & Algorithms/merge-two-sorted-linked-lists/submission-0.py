# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        head = None
        curr = None

        while curr1 or curr2:
            next = None
            if not curr1:
                next = curr2
                curr2 = curr2.next
            elif not curr2:
                next = curr1
                curr1 = curr1.next
            elif curr1.val <= curr2.val:
                next = curr1
                curr1 = curr1.next
            else:
                next = curr2
                curr2 = curr2.next

            if not head:
                head = next
            
            if curr:
                curr.next = next
            curr = next
            curr.next = None
    
        return head


            

            
        