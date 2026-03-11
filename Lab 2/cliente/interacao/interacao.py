import json
import socket
# import json
# PORT e SERVER ADDRES
COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "add_obj  "
SYM_OP = "sym      "
BYE_OP = "bye      "
SUB_OP = "sub      "
END_OP = "stop     "
PORT = 35000
SERVER_ADDRESS = "31.22.145.201"

# ----- enviar e receber strings ----- #
def receive_str(connect, n_bytes: int) -> str:
    """
    :param n_bytes: The number of bytes to read from the current connection
    :return: The next string read from the current connection
    """
    data = connect.recv(n_bytes)
    return data.decode()

def send_str(connect, value: str) -> None:
    connect.send(value.encode())

def send_int(connect: socket.socket, value: int, n_bytes: int) -> None:
    connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

def receive_int(connect: socket.socket, n_bytes: int) -> int:
    data = connect.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)

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

class Interacao:
    def __init__(self):
        self.COMMAND_SIZE = 9
        self.INT_SIZE = 8
        self.ADD_OP = "add      "
        self.OBJ_OP = "add_obj  "
        self.SYM_OP = "sym      "
        self.SUB_OP = "sub      "
        self.BYE_OP = "bye      "
        self.END_OP = "stop     "
        self.res = 0
        self.PORT = 35001
        self.SERVER_ADDRESS = "10.1.58.252"

    def execute(self):
        # Socket & ligação
        connection = socket.socket()
        connection.connect((self.SERVER_ADDRESS, self.PORT))
        # Testar a operação de soma
        a = 10
        b = 15
        send_str(connection, self.ADD_OP)
        send_int(connection, a, self.INT_SIZE)
        send_int(connection, b, self.INT_SIZE)
        self.res = receive_int(connection, self.INT_SIZE)
        print("O resultado da soma é:", self.res)

        send_str(connection, self.END_OP)
        print("Client terminating connection and server activity")
        connection.close()

#        def main():
#            # Socket & ligação
#            connection = socket.socket()
#            connection.connect((SERVER_ADDRESS, PORT))
#            # Testar a operação de soma
#            a = 10
#            b = 15
#            send_str(connection, self.ADD_OP)
#            send_int(connection, a, self.INT_SIZE)
#            send_int(connection, b, self.INT_SIZE)
#            self.res = receive_int(connection, self.INT_SIZE)
#            print("O resultado da soma é:", self.res)
#            # Execute a new type of operation: OBJ_OP
#            # Client sends a dictionary.
#            objeto = {"oper": "+", "oper1": 4, "oper2": 5}
#            send_str(connection, self.OBJ_OP)
#            send_object(connection, objeto)
#            # It receives an integer a result of the operation
#            res = receive_int(connection, INT_SIZE)
#            print("O resultado da operação do objeto é:", res)
#
#            # ...
#            # Testar duas operações de subtração
#            for i in range(2):
#                a += 1
#                # Operação de subtração
#                send_str(connection, SUB_OP)
#                send_int(connection, a, INT_SIZE)
#                send_int(connection, b, INT_SIZE)
#                res = receive_int(connection, INT_SIZE)
#                print("O resultado da subtração é:", res)
#            # 1 Fechar a conexão apenas do lado do cliente ou...
#            # send_str(connection,BYE_OP)
#            # print("Connection is going to close...")
#            # connection.close()
#            # 2 Fechar a conexão do lado do cliente e do servidor
#            send_str(connection, END_OP)
#            print("Client terminating connection and server activity")
#            connection.close()
#
#        if __name__ == "__main__":
#            main()
