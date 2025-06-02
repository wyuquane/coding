class HashMap:
    def __init__(self):
        self.data = [[], [], [], [], [], [], [], [], [], []]
        self.size = 0

    def hash(self, key):
        sum_digits = 0
        for digit in str(key):
            sum_digits += int(digit)
        return sum_digits % 10

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.data[index]
        for i, k in enumerate(bucket[::2]):
            if k == key:
                bucket[2 * i + 1] = value
                return
        bucket.extend([key, value])
        self.size += 1

    def remove(self, key):
        index = self.hash(key)
        bucket = self.data[index]
        if key in bucket[::2]:
            position = bucket[::2].index(key) * 2
            bucket.pop(position)
            bucket.pop(position)
            self.size -= 1

    def get(self, key):
        index = self.hash(key)
        bucket = self.data[index]
        if key in bucket[::2]:
            position = bucket[::2].index(key) * 2
            return bucket[position + 1]
        return None

    def length(self):
        return self.size

    def __str__(self):
        string = str()
        for bucket in self.data:
            string += f'{bucket}\n'
        return string[0: -1]

if __name__ == '__main__':
    hash_map = HashMap()

    # Adding some entries
    hash_map.put("1234567", "Charlotte")
    hash_map.put("1234568", "Thomas")
    hash_map.put("1234569", "Jens")
    hash_map.put("1234570", "Peter")
    hash_map.put("1234571", "Lisa")
    hash_map.put("1234672", "Adele")
    hash_map.put("1234573", "Michaela")
    hash_map.put("1236574", "Bob")

    print(hash_map)

    # Demonstrating retrieval
    print("\nName associated with '1234570':", hash_map.get("1234570"))

    print("Updating the name for '1234570' to 'James'")
    hash_map.put("1234570", "James")

    # Checking if Peter is still there
    print("Name associated with '1234570':", hash_map.get("1234570"))

    print("Removing the entry associated with '1234567'")
    hash_map.remove('1234567')
    print("Name associated with '1234567':", hash_map.get("1234567"))
