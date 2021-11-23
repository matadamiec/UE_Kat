"""
Zad 5
Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
. Funkcja ma sprawdzić, czy lista z parametru pierwszego zawiera taką wartość
jaką przekazano w parametrze drugim.
"""


def check_if_list_contain(list_to_check:  list, item_to_check: int) -> bool:
    if item_to_check in list_to_check:
        return True
    else:
        return False


print("check_if_list_contain result:")
print(check_if_list_contain([5, 6, 7, 8], 10))
