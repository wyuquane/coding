import random
from IsAscending import is_ascending



def merge_sorted_list(arr1: list, arr2: list):
	if len(arr1) == 0:
		return arr2
	if len(arr2) == 0:
		return arr1

	sorted_list = list()
	i = j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			sorted_list.append(arr1[i])
			i += 1
		else:
			sorted_list.append(arr2[j])
			j += 1

	if i == len(arr1):
		sorted_list += arr2[j: ]
	else:
		sorted_list += arr1[i: ]

	return sorted_list



def merge_sort(arr: list):
	if len(arr) == 1:
		return arr

	mid = len(arr) // 2
	return merge_sorted_list(merge_sort(arr[: mid]), merge_sort(arr[mid: ]))


if __name__ == '__main__':
    arr = [random.randint(10, 100) for _ in range(10)]
    print(arr)
    arr = merge_sort(arr)
    print(arr, is_ascending(arr))
