num = {1,2,3,4,4}
print(num)


# num = {{1,2,3,4}, "apple"}
# print(num)

s = {1,2,3,4,5,6}
s.add(10)
# s.remove(100)   # remove element(Give error when not found)
# s.discard(100)  # remove element( no error)
s.pop()
print(s)

s = frozenset([1,2,3,4])
print(s)