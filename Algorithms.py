#! /usr/bin/python
# -*- coding:UTF-8 -*-



class Solution(object):


    ## Q1 ##
    '''
    Given an array of integers, return indices of the two numbers 
    such that they add up to a specific target.
    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None:
            return None

        secnumdict = {}
        for i in xrange(len(nums)):
            if secnumdict.has_key(nums[i]):
                return [secnumdict[nums[i]],i]
            else:
                secnumdict[target-nums[i]] = i
        

    ## Q3 ##
    # Given a string, find the length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s is None or len(s) == 0:
            return 0
            
        charset = set()
        maxlen = 0
        pre = 0
        back =0
        
        for i in xrange(len(s)):
            if s[i] in charset:
                while s[back] != s[i]:
                    charset.remove(s[back])
                    back += 1
                back += 1
            charset.add(s[i])
            pre = i
            maxlen = max(maxlen, pre - back + 1)
        return maxlen





if __name__ == '__main__':

    solu = Solution()

    print solu.twoSum([2,7,11,15],9)

    #print solu.lengthOfLongestSubstring('pwwkew')
