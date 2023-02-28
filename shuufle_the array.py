class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle=[]
        for j in range(n):
            shuffle+=[nums[j]]
            shuffle+=[nums[j+n]]
        return shuffle
