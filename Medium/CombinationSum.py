#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:09:03 2020

@author: sowndhariyanandarajkumar
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == None or len(candidates) == 0:
            return []
        self.result = []
        self.backtrack(candidates,target,[],0,0)
        return self.result
        
    def backtrack(self,candidates,target,temp,index,sums):
        #base
        if sums == target:
            self.result.append(list(temp))
        if sums > target:
            return
        
        #logic
        #action
        for i in range(index,len(candidates)):
            temp.append(candidates[i])
           #recursion
            self.backtrack(candidates,target,temp,i,sums+candidates[i])
            #backtrack
            temp.pop()
        
    
        
        
        
        
        
obj = Solution()
obj.combinationSum([2,3,5],8)