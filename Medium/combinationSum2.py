#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:17:45 2020

@author: sowndhariyanandarajkumar
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        if candidates == None or len(candidates) == 0:
            return []
        candidates.sort()
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
            if i != index and candidates[i] == candidates[i-1]:
                continue
            temp.append(candidates[i])
            self.backtrack(candidates,target,temp,i+1,sums+candidates[i])
            temp.pop()
        
obj = Solution()
obj.combinationSum2([2,3,5],8)  