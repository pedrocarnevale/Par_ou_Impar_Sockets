import socket
from _thread import *
import pickle
from jogo import jogo

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((socket.gethostname(), 5555))
except socket.error as ERRO:
    str(ERRO)
s.listen()
print("Esperando por conexoes")
conta_id = 0
jogadores=[]

def cliente_thread(conn, jogador, partida):
    global conta_id
    conn.send(pickle.dumps(jogador))
    resposta = ""
    while True:
        try:
            dados = pickle.loads(conn.recv(4096))
            if not dados:
                print("Desconectado")
                break
            else:
                if dados == "zerar":
                    partida.zerar()
                    if jogador==0:
                        print("Criando novo jogo")
                elif dados != "conectar" and dados!="atualizar":
                    partida.joga(jogador, int(dados[0]), int(dados[1]))
                resposta = partida
                conn.sendall(pickle.dumps(resposta))
                if dados != "conectar" and dados != "atualizar" and dados!="zerar":
                    print(resposta)
        except:
            break
    print("Conexao perdida com o jogador",jogador+1)
    jogadores.remove(jogador)
    conta_id -= 1
    conn.close()


while True:
    (conn,address,) = (s.accept())
    conta_id += 1
    jogador = 0
    if conta_id == 1:
        jogadores.append(jogador)
        partida = jogo()
        print("Jogador 1 conectado")
        print("Criando novo jogo")
    if conta_id == 2:

        partida.pronto = True
        if jogadores[0]==0:
            jogador = 1
        else:
            jogador==0
        jogadores.append(jogador)
        print("Jogador 2 conectado")
    start_new_thread(cliente_thread, (conn, jogador, partida))