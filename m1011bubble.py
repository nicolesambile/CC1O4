def bubble_sort(arr_nbs):
    n_nbs = len(arr_nbs)
    for i_nbs in range(n_nbs):
        for j_nbs in range(0, n_nbs - i_nbs - 1):
            if arr_nbs[j_nbs] > arr_nbs[j_nbs + 1]:
                arr_nbs[j_nbs], arr_nbs[j_nbs + 1] = arr_nbs[j_nbs + 1], arr_nbs[j_nbs]
    return arr_nbs

arr_nbs = [5, 3, 8, 4, 2]
print("Original array:", arr_nbs)
print("Sorted array:", bubble_sort(arr_nbs))