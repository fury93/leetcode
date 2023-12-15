class Solution:
    def findIntersectionValues(self, nums1: List
[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)

        cnt1, cnt2 = 0, 0
        for n1 in nums1:
            if n1 in s2: cnt1 += 1
        for n2 in nums2:
            if n2 in s1: cnt2 += 1
                
        return [cnt1, cnt2]

