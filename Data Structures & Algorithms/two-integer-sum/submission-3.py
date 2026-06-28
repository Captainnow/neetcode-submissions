class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind , num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement] , ind]
            seen[num] = ind