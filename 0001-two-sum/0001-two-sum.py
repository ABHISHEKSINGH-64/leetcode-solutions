class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in map:
                return [map[needed], i]

            map[nums[i]] = i

        return []

            