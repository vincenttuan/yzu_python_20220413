# 繼承 __init__, __str__
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(Person):
    grade = 0
    def __init__(self, name, age, sex, grade):
        # super 在此指的就是 Person
        super.__init__(name, age, sex)  # 調用 Person 的 __init__ 方法
        self.grade = grade

if __name__ == '__main__':
    student = Student('Vincent', 18, 'M', 8)
