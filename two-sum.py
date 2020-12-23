class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(num, i) for i, num in enumerate(nums)])
        left, right = 0, len(nums) - 1
        num, idx = 0, 1
        while not left == right:
            temp = nums[left][num] + nums[right][num]
            if temp > target:
                right -= 1
            elif temp < target:
                left += 1
            else:
                return [nums[left][idx], nums[right][idx]]