# Le Huy Hoang - 24122034
# Recursion 1

def factorial(n: int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def bunny_ears(bunnies: int):
    if bunnies == 0:
        return 0
    return 2 + bunny_ears(bunnies - 1)


def fibonacci(n: int):
    if n <= 1:
        return n
    return fibonacci(n - 1) + factorial(n - 2)


def bunny_ears2(bunnies: int):
    if bunnies == 0:
        return 0
    if bunnies % 2 == 0:
        return 3 + bunny_ears2(bunnies - 1)
    else:
        return 2 + bunny_ears2(bunnies - 1)


def triangle(rows: int):
    if rows == 0:
        return 0
    return rows + triangle(rows - 1)


def sum_digits(n: int):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def count7(n: int):
    if n == 0:
        return 0
    if n % 10 == 7:
        return 1 + count7(n // 10)
    else:
        return count7(n // 10)


def count8(n: int):
    if n == 0:
        return 0
    if n % 100 == 88:
        return 2 + count8(n // 10)
    elif n % 10 == 8:
        return 1 + count8(n // 10)
    else:
        return count8(n // 10)


def power_n(base: int, n: int):
    if n == 0:
        return 1
    return base * power_n(base, n - 1)


def count_x(s: str):
    if len(s) == 0:
        return 0
    if s[0] == 'x':
        return 1 + count_x(s[1:])
    else:
        return count_x(s[1:])


def count_hi(s: str):
    if len(s) <= 1:
        return 0
    if s[0: 2] == 'hi':
        return 1 + count_hi(s[1:])
    else:
        return count_hi(s[1:])


def change_x_y(s: str):
    if len(s) == 0:
        return s
    if s[0] == 'x':
        return 'y' + change_x_y(s[1:])
    else:
        return change_x_y(s[1:])


def change_pi(s: str):
    if len(s) <= 1:
        return s

    if s[0: 2] == 'pi':
        return '3.14' + change_pi(s[2:])
    else:
        return s[0] + change_pi(s[1:])


def no_x(s: str):
    if len(s) == 0:
        return s
    if s[0] == 'x':
        return no_x(s[1:])
    else:
        return s[0] + no_x(s[1:])


def array6(nums: list, index: int):
    if index >= len(nums):
        return False
    if nums[index] == 6:
        return True
    else:
        return array6(nums, index + 1)


def array11(nums: list, index: int):
    if index >= len(nums):
        return 0
    if nums[index] == 11:
        return 1 + array11(nums, index + 1)
    else:
        return array11(nums, index + 1)


def array220(nums: list, index: int):
    if index >= len(nums) - 1:
        return False
    if nums[index + 1] == 10 * nums[index]:
        return True
    else:
        return array220(nums, index + 1)


def all_star(s: str):
    if len(s) == 1:
        return s
    return s[0] + '*' + all_star(s[1:])


def pair_star(s: str):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + '*' + s[1] + pair_star(s[2:])
    else:
        return s[0] + pair_star(s[1:])


def end_x(s: str):
    if len(s) == 0:
        return s
    if s[0] == 'x':
        return end_x(s[1:]) + 'x'
    else:
        return s[0] + end_x(s[1:])


def count_pairs(s: str):
    if len(s) <= 2:
        return 0
    if s[0] == s[2]:
        return 1 + count_pairs(s[1:])
    else:
        return count_pairs(s[1:])


def count_abc(s: str):
    if len(s) <= 2:
        return 0
    if s[0: 3] == 'abc' or s[0: 3] == 'aba':
        return 1 + count_abc(s[1:])
    else:
        return count_abc(s[1:])


def count11(s: str):
    if len(s) <= 1:
        return 0
    if s[0: 2] == '11':
        return 1 + count11(s[2:])
    else:
        return count11(s[1:])


def string_clean(s: str):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + string_clean(s[2:])
    else:
        return s[0] + string_clean(s[1:])


def count_hi2(s: str):
    if len(s) <= 1:
        return 0
    if s == 'hi':
        return 1
    if s[-3:] == 'xhi':
        return count_hi2(s[:-3])
    elif s[-2:] == 'hi':
        return 1 + count_hi2(s[:-2])
    else:
        return count_hi2(s[:-1])


def paren_bit(s: str):
    if s[0] == '(' and s[-1] == ')':
        return s

    if s[0] != '(' and s[-1] != ')':
        return paren_bit(s[1:-1])
    elif s[0] != '(':
        return paren_bit(s[1:])
    elif s[-1] != ')':
        return paren_bit(s[:-1])


def nest_paren(s: str):
    if len(s) == 0:
        return True
    if s[0] == '(' and s[-1] == ')':
        return nest_paren(s[1:-1])
    else:
        return False


def str_count(s: str, sub: str):
    if len(s) < len(sub):
        return 0
    if s[0:len(sub)] == sub:
        return 1 + str_count(s[len(sub):], sub)
    else:
        return str_count(s[1:], sub)


def str_copies(s: str, sub: str, n: int):
    if len(s) < len(sub):
        if n <= 0:
            return True
        return False

    if s[0:len(sub)] == sub:
        return str_copies(s[1:], sub, n - 1)
    return str_copies(s[1:], sub, n)


def str_dist(s: str, sub):
    if len(s) < len(sub):
        return 0
    if s[:len(sub)] == s[-len(sub):] == sub:
        return len(s)
    elif s[:len(sub)] == sub:
        return str_dist(s[:-1], sub)
    elif s[-len(sub):] == sub:
        return str_dist(s[1:], sub)
    else:
        return str_dist(s[1:-1], sub)


# Recursion 2

def group_sum(start: int, nums: list, target: int):
    if start >= len(nums):
        if target == 0:
            return True
        return False

    return (group_sum(start + 1, nums, target - nums[start])
            or group_sum(start + 1, nums, target))


def group_sum6(start: int, nums: list, target: int):
    if start >= len(nums):
        return target == 0

    if nums[start] == 6:
        return group_sum6(start + 1, nums, target - 6)
    return (group_sum6(start + 1, nums, target - nums[start])
            or group_sum6(start + 1, nums, target))


def group_no_adj(start: int, nums: list, target: int):
    if start >= len(nums):
        return target == 0

    return (group_no_adj(start + 1, nums, target)
            or group_no_adj(start + 2, nums, target - nums[start]))


def group_sum5(start: int, nums: list, target: int):
    if start >= len(nums):
        return target == 0
    if start == len(nums) - 1 and nums[start] == 5:
        return target == 5

    if nums[start] == 5:
        if nums[start + 1] != 1:
            return group_sum5(start + 1, nums, target - 5)
        return group_sum5(start + 1, nums, target)

    return (group_sum5(start + 1, nums, target - nums[start])
            or group_sum5(start + 1, nums, target))


def group_sum_clump(start: int, nums: list, target: int):
    if start >= len(nums):
        return target == 0
    if start == len(nums) - 1:
        return target == nums[start] or target == 0

    if nums[start] == nums[start + 1]:
        extent = 2
        i = start + 2
        while i < len(nums) and nums[i] == nums[start]:
            extent += 1
        return (group_sum_clump(start + extent, nums, target)
                or group_sum_clump(start + extent, nums,
                                   target - extent * nums[start]))
    else:
        return (group_sum_clump(start + 1, nums, target)
                or group_sum_clump(start + 1, nums, target - nums[start]))


def split_array(nums: list):
    def helper(start: int, this: int, that: int):
        if start >= len(nums):
            return this == that

        return (helper(start + 1, this + nums[start], that)
                or helper(start + 1, this, that + nums[start]))

    return helper(0, 0, 0)


def split_odd10(nums: list):
    def helper(start: int, this: int, that: int):
        if start >= len(nums):
            return ((this % 10 == 0 and that % 2 == 1)
                    or (this % 2 == 1 and that % 10 == 0))

        return (helper(start + 1, this + nums[start], that)
                or helper(start + 1, this, that + nums[start]))

    return helper(0, 0, 0)


def split53(nums: list):
    def helper(start: int, mul5: int, mul3: int):
        if start >= len(nums):
            return mul5 == mul3

        if nums[start] % 5 == 0:
            return helper(start + 1, mul5 + nums[start], mul3)
        elif nums[start] % 3 == 0:
            return helper(start + 1, mul5, mul3 + nums[start])

        return (helper(start + 1, mul5 + nums[start], mul3)
                or helper(start + 1, mul5, mul3 + nums[start]))

    return helper(0, 0, 0)







