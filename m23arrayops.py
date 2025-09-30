#Python list as array

arr_nbs = [10, 20, 30, 40, 50]

#o(1) access
print("first element:", arr_nbs[0])
print("last element:", arr_nbs[-1])

#O(n) traversal
for x in arr_nbs:
    print(x)


#O(n) insertion (worst case)
arr_nbs.insert(0, 5)
print("after insertion:", arr_nbs )

#O(n) deletion
arr_nbs.remove(30)
print("after deletion:", arr_nbs)
