s = input()
chars_in_s = list(set(s))
print(chars_in_s)
case = []
for i in range(len(chars_in_s) - 1):
    for j in range(i + 1, len(chars_in_s)):
        case.append([chars_in_s[i], chars_in_s[j]])
print(case)
alternate_string = []
for i in range(len(case)):
    temp_string = str()
    # pointer_0_1 = 0
    if s.find(case[i][0]) < s.find(case[i][1]):
        pointer_0_1 = 0
    else:
        pointer_0_1 = 1
    char = case[i][pointer_0_1]
    indx = s.find(char)
    while indx != -1:
        temp_string += s[indx]
        if pointer_0_1 == 1:
            pointer_0_1 = 0
        else:
            pointer_0_1 = 1
        char = case[i][pointer_0_1]
        temp_indx = s.find(char, indx + 1)
        indx = temp_indx
    alternate_string.append(temp_string)
print(alternate_string)
lenght_alternate_string = list(map(len, alternate_string))
print(lenght_alternate_string)
print(max(lenght_alternate_string))





