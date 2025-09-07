# Problem: ContainsDuplicate

# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy  

---

## Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False
```

---

## Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(n) (set)
