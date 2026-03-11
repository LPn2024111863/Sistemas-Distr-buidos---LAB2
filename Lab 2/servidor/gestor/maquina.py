from servidor.operacoes import dividir, somar, subtrair, multiplicar, raiz_quadrada
from typing import Union
import json
import socket

COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "add_obj  "
SYM_OP = "sym      "
SUB_OP = "sub      "
BYE_OP = "bye      "
END_OP = "stop     "
PORT = 35001
SERVER_ADDRESS = "192.168.56.1"

# ---------------------- interaction with sockets ------------------------------
def receive_int(connection, n_bytes: int) -> int:
    """
    :param n_bytes: The number of bytes to read from the current connection
    :return: The next integer read from the current connection
    """
    data = connection.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)

def send_int(connection, value: int, n_bytes: int) -> None:
    """
    :param value: The integer value to be sent to the current connection
    :param n_bytes: The number of bytes to send
    """
    connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

def receive_str(connection, n_bytes: int) -> str:
    """
    :param n_bytes: The number of bytes to read from the current connection
    :return: The next string read from the current connection
    """
    data = connection.recv(n_bytes)
    return data.decode()

def send_str(connection, value: str) -> None:
    """
    :param value: The string value to send to the current connection
    """
    connection.connection.send(value.encode())

    # TODO
    # Implement a method that sends and object and returns an object.
    # ...

def send_object(connection, obj):
    """1º: envia tamanho, 2º: envia dados."""
    data = json.dumps(obj).encode('utf-8')
    size = len(data)
    send_int(connection, size, INT_SIZE)  # Envio do tamanho
    connection.send(data)  # Envio do objeto

def receive_object(connection):
    """1º: lê tamanho, 2º: lê dados."""
    size = receive_int(connection, INT_SIZE)  # Recebe o tamanho
    data = connection.recv(size)  # Recebe o objeto
    return json.loads(data.decode('utf-8'))

class Maquina:
    def __init__(self):
        self.COMMAND_SIZE = 9
        self.INT_SIZE = 8
        self.ADD_OP = "add      "
        self.OBJ_OP = "add_obj  "
        self.SYM_OP = "sym      "
        self.SUB_OP = "sub      "
        self.BYE_OP = "bye      "
        self.END_OP = "stop     "
        self.PORT = 35001
        self.SERVER_ADDRESS = "10.1.58.252"

    def execute(self)-> Union[float,str, None]:
        """

        :param operador: String que representa a operação que será efetuada .
        :param x: Float que representa o primeiro valor da operação, a menos que
        seja a raíz quadrada, sendo neste caso o valor utilizado por esta.
        :param y: Float que representa o segundo valor da operação.

        :return: Este metodo retorna o resultado da operação, sendo este um float
        em caso da operação ser sucedida, str se houver um erro na divisão ou
        raíz quadrada, ou None caso o operador seja inválido.
        """
        s = socket.socket()
        s.bind(('', self.PORT))
        s.listen(1)
        print("Waiting for clients to connect on port " + str(self.PORT))
        keep_running = True
        while keep_running:
            print("On accept...")
            connection, address = s.accept()
            print("Client " + str(address) + " just connected")
            last_request = False
            # Recebe mensagens...
            while not last_request:
                request_type = receive_str(connection, self.COMMAND_SIZE)
                match request_type:
                    case self.ADD_OP:
                        a = receive_int(connection, self.INT_SIZE)
                        b = receive_int(connection, self.INT_SIZE)
                        print("Pediram para somar:", a, "+", b)
                        som: object = somar.Somar(a,b)
                        result = som.executar()
                        send_int(connection, result, self.INT_SIZE)

                    case "-":
                        sub: object = subtrair.Subtrair(a, b)
                        resultado = sub.executar()

                    case "/":
                        div: object = dividir.Dividir(a, b)
                        resultado = div.executar()

                    case "*":
                        s: object = multiplicar.Multiplicar(a, b)
                        resultado = s.executar()

                    case "sqrt":
                        s: object = raiz_quadrada.RaizQuadrada(a)
                        resultado = s.executar()

                    case self.BYE_OP:
                        print("Last request...")
                        last_request = True
                        # keep_running = False

                    case self.END_OP:
                        last_request = True
                        keep_running = False

                    case _:
                        print("Operação inválida")
                        return None

        print("Stopping...")
        s.close()
        print("Server stopped")

#    def main():
#        """
#        Runs the server server until the client sends a "terminate" action
#        """
#
#            match request_ty
#                if request_type == ADD_OP:
#
#
#                elif request_type == SUB_OP:
#                    a = receive_int(connection, INT_SIZE)
#                    b = receive_int(connection, INT_SIZE)
#                    print("Pediram para subtrair:", a, "-", b)
#                    result = a - b
#                    send_int(connection, result, INT_SIZE)
#                elif request_type == OBJ_OP:
#                    # A new type of operation. The server receives a dictionary.
#                    objeto = receive_object(connection)
#                    if objeto["oper"] == "+":
#                        print("Pediram para somar:", objeto["oper1"], "+", objeto["oper2"])
#                        result = objeto["oper1"] + objeto["oper2"]
#                        send_int(connection, result, INT_SIZE)
#                # It returns an integer.
#
#
#
#    if __name__ == "__main__":
#        main()
