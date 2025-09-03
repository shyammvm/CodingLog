# Problem: Time Based Key-Value Store
# Link: https://leetcode.com/problems/time-based-key-value-store/description/
# Difficulty: Medium
```
class TimeMap:

    def __init__(self):
        self.store = {}

    def binary(self, arr : list, timestamp : int) -> str:
        l, r = 0, len(arr) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]

            elif arr[mid][0] < timestamp:
                result = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = []
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
            return self.binary(arr, timestamp)
        else:
            return ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```