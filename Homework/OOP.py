class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lector) and (course in self.courses_in_progress or course in self.finished_courses) and \
                course in lector.courses:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return "Ошибка"

    def get_average(self):
        count_grades = 0
        sum_of_grades = 0
        for course in self.grades:
            for grade in self.grades[course]:
                count_grades += 1
                sum_of_grades += grade
        return round(sum_of_grades / count_grades, 1)

    def __str__(self):
        text = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Средняя оценка за домашние задания: {self.get_average()}',
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}',
            f'Пройденые курсы: {", ".join(self.finished_courses)}',
        ]
        return '\n'.join(text)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.get_average() < other.get_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = self.courses_attached
        self.grades = {}

    @property
    def get_average(self):
        count_grades = 0
        sum_of_grades = 0
        for course in self.grades:
            for grade in self.grades[course]:
                count_grades += 1
                sum_of_grades += grade
        return round(sum_of_grades / count_grades, 1)

    def __str__(self):
        text = [
            f'Имя: {self.name}',
            f'Фамилия: {self.surname}',
            f'Средняя оценка за лекции: {self.get_average}'
        ]
        return '\n'.join(text)

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Не является лектором')
            return
        return self.get_average < other.get_average


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    @staticmethod
    def rate_student(student, course, grade):
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        text = [
            f'Имя: {self.name}',
            f'Имя: {self.surname}'
        ]
        return '\n'.join(text)


# initial settings
lector1 = Lector('Глеб', "Головин")
lector1.courses += ['Python']
lector1.courses += ['JS']

lector2 = Lector('Вячеслав', "Ягодкин")
lector2.courses += ['Python']

student1 = Student('Николай', "Иванов", 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['JS']
student1.finished_courses += ['Введение в программирование']
student1.rate_lecture(lector1, 'Python', 10)
student1.rate_lecture(lector2, 'Python', 4)

student2 = Student('Иван', "Вчерашний", 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']
student2.rate_lecture(lector1, 'Python', 6)
student2.rate_lecture(lector2, 'Python', 10)

reviewer1 = Reviewer('Олег', 'Новиков')
reviewer1.rate_student(student1, 'Python', 10)
reviewer1.rate_student(student1, 'Python', 5)
reviewer1.rate_student(student1, 'JS', 10)
reviewer1.rate_student(student2, 'Python', 7)
reviewer1.rate_student(student2, 'Python', 9)
# end initial settings

print(f'Проверяющий: \n{reviewer1}\n')

print(f'Лектор1: \n{lector1}\n')

print(f'Лектор2: \n{lector2}\n')

print(f'Студент1: \n{student1}\n')
print(f'Студент2: \n{student2}\n')


# print(lector2 > lector1)
# print(student2 < student1)

def get_average_of_student(course, students):
    sum_of_grades = 0
    count_grades = 0
    for student in students:
        for grade in student.grades[course]:
            sum_of_grades += grade
            count_grades += 1
    return f'Средняя оценка за домашние задания по предмету {course}: {round(sum_of_grades / count_grades, 1)}'


def get_average_of_lectors(course, lectors):
    sum_of_grades = 0
    count_grades = 0
    for lector in lectors:
        for grade in lector.grades[course]:
            sum_of_grades += grade
            count_grades += 1
    return f'Средняя оценка за домашние задания по предмету {course}: {round(sum_of_grades / count_grades, 1)}'


print(get_average_of_student('Python', [student1, student2]))
print(get_average_of_lectors('Python', [lector1, lector2]))
