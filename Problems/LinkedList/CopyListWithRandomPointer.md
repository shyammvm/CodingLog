# Problem: CopyListWithRandomPointer

# Link: https://leetcode.com/problems/copy-list-with-random-pointer
# Difficulty: Medium  

---

## Solution

### 1. with O(n) space complexity using hashmap and 2 passes

Example:
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ref = {}

        curr = head
        while curr:
            ref[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                ref[curr].next = ref[curr.next]
            if curr.random:
                ref[curr].random = ref[curr.random]
            curr = curr.next
        
        return ref[head]
```

---

## Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(n)

### 2. With O(1) space complexity but 3 passes
1.  Clone nodes and interleave them
    1.  For each original node, create a copy and insert it right after the original.
2.  Assign random pointers
    1.  Now, for each original node curr, its copy is curr.next.
    2.  curr.random.next will be the copied version of curr.random.
3.  Separate the two lists

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = curr.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return copy_head
```
## Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(1)

