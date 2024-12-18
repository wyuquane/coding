import string
import random
import time

alphabet = string.ascii_letters + " "
target = 'Hello World'
result = str()

for char in target:
    rndom = random.choice(alphabet)
    while rndom != char:
        print(result + rndom)
        time.sleep(0.02)
        rndom = random.choice(alphabet)
        
    result += char
    print(result)
    time.sleep(0.02)