class Somar:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self):
        self.res = self.x + self.y
        return self.res