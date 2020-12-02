import socket
import pickle
class Rede:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (socket.gethostname(), 5555)
        self.objeto_socket = self.connect()

    def get_objeto_socket(self):
        return self.objeto_socket

    def connect(self):
        try:
            self.cliente.connect(self.address)
            return pickle.loads(self.cliente.recv(4096))
        except:
            pass

    def send(self, data):
        try:
            self.cliente.send(pickle.dumps(data))
            return pickle.loads(self.cliente.recv(4096))
        except socket.error as ERRO:
            print(ERRO)