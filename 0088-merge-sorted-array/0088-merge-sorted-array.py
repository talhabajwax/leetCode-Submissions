class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_index=(m-1)
        num2_index=(n-1)
        num1_last_index= n+m-1
        while num2_index>=0:
            if num1_index>=0:
                if nums1[num1_index] < nums2[num2_index]:
                    nums1[num1_last_index] = nums2[num2_index]
                    num2_index = num2_index-1
                    num1_last_index = num1_last_index-1
                 

                elif nums1[num1_index] > nums2[num2_index]:
                     nums1[num1_last_index] =  nums1[num1_index]
                     num1_index = num1_index-1 
                     num1_last_index = num1_last_index-1
                elif nums1[num1_index] == nums2[num2_index]:
                     nums1[num1_last_index] = nums2[num2_index]
                     num2_index = num2_index-1
                     num1_last_index = num1_last_index-1
            else:
                        nums1[num1_last_index] = nums2[num2_index]
                        num2_index = num2_index-1
                        num1_last_index = num1_last_index-1

                     