def find_max_substr(s: str):
    s = s + '_'
    result = dict()
    count_char = 1
    for i, char in enumerate(s[0: len(s) - 1]):
        if s[i] != s[i + 1]:
            if char not in result.keys():
                result[char] = count_char
                count_char = 1
            else:
                if count_char > result[char]:
                    result[char] = count_char
                    count_char = 1
        else:
            count_char += 1
    return result

def weight_string(dic: dict):
    result = list()
    alphabet =' abcdefghijklmnopqrstuvwxyz'
    for char in dic.keys():
        weight_char = alphabet.find(char)
        result.extend([weight_char * i for i in range(1, dic[char] + 1)])
    return result


string = input()
statistic_char = find_max_substr(string)
possible_weight = weight_string(statistic_char)

output = list()

queries = int(input())
for _ in range(queries):
    query = int(input())
    if query in possible_weight:
        output.append('Yes')
    else:
        output.append('No')

print('\n'.join(output))
