a = [1,2,3,4,5,6]
print(a[0:4])


# List Comprehension
# Baisc generation
squares = [x*x for x in range(1,6)]
print(squares)

# Filtering
numbers = [1,2,3,4,5,6,7]
new_list = [x for x in numbers if x%2 == 0]
print(new_list)


# Unpacking
numbers = [10, 20, 30, 40, 50]
a, b, c, *d = numbers
print(a,b,c,d)