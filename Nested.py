#First definition
def factorial (nbs):
    """Returns the factorial of n."""

    def recurse(nbs, product):
        """Helper function to compute factorial."""
        if nbs == 1: return product
        else:
            return recurse(nbs - 1, nbs * product)

    return recurse(nbs,1)

print(factorial(7))


text = "Nicole"
print(len(text))

lyst1 = [2, 4, 8]
lyst2 = list(lyst1)
lyst1 == lyst2