"""
Zad 4.1
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy ocena jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
"""
from lab_4.zad_1.Classes.class_Student import Student

stud_1 = Student("John", 36)
stud_2 = Student("Adam", 51)
print("stud_1.compute_marks results:")
print(stud_1.compute_marks())
print("stud_2.compute_marks results:")
print(stud_2.compute_marks())
