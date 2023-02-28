class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list = [nums[0]]
        for j in range(1, len(nums)):
            list.append(list[-1]+nums[j])
        return list
