from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = Counter(nums)
        
        # Keep a min-heap tracking only the top K elements
        # Python orders tuples by their first element (count)
        heap = []
        for num, count in counting.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap) # Removes the item with the smallest frequency
                
        # Extract the numbers from the remaining heap items
        return [num for count, num in heap]
