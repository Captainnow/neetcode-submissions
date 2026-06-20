class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies using a standard Hash Map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            buckets[cnt].append(num)

        # Step 3: Collect elements from right to left (highest frequency to lowest)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
