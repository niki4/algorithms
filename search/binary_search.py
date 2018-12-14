# NOTE: array (list) MUST be sorted prior to run binary search, if not - functions will return -1 (so it's correct behaviour)

def binary_search(a: list, x: int) -> int:
	low = 0
	high = len(a) - 1
	mid = int()

	while low <= high:
	    mid = int((low + high) / 2)
	    if a[mid] < x:
	        low = mid + 1    # choose right part
	    elif a[mid] > x:
	    	high = mid - 1   # choose left part
	    else:
	    	return mid       # search result

	return -1                # in case something went wrong


def binary_search_recursive(a: list, x: int, low: int, high: int) -> int:
	if low > high:
		return -1

	mid = int((low + high) / 2)
	if x > a[mid]:
		return binary_search_recursive(a, x, mid + 1, high)    # choose right part
	elif x < a[mid]:
		return binary_search_recursive(a, x, low, mid - 1)     # choose left part
	else:
		return mid    # result


if __name__ == '__main__':
	where = [15, 16, 19, 20, 25, 1, 4, 5, 7, 10, 14]
	where_sorted = sorted(where)    # [1, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
	res1 = binary_search(where_sorted, 7)    # 3, is an index of the number in array
	res2 = binary_search_recursive(where_sorted, 16, 0, len(where) - 1)   # 7
	print("res1:", res1)
	print("res2:", res2)
