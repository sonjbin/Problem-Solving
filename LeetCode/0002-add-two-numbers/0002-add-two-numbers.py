# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while True:
            num1 = str(l1.val) + num1
            if not l1.next:
                break
            l1 = l1.next
        while True:
            num2 = str(l2.val) + num2
            if not l2.next:
                break
            l2 = l2.next
        num_sum = str(int(num1) + int(num2))
        num_sum = [int(d) for d in num_sum][::-1]
        root = ListNode(num_sum[0])
        curr = root
        for i in range(1, len(num_sum)):
            temp_node = ListNode(num_sum[i])
            curr.next = temp_node
            curr = temp_node
        
        return root



        