def selection_sort(arr_nbs):
    n_nbs = len(arr_nbs)
    
    for i_nbs in range(n_nbs):
        min_idx_nbs = i_nbs
        for j_nbs in range(i_nbs + 1, n_nbs):
            if arr_nbs[j_nbs] < arr_nbs[min_idx_nbs]:
                min_idx_nbs = j_nbs
        arr_nbs[i_nbs], arr_nbs[min_idx_nbs] = arr_nbs[min_idx_nbs], arr_nbs[i_nbs]
    
    return arr_nbs

arr_nbs = [5, 3, 8, 4, 2]
print("Original array:", arr_nbs)
print("Sorted array:", selection_sort(arr_nbs))