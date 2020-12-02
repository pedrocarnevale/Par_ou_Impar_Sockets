from Rede import Rede
from InterfaceGrafica import *
global jogo
run = True
rede = Rede()
jogador = int(rede.get_objeto_socket())
run=True
run_paridade=True
run_numero=False
run_espera=False
paridade=0
n_pontos=10
texto_usuario = ''
try:
    jogo = rede.send("conectar")
except:
    run = False
    print("Nao foi possivel criar o jogo")
while(run):
    clock.tick(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if run_paridade:
                    run_numero=True
                elif run_numero:
                    run_espera=True
            elif event.key == pygame.K_BACKSPACE:
                texto_usuario=texto_usuario[0:-1]
            else:
                if len(texto_usuario)<=10 and event.key != pygame.K_RETURN and run_espera==False:
                    texto_usuario += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            if continuar.clicar(posicao):
                if run_paridade:
                    run_numero=True
                elif run_numero:
                    run_espera=True
    if(run_paridade):
        redesenhar_tela_paridade(jogador + 1,texto_usuario)
    if run_numero or run_espera:
        redesenhar_tela_numero(jogador+1,texto_usuario,paridade,run_espera,n_pontos)
        if run_espera:
            n_pontos+=1
            if n_pontos==40:
                n_pontos=10

    if jogo.ambos_jogaram():
        if (jogo.determina_vencedor() == 1 and jogador == 1) or (jogo.determina_vencedor() == 0 and jogador == 0):
            vitoria=True
        else:
            vitoria=False
        jogo_amigo=jogo.jogada[jogador][1]
        jogo_adversario=jogo.jogada[not jogador][1]
        redesenhar_tela_resultado(vitoria,jogo_amigo,jogo_adversario)
        run_paridade = True
        run_numero = False
        run_espera = False
        n_pontos = 10
        texto_usuario = ''
        try:
            jogo = rede.send("zerar")
        except:
            run = False
            print("Nao foi possivel achar o jogo apos ambos jogarem")
            break
    if (jogo.p1jogou==0 and jogador==0) or (jogo.p2jogou==0 and jogador==1):
        if(run_paridade==True and run_numero==True):
            paridade = texto_usuario
            paridade=paridade.upper()
            paridade=paridade.replace(" ","")
            if paridade=="PAR":
                paridade=0
            if paridade=="IMPAR":
                paridade=1
            texto_usuario=''
            run_paridade=False
        if(run_numero==True and run_espera==True):
            valor = texto_usuario
            dado=[paridade,valor]
            if jogador == 0:
                if not jogo.p1jogou:
                    jogo = rede.send(dado)
            if jogador == 1:
                if not jogo.p2jogou:
                    jogo = rede.send(dado)
            run_numero=False
    jogo=rede.send("atualizar")