## Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

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