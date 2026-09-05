class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num,0) + 1
        buckets = [[] for _ in range(0, len(nums) + 1)]
        for num, freq in countMap.items():
            buckets[freq].append(num)
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans