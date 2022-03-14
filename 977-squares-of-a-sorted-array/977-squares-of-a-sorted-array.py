class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:   #[-4,-1,0,3,10]  -> 16, 1, 0, 9, 100
        
        start , end , last_index = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)
        
        while start <= end:
            if nums[start]**2 >= nums[end]**2:
                res[last_index] = nums[start]**2
                start += 1
            else:
                res[last_index] = nums[end]**2
                end -= 1
                
            last_index -= 1
        
        return res
                
                
        
        