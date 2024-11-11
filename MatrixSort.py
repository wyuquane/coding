n = int(input().strip())
stu_name = input().rstrip().split()
stu_score = list(map(int, input().rstrip().split()))

matrix = []
for i in range(len(stu_score)):
    matrix.append([stu_name[i], stu_score[i]])

def getvalue(item):
    return item[1]

matrix.sort(reverse=True, key=getvalue)

ordinal = [1]

for i in range(1, n):
    if matrix[i][1] == matrix[i - 1][1]:
        ordinal.append(ordinal[-1])
    else:
        ordinal.append(i + 1)

for name in stu_name:
    for i in range(n):
        if matrix[i][0] == name:
            print(ordinal[i], end=' ')



