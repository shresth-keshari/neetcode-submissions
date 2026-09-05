class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap =  {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        sortedKeys = sorted(countMap.keys(), key = countMap.get, reverse = True)
        return sortedKeys[:k]