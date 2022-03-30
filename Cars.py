class Bil:
  def __init__(self, mærke, drivmiddel, hastighed,):
    self.mærke = mærke
    self.drivmiddel = drivmiddel
    self.hastighed = hastighed

  def setdrivmiddel(self, drivmiddel):
    self.drivmiddel = drivmiddel
  def speedup(self, ):
    self.hastighed += 1
  def brake(self, ):
    self.hastighed -= 1

b1 = Bil("BMW","El",90)
b2 = Bil("Toyota","benzin",80)
b3 = Bil("Ferrari","benzin",120)

b1.speedup()
b1.speedup()
b1.speedup()
print(b1.hastighed)




