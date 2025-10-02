# Problem: InvertTree

# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy  

---

## Solution
## 1. Recursion
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        root.left, root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(n) for skewed trees, O(log n) for balanced trees [recursion stack]

## 2. BFS using double ended queue

- Append all elements into a queue, and invert each node from the left.
- We are using deque here instead of normal list and poping from the left because poping normal list from left involves shifting all the elements to the left, which is not ideal.
- deque.popleft() = O(1)

```python
# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(n) 