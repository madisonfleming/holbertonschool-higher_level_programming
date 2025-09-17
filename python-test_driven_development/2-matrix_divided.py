#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

    Args:
        matrix - list of integers or floats
        div - individual num in matrix

    Returns:
        divided matrix

    Raises:
        TypeError: if values are not an int or float
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    first_row = len(matrix[0])
    for row in matrix:
            if len(row) != first_row:
                raise TypeError("Each row of the matrix must have the same size")
            for element in row:
                 if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

"""
if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")

    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
"""
