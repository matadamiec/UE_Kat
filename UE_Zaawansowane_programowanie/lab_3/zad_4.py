"""
Zad 4
Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool
"""


def check_sum(number_one: int, number_two: int, number_three: int) -> bool:
    sum_to_check = number_one + number_two
    if sum_to_check >= number_three:
        return True
    else:
        return False


print("check_sum result:")
print(check_sum(10, 5, 15))
