def argument_text_natural_number(func):
    def inner(num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Wrong argument for this func, expected positive integer")
        else:
            return func(num)
    return inner


@argument_text_natural_number
def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num - 1) * num


print(factorial(3))
