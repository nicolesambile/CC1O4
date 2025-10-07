def quick_sort(arr_nbs):
    if len(arr_nbs) <= 1:
        return arr_nbs
    pivot_nbs = arr_nbs[len(arr_nbs) // 2]
    left_nbs = [x for x in arr_nbs if x < pivot_nbs]
    middle_nbs = [x for x in arr_nbs if x == pivot_nbs]
    right_nbs = [x for x in arr_nbs if x > pivot_nbs]
    return quick_sort(left_nbs) + middle_nbs + quick_sort(right_nbs)

arr_nbs = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr_nbs)
sorted_arr = quick_sort(arr_nbs)
print("Sorted array:", sorted_arr)