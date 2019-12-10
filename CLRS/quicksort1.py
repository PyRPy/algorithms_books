# quick sort - different version in python
# https://stackoverflow.com/questions/18262306/quicksort-with-python
def quicksort(xs):
    """given indexable and slicable iterable, return a sorted list"""
    if xs:
        pivot = xs[0]
        below = [i for i in xs[1:] if i < pivot]
        above = [i for i in xs[1:] if i >= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else:
        return xs

# this one use comprehension heavily

xs = [1, 5, 6, 3, 9, 8]

xs_sorted = quicksort(xs)
print(xs)
print(xs_sorted)

# another version
q = lambda x:x and q([i for i in x[1:] if i <=x[0]]) + [x[0]] + \
    q([i for i in x[1:] if i > x[0]])

print(q(xs))
