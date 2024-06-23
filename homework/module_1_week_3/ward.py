class Ward:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        return sum(isinstance(p, Doctor) for p in self.people)

    def sort_age(self):
        self.people.sort(key=lambda p: p.yob)

    def compute_average(self):
        teachers = [p for p in self.people if isinstance(p, Teacher)]
        if not teachers:
            return None
        return sum(t.yob for t in teachers) / len(teachers)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            person.describe()


class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, yob: {self.yob}, grade: {self.grade}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor: {self.name}, yob: {self.yob}, specialist: {self.specialist}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher: {self.name}, yob: {self.yob}, subject: {self.subject}")
