from math import sqrt

class Triangle:
    def __init__(self, Ax1, Ay1, Bx2, By2, Cx3, Cy3):
        self.Ax1 = Ax1
        self.Ay1 = Ay1
        self.Bx2 = Bx2
        self.By2 = By2
        self.Cx3 = Cx3
        self.Cy3 = Cy3
        self.AB = sqrt((Bx2-Ax1)**2+(By2-Ay1)**2)
        self.BC = sqrt((Cx3-Bx2)**2+(Cy3-By2)**2)
        self.AC = sqrt((Ax1-Cx3)**2+(Ay1-Cy3)**2)

    def PTriangle(self):
        self.PTriangle = (self.AB+self.AC+self.BC)
        return (self.PTriangle)
    
    def STriangle(self):
        self.STriangle = sqrt(self.PTriangle*(self.PTriangle-self.AB)*(self.PTriangle-self.BC)*(self.PTriangle-self.AC))
        return (self.STriangle)
    
    def h1Triangle(self):
        self.h1Triangle = 2*(self.STriangle/self.AB)
        return (self.h1Triangle)

    def h2Triangle(self):
        self.h2Triangle = 2*(self.STriangle/self.BC)
        return (self.h2Triangle)

    def h3Triangle(self):
        self.h3Triangle = 2*(self.STriangle/self.AC)
        return (self.h3Triangle)
    
Figure = Triangle(2, 2, 5, 5, 8, 2)

print('Длинна строны АВ = {}, ВС = {}, AC = {}'.format(Figure.AB, Figure.BC, Figure.AC))
print('Периметр треугольника АВС равен {}'.format(Figure.PTriangle()))
print('Площадь треугольника АВС равна {}'.format(Figure.STriangle()))
print('Высота треугольника АВС, проведенная из угла C равна {}'.format(Figure.h1Triangle()))
print('Высота треугольника АВС, проведенная из угла A равна {}'.format(Figure.h2Triangle()))
print('Высота треугольника АВС, проведенная из угла B равна {}'.format(Figure.h3Triangle()))
