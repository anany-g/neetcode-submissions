class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxVal = 0
        for i in nums:
            if i == 1: 
                counter += 1 
                maxVal = max(maxVal, counter)
            else:
                counter = 0
        return maxVal
    