class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            if cur_sum < 0: # abandon current subarray, start over
                cur_sum = num
            else:
                cur_sum += num # extend
            
            # Update global max  
            max_sum = max(max_sum, cur_sum)  
                
        return max_sum

    
if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    solver = Solution()
    print(solver.maxSubArray(nums))