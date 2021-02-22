class Person(object):

    pouplation = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopoulation(cls):
        return cls.pouplation


    @staticmethod
    def isAudult(age):
        return age > 10

    def show(self):
        return f'{self.name} {self.age}'

person1 = Person('phucc', 10)

# call class method
print(Person.getPopoulation())

# call static method
print(person1.isAudult(10))

# call its method
print(person1.show())

