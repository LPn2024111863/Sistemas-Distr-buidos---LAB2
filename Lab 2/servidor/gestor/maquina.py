from servidor.operacoes import dividir, somar, subtrair, multiplicar, raiz_quadrada
from typing import Union

class Maquina:
    def __init__(self):
        pass

    def operar(self, operador:str, x:float,y:float )-> Union[float,str, None]:
        """

        :param operador: String que representa a operação que será efetuada .
        :param x: Float que representa o primeiro valor da operação, a menos que
        seja a raíz quadrada, sendo neste caso o valor utilizado por esta.
        :param y: Float que representa o segundo valor da operação.

        :return: Este metodo retorna o resultado da operação, sendo este um float
        em caso da operação ser sucedida, str se houver um erro na divisão ou
        raíz quadrada, ou None caso o operador seja inválido.
        """
        match operador:
            case "+":
                som: object = somar.Somar(x, y)
                resultado = som.executar()

            case "-":
                sub: object = subtrair.Subtrair(x, y)
                resultado = sub.executar()

            case "/":
                div: object = dividir.Dividir(x, y)
                resultado = div.executar()

            case "*":
                s: object = multiplicar.Multiplicar(x, y)
                resultado = s.executar()

            case "sqrt":
                s: object = raiz_quadrada.RaizQuadrada(x)
                resultado = s.executar()
            case _:
                print("Operação inválida")
                return None

        return resultado