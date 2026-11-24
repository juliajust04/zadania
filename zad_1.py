class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self) -> str:
        return f"Student: {self.name}, oceny: {self.marks}"


if __name__ == "__main__":
    student1 = Student("Julia", [80, 70, 90])
    student2 = Student("Adam", [20, 40, 30])

    print(student1.is_passed())
    print(student2.is_passed())