from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = Counter(nums)
        return [item for item, count in counting.most_common(k)]
