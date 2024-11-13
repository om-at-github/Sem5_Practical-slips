""""
cd slip11
python compute_element_wise_sum_of_given_tuples.py

Write a Python program to compute element-wise sum of given tuples.
Original lists: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
Element-wise sum of the said tuples: (6, 9, 8, 6)
"""
tuple1 = [1,2,3,4]
tuple2 = [3,5,2,1]
tuple3 = [2,2,3,1]

def sumTupple(tup1,tup2):
    addition = 0
    sum =[]
    i=0
    for x  in tup1:
        addition = x + tup2[i]
        sum.append(addition)
        i=i+1

    return sum

val1 = sumTupple(tuple1,tuple2)
val2 = sumTupple(val1,tuple3)
print("the sum of two tupple is",val2)

    