# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode()
        c = d
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c=c.next
        if list1 is not None:
            c.next = list1
        elif list2 is not None:
            c.next = list2
        return d.next