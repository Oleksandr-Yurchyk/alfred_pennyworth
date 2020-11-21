import logging


# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


print('-----------------------1. double_result-------------------------')
print('This is just func add(5, 5) -->', add(5, 5))  # Should return 10


@double_result
def add(a, b):
    return a + b


print('This is func with @double_result add(5, 5) -->', add(5, 5))  # Should return 20


# 2. only_even_parameters
# This decorator function should only allow a function to have even parameters,
# otherwise return the string "Please only use even numbers!"
def only_even_parameters(func):
    # if args passed to func are not even - return "Please only use even numbers!"
    def inner(*args, **kwargs):
        for i in args:
            if i % 2 != 0:
                return "Please only use even numbers"
            else:
                return func(*args, **kwargs)

    return inner


@only_even_parameters
def add(a, b):
    return a + b


print('--------------------2. only_even_parameters---------------------')
print('This is func with @only_even_param add(5, 5) --> ', add(5, 5))  # Should return "Please only use even numbers!"
print('This is func with @only_even_param add(4, 4) --> ', add(4, 4))  # Should return 8


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print('This is func with @only_even_param multiply(1, 4, 6, 7, 8) --> ',
      multiply(1, 4, 6, 7, 8))  # Should return "Please only use even numbers!"
print('This is func with @only_even_param multiply(2, 4, 6, 8, 10) --> ',
      multiply(2, 4, 6, 8, 10))  # Should return 3840


# 3. logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
def logged(func):
    # log function arguments and its return value
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d %b %y, %H:%M:%S',
                        level=logging.INFO)

    def inner(*args, **kwargs):
        logging.info(f'Arguments for this function are: args - {args}, kwargs - {kwargs}')
        res = func(*args)
        logging.info(f'Result of this function is: {res}')
        return res

    return inner


@logged
def function(*args):
    return 3 + len(args)


print('--------------------------3. logged-----------------------------')
print('This is func with @logged function(4, 4, 4) --> ', function(4, 4, 4))  # Should return 6


# 4. type_check (see pass_args_to_decorator.py from lecture for example)
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print("Bad Type"), otherwise function should be executed.
def type_check(correct_type):
    def type_decorator(func):
        def inner(param):
            if type(param) == correct_type:
                return func(param)
            else:
                return 'Bad Type'

        return inner

    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


print('------------------------4. type_check---------------------------')
print('This is func with @type_check times2(2) --> ', times2(2))  # Should return 4
print('This is func with @type_check times2("Not A Number") --> ',
      times2('Not A Number'))  # "Bad Type" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print('This is func with @type_check first_letter("Hello World") --> ', first_letter('Hello World'))
print('This is func with @type_check first_letter(["Not", "A", "String"]) --> ',
      first_letter(['Not', 'A', 'String']))  # "Bad Type" should be printed, since non-str passed to decorated function
