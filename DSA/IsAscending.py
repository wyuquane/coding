def is_ascending(arr: list):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True



if __name__ == '__main__':
    pass