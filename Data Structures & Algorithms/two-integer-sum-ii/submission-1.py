class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        
        for ind, num in enumerate(numbers):
            complement = target - num
            
            if complement in seen:
                # Return 1-indexed positions
                return [seen[complement] + 1, ind + 1]
                
            # Store the 0-indexed position in the dictionary
            seen[num] = ind
