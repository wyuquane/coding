def flatten_v2(nested_list: list):
    stack = [nested_list]
    result = list()
    while len(stack) != 0 and isinstance(stack, list):
        popped = stack[-1]
        stack.pop()
        for ele in popped:
            stack.append(ele)
        while len(stack) != 0 and not isinstance(stack[-1], list):
            pop_ele = stack[-1]
            stack.pop()
            result.append(pop_ele)
    result += stack[::-1]
    result.reverse()
    return result


def flatten_nested_list(nested_list: list):
    s = str(nested_list)
    arr = list(s.split(', '))
    for i in range(len(arr)):
        arr[i] = arr[i].strip('[]')
    arr = list(map(int, arr))
    return arr

if __name__ == '__main__':
    arr = [1, [2, [3, [1, 4]]], [1, 3]]
    flatten = flatten_v2(arr)
    print(flatten)
