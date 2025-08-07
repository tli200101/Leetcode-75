class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = cur_min = global_max = nums[0]

        for num in nums[1:]:            
            temp = cur_max * num
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)
            global_max = max(global_max, cur_max)
            
        return global_max

if __name__ == "__main__":
    nums = [2,3,-2,4]
    solver = Solution()
    print(solver.maxProduct(nums))