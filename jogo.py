class jogo:
    def __init__(self):
        self.p1jogou = False
        self.p2jogou = False
        self.pronto = False
        self.jogada = [
            [None, None],
            [None, None],
        ]  # posicao 0 par ou impar, posicao 1 jogada
        ## par=0, impar =1
        self.vencedor = [0, 0]

    def __repr__(self):
        if (not self.p1jogou) and (not self.p2jogou):
            return "Jogadores 1 e 2 ainda nao jogaram"
        if self.p1jogou and not self.p2jogou:
            return "Jogador 1 jogou " + str(self.jogada[0][1]) + " e Jogador 2 nao jogou"
        if not self.p1jogou and self.p2jogou:
            return "Jogador 1 nao jogou e Jogador 2 jogou " + str(self.jogada[1][1])
        if self.ambos_jogaram():
            return "Jogador 1 jogou " + str(self.jogada[0][1]) + " e Jogador 2 jogou " + str(self.jogada[1][1])
        else:
            return self

    def get_jogada(self, jogador):
        return self.jogada[jogador]

    def joga(self, jogador, paridade, movimento):
        self.jogada[jogador][0] = paridade
        self.jogada[jogador][1] = movimento

        if jogador == 0:
            self.p1jogou = True
        else:
            self.p2jogou = True

    def conectados(self):
        return self.pronto

    def ambos_jogaram(self):
        return self.p1jogou and self.p2jogou

    def determina_vencedor(self):
        paridade1 = self.jogada[0][0]
        p1 = self.jogada[0][1]
        p2 = self.jogada[1][1]
        resultado = p1 + p2
        if (resultado % 2) == paridade1:
            self.vencedor[0] = 1
            vence = 0
        else:
            self.vencedor[1] = 1
            vence = 1
        return vence

    def zerar(self):
        self.p1jogou = False
        self.p2jogou = False