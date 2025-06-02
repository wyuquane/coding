class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        queues = [['', '', n]]

        for i in range(2 * n):
            for _ in range(len(queues)):
                ele = queues.pop(0)
                if ele[1] == '':
                    ele[0] += '('
                    ele[1] += '('
                    ele[2] -= 1
                    queues.append(ele)

                else:
                    temp = ele.copy()
                    if ele[2] > 0:
                        temp[0] += '('
                        temp[1] += '('
                        temp[2] -= 1
                        queues.append(temp)

                    ele[0] += ')'
                    ele[1] = ele[1][0: -1]
                    queues.append(ele)

        result = list()
        for ele in queues:
            result.append(ele[0])

        return result

result = Solution().generateParenthesis(1)
print(result)





