# Problem: ComplimentOfBase10Integer

# Link: https://leetcode.com/problems/complement-of-base-10-integer
# Difficulty: easy  

---

## Solution
## 1. Approach 1 : Arithmetic
```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        i = 0
        while n > 0:
            this = 1 if (n % 2) == 0 else 0
            ans = ans + (this * (2 ** i))
            i += 1
            n = n // 2
        return ans
```

---

#### Notes
- Approach:
- Time Complexity: O(1)
- Space Complexity: O(length)


## 2. Approach 2 : Using shift operation instead of arithmetic
```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        i = 0
        while n > 0:
            this = 1 if (n % 2) == 0 else 0
            ans = ans + (this * (2 ** i))
            i += 1
            n = n // 2
        return ans
```

---

#### Notes
- Approach:
- Time Complexity: O(1)
- Space Complexity: O(length)
  

## 2. Approach 3  : Using mask and XOR operation
```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        i = 0
        while n > 0:
            this = 1 if (n % 2) == 0 else 0
            ans = ans + (this * (2 ** i))
            i += 1
            n = n // 2
        return ans
```

---

#### Notes
- Approach:
- Time Complexity: O(1)
- Space Complexity: O(1)