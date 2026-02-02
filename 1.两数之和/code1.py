class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = nums[0]
        for i in range(len(nums)):
            for g in range(i + 1,len(nums)):
                if nums[i] + nums[g] == target:
                    return [i,g]