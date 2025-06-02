import random
from IsAscending import is_ascending


def radix_sort(arr: list[int]):
    no_digit = len(str(max(arr)))

    for i in range(no_digit):
        container = [[], [], [], [], [], [], [], [], [], []]
        for j in range(len(arr)):
            num = arr.pop(0)
            try:
                digit = int(str(num)[- (i + 1)])
            except:
                digit = 0
            container[digit].append(num)

        for k in range(10):
            arr.extend(container[k])

    return arr

def flash_sort(array):
    n = len(array)
    
    # Step 1: Find mininum and maximum values
    min_value, max_value = array[0], array[0]
    for i in range(1, n):
        if array[i] > max_value: max_value = array[i]
        if array[i] < min_value: min_value = array[i]
    if min_value == max_value: return     
    
    # Step 2: Divide array into m buckets
    import math
    m = max(math.floor(0.45 * n), 1)

    # Step 3: Count the number of elements in each class
    def get_bucket_id(value): 
        return math.floor((m * (value-min_value)) / (max_value-min_value+1))
    Lb = [0]*m
    for value in array:
        Lb[get_bucket_id(value)] +=1
    
    # Step 4: Convert the count to prefix sum
    for i in range(1, m):
        Lb[i] = Lb[i-1]+Lb[i]

    # Step 5: Rearrange the elements
    def find_swap_index(b_id):
        for ind in range(Lb[b_id-1],Lb[b_id]):
            if get_bucket_id(array[ind])!=b_id: break
        return ind
    def arrange_bucket(i1, i2, b):
        for i in range(i1, i2):
            b_id = get_bucket_id(array[i])
            while(b_id != b):
                s_ind = find_swap_index(b_id)
                array[i], array[s_ind] = array[s_ind], array[i]
                b_id = get_bucket_id(array[i])
        return

    for b in range(0, m-1): 
        if b == 0: arrange_bucket(b, Lb[b], b)
        else: arrange_bucket(Lb[b-1], Lb[b], b)

    # Step 6: Sort each bucket
    def insertion_sort(array):
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return array

    for i in range(m):
        if i == 0: array[i:Lb[i]] = insertion_sort(array[i:Lb[i]])
        else: array[Lb[i-1]:Lb[i]] = insertion_sort(array[Lb[i-1]:Lb[i]])
    return 




if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(10)]
    print(arr)
    flash_sort(arr)
    print(arr, is_ascending(arr))

