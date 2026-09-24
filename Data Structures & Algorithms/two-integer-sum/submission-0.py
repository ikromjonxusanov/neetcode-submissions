class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i, num in enumerate(nums):
            answer[target - num] = i

        for i, num in enumerate(nums):
            if num not in answer:
                continue
            if answer[num] == i:
                continue
            return [i, answer[num]]
            
        return [0,0]
            
        