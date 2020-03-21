#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 01:49:19 2020

@author: sowndhariyanandarajkumar
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or len(nums) == 0:
            return []
       
        result = [0]*2
        low = 0 
        high = len(nums)-1
        while (low < high):
            current = nums[low] + nums[high]
            if current == target:
                result[0]= low
                result[1]= high
                break
            elif current > target:
                high -= 1
                
            else:
                low += 1
        return result
                
                
            
        
obj = Solution()
obj.twoSum([2, 7, 11, 15],9)


class Solution(object):
    def twoSumApproach2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or len(nums) == 0:
            return []
        l = sorted(zip(nums, range(len(nums))))
        left, right = 0, len(l)-1
        while left<right:
            v = l[left][0]+l[right][0]
            if v == target:
                return [l[left][1], l[right][1]]
            if v < target:
                left += 1
            else:
                right -= 1
                
                
                        
obj = Solution()
obj.twoSumApproach2([2, 7, 11, 15],9)
            