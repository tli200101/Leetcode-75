class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        # Insert into hashtable while lookup
        for index, num in enumerate(nums):
            complement = target - num
            # hashmap lookup
            if complement in hash_table:
                return [hash_table[complement], index]
            hash_table[num] = index
        
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    solver = Solution()
    print(solver.twoSum(nums, target))