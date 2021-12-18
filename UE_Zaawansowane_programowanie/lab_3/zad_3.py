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
