from typing import Union

class Interacao:
    def __init__(self, maquina:object):
        self.maquina:object = maquina

    def execute(self):
        """
        Este metodo pergunta ao utilizador qual será o operador utilizado e
        os valores que serão utilizados nessa operação.

        O metodo no final faz "print" do valor ou erro associados à efetuação
        da operação
        """
        print("Qual é o cálculo que quer efetuar? x + - / sqrt")
        res:str = input()
        x:float = float(input("x= "))
        y:float = float(input("y= "))

        resultado: Union[float, str] = self.maquina.operar(res, x, y)
        if resultado is not None:
            print("O resultado da operação é: " + str(resultado))