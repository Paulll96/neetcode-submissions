class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        hm = {}
        l = []

        for i in nums:
            hm[i] = hm.get(i, 0) + 1

        li = sorted(hm.items(), key=lambda x: x[1], reverse=True)

        for i in li[:k]:
            l.append(i[0])

        return l