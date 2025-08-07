class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Core idea: answer[i] = prefix * suffix. 
        n = len(nums)
        answer = [1] * n # Initialize answer array

        # First pass: left to right, compute prefixes, directly store prefix in answer array
        for i in range(1, n): # Skipping first element, cuz no prefix
            answer[i] = answer[i-1] * nums[i-1]

        # Second pass: right to left, compute suffix on the fly
        suffix = 1
        for i in range(n-1, -1, -1): # Reverse iteration
            answer[i] *= suffix 
            suffix *= nums[i] # update suffix

        return answer
        

if __name__ == "__main__":
    nums = [1,2,3,1]
    solver = Solution()
    print(solver.productExceptSelf(nums))