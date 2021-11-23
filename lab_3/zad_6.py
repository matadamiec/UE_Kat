"""
Zad 6
Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
"""


def merge_two_lists(first_list:  list, second_list:  list) -> list:
    merged_list = list(set(first_list + second_list))
    for x in range(len(merged_list)):
        merged_list[x] = merged_list[x] ** 3

    return merged_list


print("merge_two_lists result:")
print(merge_two_lists([1, 2, 3, 4], [4, 5]))
