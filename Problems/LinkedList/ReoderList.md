# Problem: ReoderList

# Link: https://leetcode.com/problems/reorder-list/
# Difficulty: Medium  

---

## Solution
1. Brute Force but beats 100% in leetcode:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        store = []

        i = head
        while i:
            store.append(i)
            i = i.next

        l, r = 0, len(store) - 1
        this = None
        while l < r:
            store[l].next = store[r]
            l += 1
            if l == r:
                break
            store[r].next = store[l]
            r -= 1
        store[l].next = None
    
        return head        
```
## Notes
- Approach:
- Time Complexity:O(n) + O(n) = O(n)
- Space Complexity: O(n) (Array)

2. slow/fast pointers
   1. use slow fast pointers and find the middle node
   2. reverse teh second half
   3. merge 1st half and 2nd half alternatively
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        p = None
        c = slow.next
        slow.next = None

        while c:
            temp = c.next
            c.next = p
            p = c
            c = temp
        
        l = head
        r = p

        while l and r:
            temp1 = l.next
            temp2 = r.next
            l.next = r
            r.next = temp1
            r = temp2
            l = temp1
        
        return head
```

Time Complexity : O(n)
space Complexity : O(1)