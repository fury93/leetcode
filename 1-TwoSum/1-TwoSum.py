            seen[value] = index

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums = sorted((value, index) for index, value in enumerate(nums))
        l, r = 0, len(nums)-1

        while l < r:
            sm = nums[l][0] + nums[r][0]
            if sm > target:
                r -= 1
            elif sm < target:
                l +=1
            else:
                break

        return [nums[l][1], nums[r][1]]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = len(nums)
        for i, j in itertools.product(range(L), range(1, L)):
            if nums[j] == target - nums[i]:
                return [i, j]
                


[
