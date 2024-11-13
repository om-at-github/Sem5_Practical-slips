## cd slip1
## python remove_duplicates_list.py
## remove duplicates elements from a list.

# Method 1:Using a Loop
# list = [1,1,1,3,3,2,5,5,6,7,7,7,8,9,0,0,0,1,11,10]

# for num in list:
 #   list.remove(num)
  #  print(list)


my_list = [1, 2, 2, 3, 4, 4, 5]

# Method 2: Using a Set
unique_list_set = list(set(my_list))
print("Using set:", unique_list_set)
    