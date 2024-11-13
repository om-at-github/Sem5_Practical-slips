## cd slip8
## python repeated_items_of_a_tuple.py
## Write a python script to find the repeated items of a tuple 

def find_repeated_items(tup):
    repeated_items = []
    seen = set()
    for item in tup:
        if item in seen:
            if item not in repeated_items:
                repeated_items.append(item)
        else:
            seen.add(item)
    return repeated_items

# Example usage:
tuple1 = (1, 2, 3, 2, 4, 5, 3, 6, 3)
repeated = find_repeated_items(tuple1)
print("Repeated items in the tuple:", repeated)
