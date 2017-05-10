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
        

    ## Q2 ##
    '''
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    '''
    
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        res = l1  #the result will be saved in l1
        cell = 0
        newNode = ListNode(0)
        while 1:
            if l1 != None and l2 != None:
                remainder = (l1.val + l2.val + cell) % 10
                cell = (l1.val + l2.val + cell) // 10
                l1.val = remainder
                if l1.next == None and l2.next != None:
                    newNode.next = l1  # use the point of the cell node to save the point one step previous of l1
                    l1.next = l2.next    #the rest of the l2 be a list behind the l1
                    l1 = l1.next
                    l2 = None
                else:
                    newNode.next = l1  # use the point of the cell node to save the point one step previous of l1
                    l1 = l1.next
                    l2 = l2.next
            elif l1 != None:
                remainder = (l1.val + cell) % 10
                cell = (l1.val + cell) / 10
                l1.val = remainder
                newNode.next = l1  # use the point of the cell node to save the point one step previous of l1
                l1 = l1.next
            else:
                break
        if cell > 0:   #has cell in the end 
            newNode.val = cell
            newNode.next.next = newNode
            newNode.next = None  #clear the point finally
        return res
        



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


    ## Q4 Median of Two Sorted Arrays ##
    '''
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    '''

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       

    ## Q328 Odd even linked list ##
    '''
    Given a singly linked list, group all odd nodes together followed by the even nodes. 
    Please note here we are talking about the node number and not the value in the nodes.
    You should try to do it in place. The program should run in O(1) space complexity 
    and O(nodes) time complexity.
    '''

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head

        odd = head
        even = head.next
        temp = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = temp

        return head



    ## Q445 Add Two Numbers II ##
    '''
    You are given two non-empty linked lists representing two non-negative integers. 
    The most significant digit comes first and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    '''

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None: return l2
        if l2 == None: return l1

        # use two list
        res = ListNode(None)
        ls1 = []
        ls2 = []
        while l1 != None:
            ls1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            ls2.append(l2.val)
            l2 = l2.next

        len1 = len(ls1)
        len2 = len(ls2)

        idx = 1
        carry = 0
        while len1 - idx >=0 or len2 - idx >= 0:
            if len1 - idx >=0 and len2 - idx >= 0:
                reminder = (ls1[len1-idx] + ls2[len2-idx] + carry) // 10
                newNode = ListNode((ls1[len1-idx] + ls2[len2-idx] + carry) % 10)
                carry = reminder
                newNode.next = res.next
                res.next = newNode
            elif len1 - idx >= 0:
                reminder = (ls1[len1-idx] + carry) // 10
                newNode = ListNode((ls1[len1-idx] + carry) % 10)
                carry = reminder
                newNode.next = res.next
                res.next = newNode
            elif len2 - idx >= 0:
                reminder = (ls2[len2-idx] + carry) // 10
                newNode = ListNode((ls2[len2-idx] + carry) % 10)
                carry = reminder
                newNode.next = res.next
                res.next = newNode
            else:
                break

            idx += 1
        
        # if the carry is not zero in the end, insert it into the list 
        if carry > 0:
            newNode = ListNode(carry)
            newNode.next = res.next
            res.next = newNode

        return res.next
                






if __name__ == '__main__':

    solu = Solution()

    print solu.twoSum([2,7,11,15],9)

    #print solu.lengthOfLongestSubstring('pwwkew')
