def knight(vi_tri: str):
    hang = int(vi_tri[1])
    cot = vi_tri[0]
    match cot:
        case 'a':
            cot = 1
        case 'b':
            cot = 2
        case 'c':
            cot = 3
        case 'd':
            cot = 4
        case 'e':
            cot = 5
        case 'f':
            cot = 6
        case 'g':
            cot = 7
        case 'h':
            cot = 8
    if hang >= 5:
        hang = 9 - hang
    if cot >= 5:
        cot = 9 - cot
    match (hang, cot):
        case (1, 1):
            print(2)
        case (1, 2) | (2, 1):
            print(3)
        case (3, 1) | (2, 2) | (1, 3) | (1, 4) | (4, 1):
            print(4)
        case (2, 3) | (3, 2) | (2, 4) | (4, 2):
            print(6)
        case _:
            print(8)

n = int(input())
day_vi_tri = list()
for i in range(n):
    vi_tri = input()
    day_vi_tri.append(vi_tri)
for strr in day_vi_tri:
    knight(strr)
