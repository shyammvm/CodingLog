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

### Sliding Window O(n):
```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        counts = Counter(s1)
        n, m = len(s1), len(s2)
        start, end = 1, m
        window = Counter(s2[:n])
        if window == counts:
            return True

        for i in range(n,m):
            left = s2[i-n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]

            window[s2[i]] += 1
            if window == counts:
                return True
        return False
```

---

## Notes
- Approach: 
- Time Complexity: O(n)
- Space Complexity: O(1) : atmost len(s1) elements in the counter