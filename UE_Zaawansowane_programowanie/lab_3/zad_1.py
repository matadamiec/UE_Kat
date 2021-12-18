"""
Zad 1
Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
wyświetlić ( print)
"""


def name_and_surname(name: str, surname: str) -> str:
    return str("Cześć " + name + " " + surname + "!")


result = name_and_surname("Mateusz", "Adamiec")
print("name_and_surname result:")
print(result)
