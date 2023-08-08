import turtle


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        # 创建一个turtle对象
        self.t = turtle.Turtle()
        self.t.shape('turtle')

        # 角度增量设置为5度
        self.step = 5
        self.drawingComplete = False

        self.setParams(xc, yc, col, R, r, l)

        self.restart()

    def setParams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
