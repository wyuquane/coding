def combinations(n: int, k: int) -> list[list]:
    queues = [[i] for i in range(n - k + 1)]
    for i in range(1, k):
        for _ in range(len(queues)):
            replace_list = queues.pop(0)
            for j in range(replace_list[-1] + 1, n - k + i + 1):
                queues.append(replace_list + [j])
    return queues

if __name__ == '__main__':
    result = combinations(5, 3)
    print(result)

