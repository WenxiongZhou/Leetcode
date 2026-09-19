class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if not size:
            return 0
        idx = 1
        for i in range(1, size):
            if nums[i] != nums[idx-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx 