
def check_capture(coordinates: list):
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            if abs(j - i) == abs(coordinates[j] - coordinates[i]):
                return True
    return False

def backtracking(coordinates=[]):
    if check_capture(coordinates):
        return
    if len(coordinates) == 8:
        print(coordinates)
        return

    remain = {1, 2, 3, 4, 5, 6, 7, 8} - set(coordinates)

    for row in remain:
        backtracking(coordinates + [row])

if __name__ == '__main__':
    backtracking()
