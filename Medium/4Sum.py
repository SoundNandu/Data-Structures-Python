#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:17:43 2020

@author: sowndhariyanandarajkumar
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if nums == None or len(nums)==0:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if (i > 0 and nums[i] == nums[i - 1]):  # if two consecutive numbers in the outer loop are same, skip the second
                continue
            low = i+1
            high = len(nums)-1
            mid = i + high //2
            
            while (low<high):
                currentSum = nums[i]+nums[low]+nums[mid]+nums[high]
                if currentSum ==  target:
                    result.append([nums[i],nums[low],nums[mid],nums[high]])
                    low += 1
                    mid += 1
                    high -= 1
                    while (low < high and nums[low] == nums[low - 1]):
                        low += 1
                    while (low < high and nums[high] == nums[high + 1]):
                        high -= 1 
                    while (low < high and nums[mid] == nums[mid - 1]):
                        mid += 1
                elif currentSum < target :
                    low += 1
                    mid += 1
                else:
                    high -= 1
        return result
                    
            
    
       
        
        

obj = Solution()
obj.fourSum([1, 0, -1, 0, -2, 2],0)