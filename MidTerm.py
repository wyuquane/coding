
def is_not_empty(s: str):
    if len(s) == 0:
        return False
    return True

def readFile(filename: str) -> list:
    file = open(filename, 'rt', encoding='utf-8')
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
    data = list(filter(is_not_empty, data))
    return data

def extract_num(s: str):
    num = str()
    for char in s:
        if char.isnumeric():
            num += char
    num = int(num)
    return num

def mergeFile(filename1: str, filename2: str) -> list:
    data1 = readFile(filename1)
    data2 = readFile(filename2)
    data = data1 + data2
    data.sort(key=extract_num)
    return data

def del_num(s: str):
    for char in s:
        if char.isnumeric():
            s = s[1: ]
        else:
            return s

def writeFile(out_file: str, content: list) -> None:
    file = open(out_file, 'wt', encoding='utf-8')
    content = list(map(del_num, content))
    for line in content:
        file.write(line + '\n')
    file.close()
    return None


def convert(filename: str) -> str:
    file = open('encode.txt', 'rt', encoding='utf-8')
    data = file.read()
    file.close()
    data = data.replace(' ', '')
    data = data.replace('\n', ' ')
    return data


if __name__ == '__main__':
    file = 'encode.txt'
    print(convert(file))


