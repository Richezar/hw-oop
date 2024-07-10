def average(rate):
    s = 0
    l = 0
    for k, v in rate.items():
        l += len(v)
        s += sum(v)
    return round(s / l, 1)

def stud_rate_course(students, course):
    res = ''
    i = 0
    for student in students:
        for name, grades in student.items():
            for cours, grade in grades.items():
                if cours == course:
                    res += f'{name}, "Python" = {str(round(sum(grade) / len(grade), 1))}\n'
    return res

def lector_rate_course(lecotrs, course):
    res = ''
    i = 0
    for lector in lecotrs:
        for name, grades in lector.items():
            for cours, grade in grades.items():
                if cours == course:
                    res += f'{name}, "Python" = {str(round(sum(grade) / len(grade), 1))}\n'
    return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # оконченные курсы
        self.courses_in_progress = [] # курсы в процессе изучения
        self.grades_student = {} # оценки студента

    def __eq__(self, other):
        return average(self.grades_student) == average(other)

    def __lt__(self, other):
        return average(self.grades_student) < average(other)

    def __le__(self, other):
        return average(self.grades_student) <= average(other)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average(self.grades_student)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def rate_at(self, student, lecturer, course, score):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades_lector:
                lecturer.grades_lector[course] += [score]
            else:
                lecturer.grades_lector[course] = [score]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = [] # предметы учителя
        self.grades_lector = {} # оценки учителя

    def __eq__(self, other):
        return average(self.grades_lector) == average(other)

    def __lt__(self, other):
        return average(self.grades_lector) < average(other)

    def __le__(self, other):
        return average(self.grades_lector) <= average(other)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average(self.grades_lector)}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = [] # предметы проверяющего

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'



student1 = Student('Mike', 'Lambert', 'male')
student2 = Student("Travis", 'Bell', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['English']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['English']
student2.finished_courses += ['Box']
reviewer1 = Reviewer('John', 'Snyder')
reviewer2 = Reviewer('Duane', 'Evans')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['English']

lector1 = Lecturer('Some', 'Buddy')
lector2 = Lecturer('David', 'Smith')
lector1.courses_attached += ['Python']
lector2.courses_attached += ['Python', 'English']

student1.rate_at(student1, lector1, "Python", 9)
student1.rate_at(student1, lector1, "Python", 10)
student2.rate_at(student2, lector2, "English", 5)
student2.rate_at(student2, lector2, "English", 3)
student2.rate_at(student2, lector2, "Python", 10)
student2.rate_at(student2, lector2, "Python", 5)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student1, 'English', 9)
reviewer2.rate_hw(student1, 'English', 10)
reviewer2.rate_hw(student1, 'English', 7)
reviewer1.rate_hw(student2, 'Python', 2)
reviewer1.rate_hw(student2, 'Python', 4)
reviewer1.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'English', 1)
reviewer2.rate_hw(student2, 'English', 3)
reviewer2.rate_hw(student2, 'English', 6)

print(student1.name, student1.surname, student1.courses_in_progress, student1.grades_student, student1.finished_courses, student1.gender, sep='\n')
print()
print(student2.name, student2.surname, student2.courses_in_progress, student2.grades_student, student2.finished_courses, student2.gender, sep='\n')
print()
print(reviewer1.__str__(), reviewer2.__str__(), sep='\n\n')
print()
print(lector1.__str__(), lector2.__str__(), sep='\n\n')
print()
print(student1.__str__(), student2.__str__(), sep='\n\n')

print('Средний балл студента_1 больше ли среднего балла студента_2?', student2.__lt__(student1.grades_student), f'студент_1 = {average(student1.grades_student)} студент_2 = {average(student2.grades_student)}', sep='\n')
print('Средний балл студента_1 равен ли среднему баллу студента_2?', student2.__eq__(student1.grades_student), f'студент_1 = {average(student1.grades_student)} студент_2 = {average(student2.grades_student)}', sep='\n')
print('Средний балл студента_1 больше или равен среднему баллу студента_2?', student2.__le__(student1.grades_student), f'студент_1 = {average(student1.grades_student)} студент_2 = {average(student2.grades_student)}', sep='\n')
print('Средний балл лектор_1 больше ли среднего балла лектор_2?', lector2.__lt__(lector1.grades_lector), f'лектор_1 = {average(lector1.grades_lector)} лектор_2 = {average(lector2.grades_lector)}', sep='\n')
print('Средний балл лектор_1 равен ли среднему баллу лектор_2?', lector2.__eq__(lector1.grades_lector), f'лектор_1 = {average(lector1.grades_lector)} лектор_2 = {average(lector2.grades_lector)}', sep='\n')
print('Средний балл лектор_1 больше или равен среднему баллу лектор_2?', lector2.__le__(lector1.grades_lector), f'лектор_1 = {average(lector1.grades_lector)} лектор_2 = {average(lector2.grades_lector)}', sep='\n')
print()
stud = [{student1.name + ' ' + student1.surname : student1.grades_student}, {student2.name + ' ' + student1.surname : student2.grades_student}]
cstud = 'Python'
print(stud_rate_course(stud, cstud))
lect = [{lector1.name + ' ' + lector1.surname : lector1.grades_lector}, {lector2.name + ' ' + lector2.surname : lector2.grades_lector}]
clect = 'Python'
print(lector_rate_course(lect, clect))