# -*- coding: utf-8 -*-
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """

        if not A:
            return B
        if not B:
            return A
        cur = m
        for item in B:
            A[cur] = item
            cur += 1

        for i in range(n + m - 1):
            for j in range(n + m - 1 - i):
                if A[j] > A[j + 1]:
                    tmp = A[j + 1]
                    A[j + 1] = A[j]
                    A[j] = tmp
        # i = 0
        # j = 0
        # while i < n + m - 1:
        #     while j < n + m - 1 -i:
        #         if A[j] > A[j+1]:
        #             tmp = A[j+1]
        #             A[j+1] = A[j]
        #             A[j] = tmp
        #         j += 1
        #     i += 1
        return A
