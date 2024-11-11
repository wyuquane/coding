
def check_contiguous(s: str):
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            return False
    return True

def uniform_contiguous_substring(s: str):
    result = list()
    while s != '':
        temp = str()
        if check_contiguous(s):
            result.append(s)
            break
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                temp = s[0: i]
                s = s[i: ]
                break
        result.append(temp)
    return result

def weight_string(s: str):
    alphabet =' abcdefghijklmnopqrstuvwxyz'
    weight_char = alphabet.find(s[0])
    return [weight_char * i for i in range(1, len(s) + 1)]


string = input()
substring = uniform_contiguous_substring(string)
possible_weight = list()

for ele in substring:
    possible_weight.extend(weight_string(ele))

output = []

queries = int(input())
for _ in range(queries):
    query = int(input())
    if query in possible_weight:
        output.append('Yes')
    else:
        output.append('No')

print('\n'.join(output))