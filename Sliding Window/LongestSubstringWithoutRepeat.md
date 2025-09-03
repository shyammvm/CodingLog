```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        temp = ""
        maxlen = 0
        for i in s:
            if i not in temp:
                temp += i
            else:
                if len(temp) > maxlen:
                    maxlen = len(temp)
                temp = temp[temp.index(i)+1:] + i
                
        return max(maxlen, len(temp))
```
            