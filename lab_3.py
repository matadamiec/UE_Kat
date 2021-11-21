"""
Zad 1
Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
wyświetlić ( print)
"""


def name_and_surname(name: str, surname: str) -> str:
    full_name = str("Cześć " + name + " " + surname + "!")
    return full_name


result = name_and_surname("Mateusz", "Adamiec")
print("name_and_surname result:")
print(result)


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


"""
Zad 3
Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
"Liczba nieparzysta"
"""


def check_if_even(number_to_check: int) -> bool:
    check_results = number_to_check % 2
    if check_results == 0:
        return True
    else:
        return False

print("check_if_even result:")
check_if_even_result = check_if_even(3)
if check_if_even_result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

"""
Zad 4
Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool
"""


def check_sum(number_one:  int, number_two: int, number_three: int) -> bool:
    sum_to_check = number_one + number_two
    if sum_to_check >= number_three:
        return True
    else:
        return False


print("check_sum result:")
print(check_sum(10, 5, 15))

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
