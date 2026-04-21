import math

# Binary Search 
arr_1 = list(range(1, 101))

def binary_search(arr, answer):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        print(answer, mid)
        guess = arr[mid]

        if guess == answer:
            return mid
        elif guess > answer:
            high = mid - 1
        else:
            low = mid + 1
    print(mid, answer)
    return None

result = binary_search(arr_1, 56)
print(result)