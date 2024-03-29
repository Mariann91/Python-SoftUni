x = "global"  # global variable


def outer():
    x = "local"  # local variable

    def inner():
        nonlocal x 
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
