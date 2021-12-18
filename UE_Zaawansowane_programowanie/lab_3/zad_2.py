"""
Zad 2
Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
mnożenia obu liczb.
"""


def multiply_two_number(number_one: int, number_two: int) -> int:
    multiply_result = number_one * number_two
    return multiply_result


multiply_two_number_result = multiply_two_number(2, 10)
print("multiply_two_number result:")
print(multiply_two_number_result)
