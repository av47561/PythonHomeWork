from math import sqrt

class trapezia():
    def __init__(self, Ax1, Ay1, Bx2, By2, Cx3, Cy3, Dx4, Dy4):
        self.Ax1 = Ax1
        self.Ay1 = Ay1
        self.Bx2 = Bx2
        self.By2 = By2
        self.Cx3 = Cx3
        self.Cy3 = Cy3
        self.Dx4 = Dx4
        self.Dy4 = Dy4
        self.AB = sqrt(((Bx2-Ax1) ** 2) + ((By2-Ay1) ** 2))
        self.BC = sqrt(((Cx3-Bx2) ** 2) + ((Cy3-By2) ** 2))
        self.CD = sqrt(((Dx4-Cx3) ** 2) + ((Dy4-Cy3) ** 2))
        self.AD = sqrt(((Dx4-Ax1) ** 2) + ((Dy4-Ay1) ** 2))
 
    def Check(self):
        if (self.AB) == (self.CD):
            self.Check = 'Трапеция равнобокая'
            return self.Check
        else:
            self.Check = 'Трапеция неравнобокая'
            return self.Check
        
    def Ptrapezia(self):
        self.Ptrapezia = (self.AB+self.BC+self.CD+self.AD)
        return (self.Ptrapezia)
    
    def Strapezia(self):
        self.Strapezia = ((self.AB+self.BC)/2)*(sqrt((self.CD**2)-((((self.BC-self.AB)**2)+(self.CD**2)-(self.AD**2))/(2*(self.BC-self.AB)))))
        return (self.Strapezia)

Figure = trapezia(2,2,7,4,10,8,5,6)

print('Длинна строны АВ = {}, ВС = {}, CD = {}, AD = {}'.format(Figure.AB, Figure.BC, Figure.CD, Figure.AD))
print('Периметр трапеции АВСD равен {}'.format(Figure.Ptrapezia()))
print('Площадь трапеции АВСD равна {}'.format(Figure.Strapezia()))
print(Figure.Check)
