class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = set(nums)
        num1 = 0
        num2 = 0
        found = False
        for num in nums:
            num1 = num
            num2 = target - num1
            if num2 in bag and num1 != num2:
                found = True
                break
        if not found:
            for num in nums:
                num1 = num
                num2 = target - num1
                if num2 in bag:
                    found = True
                    break
        indices = []
        for i in range(len(nums)):
            if num1 == nums[i]:
                indices.append(i)
                break
        for i in range(indices[0] + 1, len(nums)):
            if num2 == nums[i]:
                indices.append(i)
                break
        return indices