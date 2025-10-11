print("Hello World!")

a = 2
print(a)
print(type(a))

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)