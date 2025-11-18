def merge_sort(arr_nbs):
    if len(arr_nbs) > 1:
        mid_nbs = len(arr_nbs) // 2
        L_nbs = arr_nbs[:mid_nbs]
        R_nbs = arr_nbs[mid_nbs:]

        merge_sort(L_nbs)
        merge_sort(R_nbs)

        i_nbs = j_nbs = k_nbs = 0
        while i_nbs < len(L_nbs) and j_nbs < len(R_nbs):
            if L_nbs[i_nbs] < R_nbs[j_nbs]:
                arr_nbs[k_nbs] = L_nbs[i_nbs]
                i_nbs += 1
            else:
                arr_nbs[k_nbs] = R_nbs[j_nbs]
                j_nbs += 1
            k_nbs += 1
        while i_nbs < len(L_nbs):
            arr_nbs[k_nbs] = L_nbs[i_nbs]
            i_nbs += 1
            k_nbs += 1
        while j_nbs < len(R_nbs):
            arr_nbs[k_nbs] = R_nbs[j_nbs]
            j_nbs += 1
            k_nbs += 1

    return arr_nbs

arr_nbs = [5, 3, 8, 4, 2]
print("Original array:", arr_nbs)
print("Sorted array:", merge_sort(arr_nbs))