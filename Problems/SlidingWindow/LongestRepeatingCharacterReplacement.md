# Problem: Longest Repeating Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium

### Brute force
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        if l == 1:
            return 1
        if l < k:
            return l
        maxlen = 0
        for w in range(l, k, -1):
            print('w:',w)
            start, end = 0, w
            while end < l+1:
                window = s[start:end]
                print('window:', window)
                this = set(window)
                print('set:',this)
                if len(window) - max(window.count(ch) for ch in this) <= k:
                    return w
                start += 1
                end = start + w
```
### O(n): sliding window
```
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        maxcount = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxcount = max(maxcount, count[s[right]])

            while (right - left + 1) - maxcount > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result
```
