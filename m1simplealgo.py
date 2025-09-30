#Sum of first n Numbers - interative vs formula

def sum_interative(n):
    total_nbs=0
    for i in range (1, n+1 ):
     total_nbs += 1
     return total_nbs

def sum_formula(n):
    return n *(n + 1) // 2

print(sum_interative(10)) #O(n)
print(sum_formula(10)) #O(n)