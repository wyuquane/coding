class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        first_spot = [values[i] + i for i in range(len(values))]
        second_spot = [values[j] - j for j in range(len(values))]

        split_index = first_spot.index(max(first_spot[0: -1]))

        stack = [first_spot[0]]

        for i in range(1, split_index + 1):
            if first_spot[i] >= stack[-1]:
                stack.append(first_spot[i])

        max_2nd_spot = max(second_spot[split_index + 1: ])

        result = first_spot[split_index] + max_2nd_spot
        stack.pop()

        for i in range(split_index - 1, -1, -1):
            if second_spot[i + 1] > max_2nd_spot:
                max_2nd_spot = second_spot[i + 1]

            try:
                pair = stack[-1] + max_2nd_spot
            except:
                break

            if pair > result:
                result = pair

            if first_spot[i] == stack[-1]:
                stack.pop()

        return result


x = Solution().maxScoreSightseeingPair([2,2,2])
print(x)



