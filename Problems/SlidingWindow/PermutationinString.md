# Problem: Permutation in String
# Link: https://leetcode.com/problems/permutation-in-string/
# Difficulty: Medium

---

## Solution

### Brute Force - Sliding Window
```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counts = Counter(s1)

        start, end = 0, len(s1)

        while end <= len(s2):
            if s2[start] in counts:
                if Counter(s2[start:end]) == counts:
                    return True
            start += 1
            end += 1
        return False
```

---

## Notes
- Approach: 
- Time Complexity: 
- Space Complexity: leetcode