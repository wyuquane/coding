from typing import Optional
import numpy as np



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def traversal(root):
    cur = root
    while cur:
        print(cur.val, end=' -> ')
        cur = cur.next
    print("None")


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        roles = [0] * n
        candies = [0] * n
        local_minimum = []

        if ratings[0] > ratings[1]:
            roles[0] = 1
        else:
            local_minimum.append(0)
            roles[0] = -1
            candies[0] = 1

        if ratings[-1] > ratings[-2]:
            roles[-1] = 1
        else:
            local_minimum.append(n - 1)
            roles[-1] = -1
            candies[-1] = 1



        for i in range(1, n - 1):
            if ratings[i - 1] >= ratings[i] and ratings[i] <= ratings[i + 1]:
                local_minimum.append(i)
                roles[i] = -1
                candies[i] = 1
            elif (ratings[i - 1] < ratings[i] and ratings[i] >= ratings[i + 1]) or (ratings[i - 1] <= ratings[i] and ratings[i] > ratings[i + 1]):
                roles[i] = 1

        # print(roles)
        # print(candies)

        for index in local_minimum:
            i = index - 1
            while i >= 0 and roles[i] != 1 and candies[i] == 0:
                candies[i] = candies[i + 1] + 1
                i -= 1

            i = index + 1
            while i < n and roles[i] != 1 and candies[i] == 0:
                candies[i] = candies[i - 1] + 1
                i += 1

        # print(candies)

        if roles[0] == 1:
            candies[0] = candies[1] + 1

        if roles[-1] == 1:
            candies[-1] = candies[-2] + 1

        for i in range(1, n - 1):
            if candies[i] == 0:
                if ratings[i] != ratings[i - 1]:
                    candies[i] = max(candies[i - 1], candies[i + 1]) + 1
                else:
                    candies[i] = candies[i + 1] + 1

        # print(candies)

        return sum(candies)





if __name__ == '__main__':
    import time
    start = time.time()
    result = Solution().candy([1,3,2,2,1])
    end = time.time()
    print(result, end - start)



