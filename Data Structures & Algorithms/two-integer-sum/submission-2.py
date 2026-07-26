class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hm:
                v=hm.get(diff,0)
                return [v,i]
            else:
                hm[nums[i]]=i
        


        