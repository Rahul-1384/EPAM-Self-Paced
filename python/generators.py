def countDown(n):
    while(n > 0):
        yield n
        n -= 1

# for i in countDown(5):
#     print(i)
num = countDown(5)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))