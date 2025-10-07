def bubble_sort(arr_nbs):
    n_nbs = len(arr_nbs)
    for i_nbs in range (n_nbs):
        for j_nbs in range (0, n_nbs-1-1):
            if arr_nbs[j_nbs] > arr_nbs [j_nbs + 1]:
                arr_nbs[j_nbs], arr_nbs[j_nbs + 1] = arr_nbs[j_nbs + 1], arr_nbs[j_nbs]

    return arr_nbs
arr_nbs = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr_nbs)
sorted_arr = bubble_sort(arr_nbs)
print("Sorted array:", sorted_arr)