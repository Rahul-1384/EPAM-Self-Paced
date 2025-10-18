nums = [1,2,3]
it = iter(nums)

print(hasattr(nums, '__next__'))
print(hasattr(it, '__next__'))
print(next(it))
print(next(it))
print(next(it))

class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.current <= 0):
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
    
num = CountDown(5)
print(next(num))
print(next(num))

