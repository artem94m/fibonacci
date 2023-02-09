def fibonacci_n(n_index):
    """Calculates n Fibonacci number. Time O(N)

        n_index must be non-negative integer
    """
    if (is_non_negative_int(n_index)):
        if (0 <= n_index <= 1):
            result = n_index
        elif (n_index > 1):
            n_minus_2 = 0
            n_minus_1 = 1

            for _current_n_index in range(2, n_index + 1):
                result = n_minus_2 + n_minus_1

                n_minus_2, n_minus_1 = n_minus_1, result

        return result
    else:
        raise ValueError


def fibonacci_logn(n_index):
    """Calculates n Fibonacci number. Time O(LogN)

        n_index must be non-negative integer

        It uses the next ratio (https://en.wikipedia.org/wiki/Fibonacci_number):\n
        |1  1|n    |Fn+1   Fn|                                                  \n
        |1  0|  =  |Fn   Fn-1|
    """
    if (is_non_negative_int(n_index)):
        base_matrix = [
            [1, 1],
            [1, 0],
        ]

        if (0 <= n_index <= 1):
            result = n_index
        elif (n_index > 1):
            # in order to get n-th number we need a base matrix to the power of n-1
            exp_matrix = __pow_m2x2(base_matrix, n_index - 1)
            # then we can use matrix[0][0] value (Fn+1)
            result = exp_matrix[0][0]

        return result
    else:
        raise ValueError


def is_non_negative_int(obj):
    result = False

    if (type(obj) is int and obj >= 0):
        result = True

    return result


def __pow_m2x2(matrix, exp):
    """Raises a matrix size of 2x2 to a power of exp

        The matrix must be a list (length 2) of lists (both of them are also length 2, containing ints). Like this:
            matrix = [
                [1, 2],
                [3, 4],
            ]

        The exp must be non-negative integer.

        Validation of the "matrix" and "exp" params is not performed because:
            - the function is not for public use
            - in effort to reduce execution time
    """
    if (exp == 0):
        result = [
            [1, 0],
            [0, 1],
        ]
    elif (exp == 1):
        result = matrix
    elif (exp == 2):
        result = __multiply_m2x2(matrix, matrix)
    elif (exp > 2):
        quotient, remainder = divmod(exp, 2)

        result = __pow_m2x2(__pow_m2x2(matrix, quotient), 2)
        if (remainder):
            result = __multiply_m2x2(result, matrix)

    return result


def __multiply_m2x2(m1, m2):
    """Multiplies two matrices size of 2x2

        The matrix must be a list (length 2) of lists (both of them are also length 2, containing ints). Like this:
            matrix = [
                [1, 2],
                [3, 4],
            ]

        Validation of the "m1" and "m2" params is not performed because:
            - the function is not for public use
            - in effort to reduce execution time
    """
    return [
        [m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
        [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]],
    ]
