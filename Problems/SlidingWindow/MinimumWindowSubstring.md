# Problem: Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard

---

## Solution

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        from collections import Counter
        ref = Counter(t)
        window = Counter()
        res, res_len = [-1, -1], float('inf')
        left = 0
        have, need = 0, len(ref)


        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in ref and window[ch] == ref[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in ref and window[s[left]] < ref[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if res_len != float('inf') else ""
```

---

## Notes
- Approach: 
- Time Complexity: O(m+n)
- Space Complexity: 