import math

class RaizQuadrada:
    def __init__(self, x:float):
        self.x = x
        self.res = 0

    def executar(self):
        try:
            self.res = math.sqrt(self.x)
        except ValueError:
            return "ERRO: Raíz quadrada não aceita números negativos"

        return self.res