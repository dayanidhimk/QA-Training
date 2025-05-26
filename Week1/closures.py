def outer():
    var1 = 10

    def inner():
        nonlocal var1
        print("Value of \'var1\' variable from outer() :", var1)
    
    return inner()

outer()