def insertion_sort(arr_nbs):
    for i_nbs in range(1, len(arr_nbs)):
        key_nbs = arr_nbs[i_nbs]
        j_nbs = i_nbs - 1

        while j_nbs >= 0 and key_nbs < arr_nbs[j_nbs]:
            arr_nbs[j_nbs + 1] = arr_nbs[j_nbs]
            j_nbs -= 1

        arr_nbs[j_nbs + 1] = key_nbs

    return arr_nbs

arr_nbs = [5, 3, 8, 4, 2]
print("Original array:", arr_nbs)
print("Sorted array:", insertion_sort(arr_nbs))