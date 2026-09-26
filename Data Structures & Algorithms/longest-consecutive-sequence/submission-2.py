class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = sorted(set(nums))
        best = length = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                length += 1
                best = max(best, length)
            else:
                length = 1
        return best