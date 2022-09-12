class Employee():

    def __init__(self, first_name, last_name, age, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'


emp1 = Employee('Patrick', 'Lauzon', 25, 60000)
emp2 = Employee('John', 'Doe', 21, 37000)

print(emp1.email)
print(emp2.email)
