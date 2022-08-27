class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avarage(self):
        from statistics import mean
        avarage = round(mean(self.grades[grades] for grades in self.grades), 2)
        self.avarage = avarage
        return avarage

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avarage(self):
        all_rates = [grade in self.grades.values() for grade in self.grades]
        # from statistics import mean
        # avarage = round(mean(self.grades[grades] for grades in self.grades), 2)
        return round(sum(all_rates) / len(all_rates), 2)

    def __str__(self):
        res_lec = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avarage()}'
        return res_lec


class Reviewer(Mentor):

    def __str__(self):
        res_rew = f'Reviewer \nИмя: {self.name} \nФамилия: {self.surname}'
        return res_rew

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Gun', 'Knife']
student_one = Student('Yo', 'Yo', 'male')
student_two = Student('Big', 'Boy', 'male')
student_one.courses_in_progress += ['Knife', 'Python', 'Git', 'Survation']
student_two.courses_in_progress += ['Gun']
lect_1 = Lecturer('Alex', 'Manuiloff')
lect_1.courses_attached += ['Knife', 'Gun']

new_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('John', 'Rembo')
second_reviewer.courses_attached += ['Survation']
new_reviewer.courses_attached += ['Python', 'Knife']

new_reviewer.rate_hw(best_student, 'Python', 10)
new_reviewer.rate_hw(best_student, 'Python', 10)
new_reviewer.rate_hw(best_student, 'Python', 10)
new_reviewer.rate_hw(student_one, 'Knife', 9)
new_reviewer.rate_hw(student_one, 'Knife', 6)
new_reviewer.rate_hw(student_one, 'Knife', 8)
new_reviewer.rate_hw(student_one, 'Knife', 10)

student_one.rate_lecturer(lect_1, 'Knife', 9)
student_one.rate_lecturer(lect_1, 'Knife', 6)
student_one.rate_lecturer(lect_1, 'Knife', 6)
student_one.rate_lecturer(lect_1, 'Knife', 8)
best_student.rate_lecturer(lect_1, 'Knife', 9)
student_two.rate_lecturer(lect_1, 'Gun', 8)

print(best_student.grades)
print(second_reviewer)
print(lect_1.avarage())


