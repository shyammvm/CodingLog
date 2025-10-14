# Problem: FindTheDuplicateNumber

# Link: https://leetcode.com/problems/find-the-duplicate-number/
# Difficulty: Medium  
# Constraints : space complexity = O(1)
---

## Floyd’s theorem:

- If one pointer starts from the head of the list and another starts from the meeting point, and both move one step at a time, they’ll meet exactly at the start of the cycle.

## Solution
## 1. Brute Force using dictionary
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                return i
            else:
                count[i] = 1
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(n)

## 2. Floyd's Tortoise and Haire
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        # phase 1 : find intersection(meeting point) of cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # phase 2 : find the entrance to the cycle
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

---

#### Notes
- Approach:
- Time Complexity: O(n)
- Space Complexity: O(1)