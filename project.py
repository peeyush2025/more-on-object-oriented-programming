import math
class Circle:
    def __init__(self,r): self.r=r
    def area(self): return math.pi*self.r**2
    def peri(self): return 2*math.pi*self.r

r=float(input("Radius: "))
c=Circle(r)
print("Area:",c.area(),"Perimeter:",c.peri())
