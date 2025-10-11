# Global variable
a = 2
def fun():
    a = 2
    print("Local variable:",a)
fun()
print("Global variable:",a)