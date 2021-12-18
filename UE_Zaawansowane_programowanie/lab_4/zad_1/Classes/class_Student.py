class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute_marks(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False
