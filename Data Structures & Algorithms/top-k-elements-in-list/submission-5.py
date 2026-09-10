class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We need count hashmap to map key: n value: count
        # count buckets with i representing count of n and [] representing numbers with count n
        # Then iterate through count buckets backwards until res is len k

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



            
        
        
        