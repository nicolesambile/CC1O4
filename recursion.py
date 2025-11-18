def factorial (n_ss):
    if n_ss == 0: #base case
        return 1
    return n_ss * factorial (n_ss - 1) #recursive case

print(factorial(5))