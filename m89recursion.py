def factorial(n_nbs):
    if n_nbs == 0:
        return 1
    return n_nbs * factorial(n_nbs - 1)

def fibonacci(n_nbs):
    if n_nbs <= 1:
        return n_nbs
    return fibonacci(n_nbs - 1) + fibonacci(n_nbs - 2)

def merge_sort(arr_nbs):
    if len(arr_nbs) > 1:
        mid_nbs = len(arr_nbs) // 2
        left_nbs = arr_nbs[:mid_nbs]
        right_nbs = arr_nbs[mid_nbs:]

        merge_sort(left_nbs)
        merge_sort(right_nbs)

        i_nbs = j_nbs = k_nbs = 0

        while i_nbs < len(left_nbs) and j_nbs < len(right_nbs):
            if left_nbs[i_nbs] < right_nbs[j_nbs]:
                arr_nbs[k_nbs] = left_nbs[i_nbs]
                i_nbs += 1
            else:
                arr_nbs[k_nbs] = right_nbs[j_nbs]
                j_nbs += 1
            k_nbs += 1

        while i_nbs < len(left_nbs):
            arr_nbs[k_nbs] = left_nbs[i_nbs]
            i_nbs += 1
            k_nbs += 1

        while j_nbs < len(right_nbs):
            arr_nbs[k_nbs] = right_nbs[j_nbs]
            j_nbs += 1
            k_nbs += 1
    return arr_nbs 

print("factorial of 5:", factorial(5))
print("fibonacci of 10:", fibonacci(10))