class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            need=target - nums[i]
            if(need in nums and nums.index(need) != i):
                return[ i , nums.index(need)]
        