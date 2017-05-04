#! /usr/bin/python
# -*- coding:UTF-8 -*-



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s==null or len(s)==0:
            return 0
            
        charset = set()
        maxlen = 0
        pre = 0
        back =0
        
        for i in xrange(len(s)):
            if s[i] in charset:
                





if __name__ == '__main__':

    

