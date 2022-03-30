class Person:
  def __init__(self, name, age, eyeColor,):
    self.name = name
    self.age = age
    self.eyeColor = eyeColor
    self.speed = 0

  def changeName(self, name):
    self.name = name

  def seteyeColor(self, eyeColor):
    self.eyeColor = eyeColor

  def run(self, speed):
    self.speed += 1

#test comment


p1 = Person("John",36,"Brown")
p2 = Person("Michael",21,"Green")
p3 = Person("Lucas",19,"Black")
p4 = Person("James",12,"Blue")

print(p1.name)
print(p1.age)
print(p1.eyeColor)

p2.changeName("Ole")
print(p2.name)
print(p2.age)
print(p2.eyeColor)

print(p3.name)
print(p3.age)
print(p3.eyeColor)

print(p4.name)
print(p4.age)
print(p4.eyeColor)