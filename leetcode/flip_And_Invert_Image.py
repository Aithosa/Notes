class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = A
        for row in range(len(A)):
            B[row][:] = A[row][::-1]
            for col in range(len(A[0])):
                if B[row][col] == 0:
                    B[row][col] = 1
                else:
                    B[row][col] = 0
        return B

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = A
        for row in range(len(A)):
            B[row][:] = A[row][::-1]
            for col in range(len(A[0])):
                B[row][col] = int(not B[row][col])
        return B


# 下面是别人的答案


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for x in range(len(A)):
            A[x].reverse();
            for y in range(len(A[x])):
                if A[x][y] == 0:
                    A[x][y]= 1
                else:
                    A[x][y] = 0
        return A


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: sxs
# @Date  : 2018/10/13
# @Desc  :

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        print(A)
        for index in range(len(A)):
            A[index].reverse()
            print(A[index])
        for index in range(len(A)):
            for index_chlid in range(len(A[index])):
                A[index][index_chlid] = int(not bool(A[index][index_chlid]))
        return A


print(Solution.flipAndInvertImage("", [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for x in range(len(A)):
            A[x].reverse();
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for a in A:
            r = []
            for i in a:
                if i == 1:
                    r.insert(0, 0)
                if i == 0:
                    r.insert(0, 1)
            res.append(r)
        return res


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for line in A:
            newline = line[::-1]
            for i in range(len(newline)):
                if newline[i]==0:
                    newline[i]=1
                else:
                    newline[i]=0
            B.append(newline)
        return B

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            a.reverse()
            for x in range(len(a)):
                a[x] = a[x] ^1
        return A


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l=len(A)
        for i in range(l):
            A[i].reverse()
            for j in range(l):
                #A[i][j]=1^A[i][j]
                A[i][j]=1-A[i][j]#经过测试，这条更快
        return A