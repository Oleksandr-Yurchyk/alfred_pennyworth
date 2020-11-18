def input_until_sum_not_equal_zero():
    summa = 0
    squares_sum = 0
    while True:
        number_from_input = int(input())
        summa += number_from_input
        squares_sum += number_from_input ** 2
        if summa == 0:
            return squares_sum


print(input_until_sum_not_equal_zero())
