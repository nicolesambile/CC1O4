def insertion_sort(arr):
    for i_nbs in range(1, len(arr_nbs)):
        key_nbs = arr[i_nbs]
    j_nbs = i_nbs - 1
    while j_nbs >= 0 and key_nbs < arr[j_nbs]:
        arr[j_nbs + 1] = arr[j_nbs]
        j_nbs -= 1
        
    return arr
arr_nbs = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr_nbs)
sorted_arr = insertion_sort(arr_nbs)
print("Sorted array:", sorted_arr)