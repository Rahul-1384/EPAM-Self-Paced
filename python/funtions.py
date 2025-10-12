def fun():
    print("This is normal function declaration")
fun()


# Types of Arguments

# 1) Positional arguments
def fun(a, b):
    print(a+b)

fun(2, 3)

# 2) Arbitrary Arguments
def fun(*args):
    print(args)

fun("Rahul", 20, "Manish")

# 3) Keyword Arguments
def fun(name, age):
    print(name, age)

fun(name = "Rahul", age = 20)

# 4) Arbitrary Keyword Arguments
def fun(**kwargs):
    print(kwargs)

fun(name = "Rahul", age = 20)

# 5) Default Arguments and Optional Arguments
def fun(city = "Mathura"):
    print(city)

fun("Jhansi")
fun()

# 6) Positional-Only Arguments
def fun(a, b, /):
    print(a+b)

fun(2,3)

# 7) Keyword-Only Arguments
def fun(*, name, age):
    print(name, age)

fun(name = "Rahul", age = 20)

# 8) Combined Positional-Only and Keyword-Only
def fun(a, b, /, *, name, age):
    print(a, b, name, age)

fun(2, 3, name = "Rahul", age = 20)


# Rules to write arguments in an order
def fun(a, b, /, c, d, *args, e, **kwargs):
    print(a,b,c,d,args,e,kwargs)

fun(1, 2, 3, 4, "Rahul", e = 10, f = 11)