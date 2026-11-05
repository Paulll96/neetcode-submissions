class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={0:1}
        res=0
        csum=0
        for i in nums:
            csum+=i
            diff=csum-k
            res+=prefixsum.get(diff,0)

            prefixsum[csum]=prefixsum.get(csum,0)+1

        return res




