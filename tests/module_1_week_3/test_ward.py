from homework.module_1_week_3.ward import Ward, Student, Teacher, Doctor


def test_student_describe(capfd):
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    student1.describe()
    # output
    # >> Student - Name : studentA - YoB : 2010 - Grade : 7
    out, err = capfd.readouterr()
    assert out.strip() == "Student:  studentA , yob: 2010, grade: 7"


def test_teacher_describe(capfd):
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher1.describe()
    # output
    # >> Teacher:  teacherA , yob: 1969, subject:  Math
    out, err = capfd.readouterr()
    assert out.strip() == "Teacher:  teacherA , yob: 1969, subject:  Math"


def test_doctor_describe(capfd):
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    doctor1.describe()
    # output
    # >> Doctor - Name : doctorA - YoB : 1945 - Specialist : Endocrinologists
    out, err = capfd.readouterr()
    assert out.strip() == "Doctor:  doctorA , yob: 1945, specialist:  Endocrinologists"


def test_ward(capfd):
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ", people=[])
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    out, err = capfd.readouterr()
    assert out.strip() == '''Ward:  Ward1 
Student:  studentA , yob: 2010, grade: 7
Teacher:  teacherA , yob: 1969, subject:  Math 
Teacher:  teacherB , yob: 1995, subject:  History 
Doctor:  doctorA , yob: 1945, specialist:  Endocrinologists 
Doctor:  doctorB , yob: 1975, specialist:  Cardiologists'''
    assert ward1.count_doctor() == 2
    assert round(ward1.compute_average(), 1) == 1982.0


def test_ward_sort_age(capfd):
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ", people=[])
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.sort_age()
    ward1.describe()
    out, err = capfd.readouterr()
    assert out.strip() == '''Ward:  Ward1 
Doctor:  doctorA , yob: 1945, specialist:  Endocrinologists 
Teacher:  teacherA , yob: 1969, subject:  Math 
Doctor:  doctorB , yob: 1975, specialist:  Cardiologists 
Teacher:  teacherB , yob: 1995, subject:  History 
Student:  studentA , yob: 2010, grade: 7'''
