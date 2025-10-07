import time
#O(1) access
arr_nbs = list(range(1000000))

start_nbs = time.time()
x_nbs = arr_nbs[500000] #constant time
end_nbs = time.time()

print("O(1) access time:", end_nbs - start_nbs)

#O(n) search
target_nbs = 999999
start_nbs = time.time()
found_nbs = target_nbs in arr_nbs

# linear search
end_nbs = time.time()
print("O(n) search time:", end_nbs - start_nbs)



