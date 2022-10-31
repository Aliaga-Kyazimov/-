import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grade = 0

    def _mean_(self):
        all_grades = []
        for grade in self.grades.keys():
            all_grades += self.grades[grade]
        self.mean_grade = statistics.mean(all_grades)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def give_grade_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние работы: {self.mean_grade} \n'
              f'Курсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if self.mean_grade < other.mean_grade:
                print(f'У студента {other.name} {other.surname} средний балл больше')
            else:
                print(f'У студента {self.name} {self.surname} средний балл больше')
        else:
            print('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        print(f'Имя: {self.name} \nФамилия: {self.surname}')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.mean_grade = 0

    def take_marks(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                print(f'Студент {student.name} {student.surname} имеет следующие оценки: ', student.grades)
            else:
                print('Ошибка')
        else:
            print('Ошибка')

    def _mean_(self):
        all_grades = []
        for grade in self.grades.keys():
            all_grades += self.grades[grade]
        self.mean_grade = statistics.mean(all_grades)

    def __str__(self):
        super().__str__()
        print(f'Средняя оценка за лекции: {self.mean_grade}')

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if self.mean_grade < other.mean_grade:
                print(f'У лектора {other.name} {other.surname} средний балл больше')
            else:
                print(f'У лектора {self.name} {self.surname} средний балл больше')
        else:
            print('Ошибка')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


list_of_students = []
list_of_lecturers = []

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
list_of_students.append(best_student)

bad_student = Student('Vasya', 'Popov', 'man')
bad_student.courses_in_progress += ['Python']
list_of_students.append(bad_student)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

young_reviewer = Reviewer('Once', 'Toldsme')
young_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Rene', 'Descartes')
cool_lecturer.courses_attached += ['Python']
list_of_lecturers.append(cool_lecturer)

young_lecturer = Lecturer('Albert', 'Einstein')
young_lecturer.courses_attached += ['Python']
list_of_lecturers.append(young_lecturer)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
young_reviewer.rate_hw(best_student, 'Python', 8)
young_reviewer.rate_hw(best_student, 'Python', 9)
young_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(bad_student, 'Python', 7)
cool_reviewer.rate_hw(bad_student, 'Python', 6)
cool_reviewer.rate_hw(bad_student, 'Python', 2)
young_reviewer.rate_hw(bad_student, 'Python', 6)
young_reviewer.rate_hw(bad_student, 'Python', 6)
young_reviewer.rate_hw(bad_student, 'Python', 5)

best_student.give_grade_lect(cool_lecturer, 'Python', 10)
bad_student.give_grade_lect(cool_lecturer, 'Python', 8)

best_student.give_grade_lect(young_lecturer, 'Python', 10)
bad_student.give_grade_lect(young_lecturer, 'Python', 5)


def mean_grade(course):
    group = input('Среднюю оценку кого (студенты/лектора), Вы хотите узнать: ')
    list_of = []
    if group == 'Студенты':
        list_of = list_of_students
    elif group == 'Лектора':
        list_of = list_of_lecturers
    else:
        print('Ошибка')
    all_grades = []
    for person in list_of:
        all_grades += person.grades[course]
    all_grades = statistics.mean(all_grades)
    print(f'{group} имеют среднуюю оценку за курс {course}: {round(all_grades, 2)}')


mean_grade('Python')

best_student._mean_()
bad_student._mean_()
cool_lecturer._mean_()
young_lecturer._mean_()

best_student.__lt__(bad_student)
young_lecturer.__lt__(cool_lecturer)

best_student.__str__()
cool_lecturer.__str__()
cool_reviewer.__str__()

cool_lecturer.take_marks(best_student, 'Python')
