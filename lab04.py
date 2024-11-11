
def ex1(matrix: list):
    result = 0
    for row in matrix:
        result += sum(row)
    return result

def ex2(matrix: list):
    return [sum(row) for row in matrix]

def ex3(dic: dict):
    key_value = list(dic.items())
    value_key = list()
    for i in range(len(key_value)):
        value_key.append(key_value[i][::-1])
    return dict(value_key)

def ex4(a: set, b: set):
    intersection = set()
    for ele in a:
        if ele in b:
            intersection.add(ele)
    return intersection

def ex5(a: set, b: set):
    symmetric_difference = set()
    for ele in a:
        if ele not in b:
            symmetric_difference.add(ele)
    for ele in b:
        if ele not in a:
            symmetric_difference.add(ele)
    return symmetric_difference

def str_sort(s: str):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

def ex6(arr: list[str]):
    dic = dict()
    for word in arr:
        if str_sort(word) not in dic:
            dic[str_sort(word)] = [word]
        else:
            dic[str_sort(word)].append(word)
    return list(dic.values())

def ex7(dic1: dict, dic2: dict):
    for key in dic2:
        if key in dic1.keys():
            if type(dic2[key]) is dict:
                for k, v in dic2[key].items():
                    dic1[key][k] = v
            else:
                dic1[key] = dic2[key]
    return dic1

def ex8(matrix: list[list]):
    m = len(matrix[0])
    n = len(matrix)
    dic = dict()
    for j in range(n):
        for i in range(m):
            if matrix[j][i] not in dic.keys():
                dic[matrix[j][i]] = 1
            else:
                dic[matrix[j][i]] += 1
    return dic

def ex9(set1: set, set2: set):
    result = set()
    for ele in set1:
        if ele not in set2:
            result.add(ele)
    return result

def ex10(matrix: list[tuple]):
    m = len(matrix[0])
    n = len(matrix)
    dic = dict()
    for j in range(n):
        for i in range(m):
            if matrix[j][i] not in dic.keys():
                dic[matrix[j][i]] = 1
            else:
                dic[matrix[j][i]] += 1
    max_common = max(dic.values())
    result = set()
    for key in dic:
        if dic[key] == max_common:
            result.add(key)
    return result

def compare_str(s1: str, s2: str, order: str):
    '''s1 < s2 return 1, s1 > s2 return -1, s1 == s2 return 0'''
    if s1 == s2:
        return 0
    if len(s1) == 0: return 1
    if len(s2) == 0: return -1
    if s2.startswith(s1):
        return 1
    if s1.startswith(s2):
        return -1
    i = 0
    while s1[i] == s2[i]:
        i += 1
    if order.find(s1[i]) < order.find((s2[i])):
        return 1
    else:
        return -1

def ex11(words: list, order: str):
    for i in range(len(words) - 1):
        if compare_str(words[i], words[i + 1], order) == -1:
            return False
    return True

if __name__ == '__main__':
    words = ["hello", "", "intelligent"]
    order = "hlabicdefgjkmnopqrstuvwxyz"
    print(ex11(words, order))