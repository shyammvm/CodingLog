# Problem: RemoveNthNodeFromTheEndOfList

# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Difficulty: Medium  

---

## Solution
### Using an extra array:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None

        i = head
        ref = []
        while i:
            ref.append(i)
            i = i.next

        
        if n == len(ref):
            head = ref[1]

        elif n == 1:
            ref[-2].next = None
        
        else:
            ref[len(ref) - n - 1].next = ref[len(ref) - n + 1]

        return head

```

---

## Notes
- Approach: Using array
- Time Complexity: O(n)
- Space Complexity: O(n)


### Using 2 pointers:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
```
1. create a dummy before head so that even if we move n + 1 times from dummy we only reach None
2. move fast n + 1 times ahead
3. now move both fast and slow until fast is None
4. at this point slow is exactly n behind and is the node left to the node to be removed.
5. Now just assign slow.next to slow.next.next

## Notes
- Approach: Using array
- Time Complexity: O(n)
- Space Complexity: O(1)
