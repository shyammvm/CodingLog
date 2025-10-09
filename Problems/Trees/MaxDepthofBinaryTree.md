# Problem: MaxDepthofBinaryTree

# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy  

---

## Solution
## 1. Recursion (DFS)
```python
# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(h) h = max_height
- 
## 2. BFS
- go through all the nodes in 1 level and increment the depth variable.
```python
# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        q = deque([root])
        depth = 0

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1
        
        return depth      
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(w) : w = max width

| **Feature**         | **BFS**                           | **DFS**                                 |
|----------------------|-----------------------------------|------------------------------------------|
| **Traversal**        | Level-by-level                    | One branch to leaf, then backtrack        |
| **Uses**             | Queue                             | Recursion (stack)                         |
| **Time Complexity**  | O(n)                              | O(n)                                     |
| **Space Complexity** | O(w) (max width)                  | O(h) (height of tree)                    |
| **Best for**         | Counting levels                   | Recursive thinking / path-based logic    |
