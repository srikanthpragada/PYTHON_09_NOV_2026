class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    @property
    def kind(self):
        return "Major" if self.age >= 18 else 'Minor'



p1 = Person("Andy", 20)
print(p1.kind)    # used as property

p2 = Person("Mark", 25)
p3 = Person("Andy", 20)

print(p1)  # str(p1)  -> p1.__str__()
print(p1 == p3)  # p1.__eq__(p3)
print(p1 != p2)  # p1.__eq__(p2)
print(p2 > p1)  # p2.__gt__(p1)


