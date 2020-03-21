#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:01:21 2020

@author: sowndhariyanandarajkumar
"""

#since three values we are going to use 3 points i,low,high

class Solution:
    def threeSumClosest(self, nums, target):
        if nums == None or len(nums) == 0:
            return []
        #result = 0
        #lets sort the values of num
        nums.sort()
        #initail value if result is calculated by adding the first 3 vlaues in the nums later it will be updated
        result = sum(nums[:3])
        print(result)
       
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while (low < high):
                sums = nums[i]+nums[low]+nums[high]
                if sums == target:
                    return sums
                   
                elif abs(sums - target) < abs(result - target):
                    result = sums
                elif sums < target:
                    low +=1
                else:
                    high -=1
                
        return result
                    
                



obj = Solution()
obj.threeSumClosest([-1, 2, 1, -4],1)
        
        
        
        