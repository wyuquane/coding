def combination(k: int, n: int):
    result = []
    def backtracking(combination: list):
        if len(combination) == k:
            result.append(combination)
            return

        if len(combination) == 0:
            start = 1
        else:
            start = combination[-1] + 1

        for i in range(start, n - (k - len(combination)) + 2):
            backtracking(combination + [i])

    backtracking([])
    return result

if __name__ == '__main__':
    print(combination(2, 4))
