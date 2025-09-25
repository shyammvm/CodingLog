# Problem: Add Two Numbers 

# Link: https://leetcode.com/problems/add-two-numbers/description/
# Difficulty: Medium  

---
### 1. Brute force but beats 100% in leetcode due to python c optimisation when it comes to integer operation. But not recommended for large lists.

```python
## Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ''
        while l1:
            s = str(l1.val) + s
            l1 = l1.next
        num1 = int(s)
        s = ''
        while l2:
            s = str(l2.val) + s
            l2 = l2.next
        num2 = int(s)
        res = num1 + num2
        s = str(res)
        head = ListNode((int(s[-1])))
        prev = head
        for i in range(len(s) - 2, -1, -1):
            this = ListNode(int(s[i]))
            prev.next = this
            prev = this

        return head      
```

#### Notes
- Approach: iterating both lists and storing number in string, convert to int for addition and then back to string for creating the output list.
- Time Complexity: O(n² + m²) --not good
- Space Complexity: O(n + m) --not good
  
### 2. Without extra space and only one iteration
(Only beats 54% in leetcode, but is the best approach if there too many nodes.)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            this = v1 + v2 + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = this // 10
            digit = this % 10

            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next

```
#### Notes
- Approach: iterating both lists and storing number in string, convert to int for addition and then back to string for creating the output list.
- Time Complexity: O(n) 
- Space Complexity: O(n)
---

