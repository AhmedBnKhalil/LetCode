class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # دمج القائمتين
        nums3 = nums1 + nums2
        nums3.sort()

        n = len(nums3)

        # إذا كان العدد فردي، نرجّع العنصر الأوسط
        if n % 2 == 1:
            return float(nums3[n // 2])
        else:
            # إذا كان زوجي، نرجع متوسط العنصرين في المنتصف
            mid1 = nums3[n // 2 - 1]
            mid2 = nums3[n // 2]
            return (mid1 + mid2) / 2.0


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
