class Bil:
  ms = 1000/3600
  currentSpeed = 0
  distanceRun = 0
  def __init__(self, name, brand,acceleration):
    self.name = name
    self.brand = brand
    self.acceleration = acceleration

  def speedup(self, ):
    self.currentSpeed += self.acceleration
  def brake(self, ):
    self.currentSpeed -= self.acceleration
  def getName(self,):
    return self.name
  def getSpeed(self):
    return self.currentSpeed
  def getDistance(self):
    self.distanceRun += 100 * self.ms
    return self.distanceRun


b1 = Bil("BMW","El",110)
b2 = Bil("Toyota","benzin",100)
b3 = Bil("Ferrari","benzin",140)

b1.speedup()
b1.speedup()
b1.brake()
b2.brake()
b2.speedup()
b2.speedup()
b3.speedup()
b3.speedup()
b3.speedup()
b3.brake()



print(b1.getName(),'',b1.getSpeed(), 'km/h','har kørt', b1.getDistance(),'km')

print(b2.getName(),'',b2.getSpeed(), 'km/h','har kørt', b2.getDistance(),'km')

print(b3.getName(),'',b3.getSpeed(), 'km/h','har kørt',b3.getDistance(),'km')


