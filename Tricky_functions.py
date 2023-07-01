def outer_function(x):
    def inner_function():
        return x

    x -= 2
    return inner_function()


print(outer_function(5))
