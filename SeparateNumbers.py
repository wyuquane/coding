def separateNumbers(s: str):
    s = s.strip()
    save_s = str(s)
    for i in range(1, len(s) // 2 + 1):
        if int(s[0: i]) + 1 == int(s[i: ]):
            print('YES', save_s[0: i])
            return
        if s[i: ].startswith(str(int(s[0: i]) + 1)):
            len_num = len(str(int(s[0: i]) + 1))
            s = s[i: ]
            # print(s)
        else:
            s = str(save_s)
            continue
        while s[len_num: ].startswith(str(int(s[0: len_num]) + 1)):
            if int(s[0: len_num]) + 1 == int(s[len_num: ]):
                print('YES', save_s[0: i])
                return

            # print(s)
            temp = len(str(int(s[0: len_num]) + 1))
            s = s[len_num:]
            len_num = temp

        s = str(save_s)
    print('NO')

if __name__ == '__main__':
    q = int(input().strip())
    data = list()
    for q_itr in range(q):
        s = input()
        data.append(s)
    for ele in data:
        separateNumbers(ele)