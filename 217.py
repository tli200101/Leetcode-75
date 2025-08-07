class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
if __name__ == "__main__":
    nums = [0,2,3,1]
    solver = Solution()
    print(solver.containsDuplicate(nums))