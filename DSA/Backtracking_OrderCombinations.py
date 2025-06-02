def order_combinations(k: int, n: int):
    result = []
    set_n = {i + 1 for i in range(n)}
    def backtracking(vector: list):
        if len(vector) == k:
            result.append(vector)
            return

        remain = set_n - set(vector)
        for num in remain:
            backtracking(vector + [num])

    backtracking([])
    return result

if __name__ == '__main__':
    print(order_combinations(2, 3))
