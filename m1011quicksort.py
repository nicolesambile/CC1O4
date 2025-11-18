def quick_sort(arr_nbs):
    if len(arr_nbs) <= 1:
        return arr_nbs

    pivot_nbs = arr_nbs[len(arr_nbs) // 2]
    left_nbs = [x_nbs for x_nbs in arr_nbs if x_nbs < pivot_nbs]
    middle_nbs = [x_nbs for x_nbs in arr_nbs if x_nbs == pivot_nbs]
    right_nbs = [x_nbs for x_nbs in arr_nbs if x_nbs > pivot_nbs]

    return quick_sort(left_nbs) + middle_nbs + quick_sort(right_nbs)

arr_nbs = [5, 3, 8, 4, 2]
print("Original array:", arr_nbs)
print("Sorted array:", quick_sort(arr_nbs))