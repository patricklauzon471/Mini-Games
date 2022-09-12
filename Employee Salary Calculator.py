class Employee():

    def __init__(self, experience, age, GPA):

        self.experience = experience
        self.age = age
        self.GPA = GPA
        self.salary = 20000*(experience/1.4)*(age/20)*(GPA/2.2)


emp1 = Employee(4, 35, 3.5)
emp2 = Employee(10, 10, 3.5)

print(emp1.salary)
print(emp2.salary)
