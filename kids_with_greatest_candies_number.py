class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        can_maximum=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies>=can_maximum:
                result.append(True)
            else:
                result.append(False)
        return result
