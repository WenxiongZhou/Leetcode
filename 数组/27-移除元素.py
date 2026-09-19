class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slowidx = 0
        for i in range(len(nums)):
            if not (nums[i] == val):
                nums[slowidx] = nums[i]
                slowidx += 1

        return slowidx
        