class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        found = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in found:
                return [i, found[complement]]
            found[nums[i]] = i
