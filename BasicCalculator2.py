class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        main_stack = list()
        product_stack = list()
        s = s.replace(' ', '')
        num = str()
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
                i += 1
            elif s[i] == '+':
                main_stack.append(int(num))
                num = str()
                i += 1
            elif s[i] == '-':
                main_stack.append(int(num))
                num = '-'
                i += 1
            elif s[i] in ('*', '/'):
                product_stack.append(int(num))
                product_stack.append(s[i])
                num = str()
                i += 1
                while s[i].isnumeric() or s[i] in ('*','/'):
                    if s[i].isnumeric():
                        num += s[i]
                        i += 1
                        if i == len(s): break
                    else:
                        product_stack.append(int(num))
                        factor1 = product_stack[0]
                        factor2 = product_stack[2]
                        if product_stack[1] == '*':
                            production = factor1 * factor2
                        else:
                            if factor1 * factor2 > 0 or factor1 % factor2 == 0:
                                production = factor1 // factor2
                            else:
                                production = factor1 // factor2 + 1
                        product_stack = [production, s[i]]
                        num = str()
                        i += 1
                        # print(production)
                        # print(product_stack)

                product_stack.append(int(num))
                factor1 = product_stack[0]
                factor2 = product_stack[2]
                # print(product_stack)
                if product_stack[1] == '*':
                    production = factor1 * factor2
                else:
                    if factor1 * factor2 > 0 or factor1 % factor2 == 0:
                        production = factor1 // factor2
                    else:
                        production = factor1 // factor2 + 1
                num = str(production)
                # print(num)

                product_stack = list()

            else:
                i += 1
        if len(num) > 0: main_stack.append(int(num))
        return sum(main_stack)

s = input()
x = Solution().calculate(s)
print(x)
