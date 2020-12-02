import pygame
import sys
pygame.init()
pygame.font.init()
comprimento=550
altura=300
tela=pygame.display.set_mode((comprimento,altura))
pygame.display.set_caption("Par ou Impar")
fonte_grande = pygame.font.SysFont("comicsansms", 40)
fonte_pequena = pygame.font.SysFont("comicsansms", 20)
fonte_media = pygame.font.SysFont("comicsansms", 30)
vencedor=pygame.transform.scale(pygame.image.load("./vencedor.png"),(102,128))
perdedor=pygame.transform.scale(pygame.image.load("./perdedor.png"),(108,108))
retangulo =pygame.Rect(120,100,300,32)
clock=pygame.time.Clock()

class Botao():
    def __init__(self, texto, x, y, cor,tamanho,comprimento,altura):
        self.texto = texto
        self.x = x
        self.y = y
        self.cor = cor
        self.comprimento = comprimento
        self.altura = altura
        self.tamanho=tamanho

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.comprimento, self.altura))
        font = pygame.font.SysFont("comicsansms", self.tamanho)
        texto = font.render(self.texto, 1, (255, 255, 255))
        tela.blit(texto, (self.x + round(self.comprimento / 2) - round(texto.get_width() / 2),
                        self.y + round(self.altura / 2) - round(texto.get_height() / 2)))

    def clicar(self, posicao):
        x1 = posicao[0]
        y1 = posicao[1]
        return (self.x <= x1 <= self.x + self.comprimento) and (self.y <= y1 <= self.y + self.altura)

continuar=Botao("continuar",310,140,(16, 148, 45),16,110,20)

def redesenhar_tela_paridade(jogador,texto_usuario):
    tela.fill((75, 152, 235))
    texto_titulo = fonte_grande.render("Escolha par ou impar:", 1, (0,0,0))
    tela.blit(texto_titulo, (55, 40))
    pygame.draw.rect(tela, (255,255,255), retangulo)
    texto_jogador=fonte_pequena.render("Jogador " + str(jogador),1,(0,0,0))
    tela.blit(texto_jogador,(440,260))
    texto = fonte_pequena.render(texto_usuario, 1, (0, 0, 0))
    tela.blit(texto, (retangulo.x + 5, retangulo.y + 5))
    continuar.desenhar(tela)
    pygame.display.update()

def redesenhar_tela_numero(jogador,texto_usuario,paridade,run_espera,n_pontos):
    tela.fill((75, 152, 235))
    if paridade==0:
        texto_paridade="Par"
    else:
        texto_paridade="Impar"
    texto_opcao = fonte_pequena.render(texto_paridade, 1, (0, 0, 0))
    tela.blit(texto_opcao, (120, 140))
    texto_titulo = fonte_grande.render("Escolha seu numero:", 1, (0,0,0))
    tela.blit(texto_titulo, (55, 40))
    pygame.draw.rect(tela, (255,255,255), retangulo)
    texto_jogador=fonte_pequena.render("Jogador " + str(jogador),1,(0,0,0))
    tela.blit(texto_jogador,(440,260))
    texto = fonte_pequena.render(texto_usuario, 1, (0, 0, 0))
    tela.blit(texto, (retangulo.x + 5, retangulo.y + 5))
    if run_espera:
        aguardo = "Aguardando outro jogador"
        for i in range(n_pontos//10):
            aguardo += '.'
        texto_espera = fonte_media.render(aguardo, 1, (0, 0, 0))
        tela.blit(texto_espera, (20, 180))
    continuar.desenhar(tela)
    pygame.display.update()

def redesenhar_tela_resultado(vitoria,jogo_amigo,jogo_adversario):
    tela.fill((75, 152, 235))
    if vitoria:
        texto_titulo = fonte_grande.render("Parabéns! Você venceu!", 1, (0,0,0))
        tela.blit(texto_titulo, (55, 40))
        tela.blit(vencedor,(400,120))
    else:
        texto_titulo = fonte_grande.render("Você perdeu", 1, (0, 0, 0))
        tela.blit(texto_titulo, (55, 40))
        tela.blit(perdedor, (400, 120))
    jogada_amiga="Você jogou " + str(jogo_amigo)
    jogada_adversaria="Seu oponente jogou " + str(jogo_adversario)
    texto_jogada_amiga = fonte_media.render(jogada_amiga, 1, (0,0,0))
    tela.blit(texto_jogada_amiga, (55, 110))
    texto_jogada_adversaria = fonte_media.render(jogada_adversaria, 1, (0, 0, 0))
    tela.blit(texto_jogada_adversaria, (55, 150))
    pygame.display.update()
    pygame.time.delay(5000)