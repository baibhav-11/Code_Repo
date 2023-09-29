# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []  # Store values of nodes
        
        # Traverse the linked list and store values
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Use two pointers to compare values from both ends
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True