class Person():

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def description(self):
        return f"{self.name} is {self.age} years old and is an {self.occupation}"

    def speak(self, sound):
        return f"{self.name} says {sound}"


Patrick = Person("Patrick", 21, 'engineer')

print(Patrick.description())

print(Patrick.speak("hello"))
