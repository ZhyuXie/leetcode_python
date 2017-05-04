#! /usr/bin/python
# -*- coding:UTF-8 -*-



class Solution(object):

    ## Given a string, find the length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s is None or len(s)==0:
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
            maxlen = max(maxlen, pre-back+1)
        return maxlen





if __name__ == '__main__':

    solu = Solution()
    print solu.lengthOfLongestSubstring('pwwkew')
