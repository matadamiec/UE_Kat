def print_names(names: [str]):
    print(f"Podane imiona to: {names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}")


def print_multiplied_numbers(numbers: [int]):
    numbers_to_print = ""
    for number in numbers:
        numbers_to_print += "," + str(number * 2)
    numbers_to_print = numbers_to_print.replace(",", "", 1)
    numbers_to_print_2 = [number * 2 for number in numbers]
    print("Wyniki mnożenia liczb:")
    print(f"a) Podane liczby pomnożone przez 2 to: {numbers_to_print}")
    print(f"b) Podane liczby pomnożone przez 2 to: {numbers_to_print_2}")


def print_only_even_numbers(numbers: [int]):
    numbers_to_print = ""
    for x in range(len(numbers)):
        if numbers[x] % 2 == 0:
            numbers_to_print += "," + str(numbers[x])

    numbers_to_print = numbers_to_print.replace(",", "", 1)
    print(f"Liczby parzyste to: {numbers_to_print}")


def print_every_other(numbers: [int]):
    numbers_to_print = ""
    for x in range(len(numbers)):
        if x % 2 == 0:
            numbers_to_print += "," + str(numbers[x])

    numbers_to_print = numbers_to_print.replace(",", "", 1)
    print(f"Co druga liczba {numbers_to_print}")


print_names(["xyz", "Imie_2", "Imie_3", "Imie_4", "Imie_5"])
print_multiplied_numbers([1, 3, 5, 7, 9])
print_only_even_numbers([1, 2, 5, 6, 9, 10])
print_every_other([1, 2, 5, 6, 9, 10])
