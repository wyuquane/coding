class HashSetOfName:
    def __init__(self):
        self.data = [[], [], [], [], []]
        self.size = 0

    def hash(self, value: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if len(value) == 0: return 0
        return alphabet.index(value[0]) % 5

    def add(self, value):
        index = self.hash(value)
        bucket = self.data[index]
        if value not in bucket:
            bucket.append(value)
            self.size += 1

    def remove(self, value):
        index = self.hash(value)
        bucket = self.data[index]
        if value in bucket:
            bucket.remove(value)
            self.size -= 1

    def contains(self, value):
        index = self.hash(value)
        bucket = self.data[index]
        return value in bucket

    def length(self):
        return self.size

    def __str__(self):
        string = str()
        for bucket in self.data:
            string += f'{bucket}\n'
        return string[0: -1]

if __name__ == '__main__':
    hash_set = HashSetOfName()

    hash_set.add("charlotte")
    hash_set.add("thomas")
    hash_set.add("jens")
    hash_set.add("peter")
    hash_set.add("lisa")
    hash_set.add("adele")
    hash_set.add("michaela")
    hash_set.add("bob")
    hash_set.add('emma')
    hash_set.add('daniel')
    print(hash_set)

    print("\n'peter' is in the set:", hash_set.contains('peter'))
    print("Removing 'peter'")
    hash_set.remove('peter')
    print("'peter' is in the set:", hash_set.contains('peter'))
    print("'adele' has hash code:", hash_set.hash('adele'))
    print('number of name in the set:', hash_set.length())