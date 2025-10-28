# Problem: LargestRectangleInHistogram

# Link: https://leetcode.com/problems/largest-rectangle-in-histogram
# Difficulty: Hard  

---

## Solution
## 1. Approach 1
- Loop over each bar in heights (plus one extra dummy height 0 at the end — to flush out remaining bars).
- Maintain a stack of (index, height) pairs where the heights are in increasing order.
- For each bar:
  -  While the current height is less than the height at the top of the stack:
  - Pop (idx, h) from the stack.
  - Compute area = h * (current_index - idx).
  - Update ans.
  - Push (new_start_index, current_height) to the stack.
  
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ref = []
        ans = 0
        for i, h in enumerate(heights + [0]):
            while ref and ref[-1][0] > h:
                height = ref.pop()[0]
                width = i if not ref else i - ref[-1][1] - 1
                area = height * width
                ans = max(area, ans)

            ref.append((h, i))

        return ans

```

---

#### Notes
- Approach: Monotonic increasing stack
- Time Complexity: O(n)
  - Each bar (index) is pushed onto the stack once.
  - Each bar is popped from the stack once.
  - Even though there’s a nested while loop,
  - the total number of iterations (push + pop) across the entire run = 2n (each element enters and leaves the stack exactly once).
- Space Complexity: O(n) [stack]
