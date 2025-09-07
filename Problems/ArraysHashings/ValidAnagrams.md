# Problem: ValidAnagrams

# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy  

---

## Solution

If both uppper & lower case or other characters : Counter
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if Counter(s) == Counter(t):
            return True
        return False
```

If only lowercase characters: 26 bit array (supposed to be faster , but counter is faster in leetcode due to more optimisation/ counter is written in C)
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ref = [0] * 26

        for i in s:
            ref[ord(i) - ord('a')] += 1
        
        for i in t:
            ref[ord(i) - ord('a')] -= 1

        return all(i == 0 for i in ref)
       
```

---

## Notes
- Approach:
- Time Complexity:
- Space Complexity:
