def fun():
    print("This is normal function declaration")
fun()


# arbitrary arguments(*args) just like rest operator in JS
def my_fun(*args):
    print(args)
my_fun("Rahul", "Manish", "Yashvi")