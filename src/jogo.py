import pygame

from src.audio import Audio

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    AZUL,
    CINZA,
    PRETO,
    BRANCO,
    VERMELHO,
    AMARELO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    processar_movimento, 
    coletar_cristal,     
    interagir_inimigo,
    desenhar_texto
)

from src.sprites import pegar_sprite
from src.dados import salvar_recorde, carregar_recorde

def executar_jogo():
    pygame.init()
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    chao = pygame.image.load("assets/imagens/chao.png").convert()
    chao = pygame.transform.scale(chao, (LARGURA_TELA, ALTURA_TELA))

    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    audio = Audio()
    audio.tocar_musica_fundo()    

    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)
    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }

    cristal = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(500, 300))
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(200, 500))
    }

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    estado = "MENU" 

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    audio.tocar_clique_menu()
                    rodando = False
                
                if estado == "MENU":
                    if evento.key == pygame.K_SPACE:
                        estado = "JOGANDO"
                
                elif estado == "GAMEOVER" or estado == "VITORIA":
                    if evento.key == pygame.K_r:
                        estado = "JOGANDO"
                        pontos = 0
                        vidas = 3
                        jogador["rect"].topleft = (100, 100)
                        cristal["rect"].topleft = (500, 300)
                        inimigo["rect"].topleft = (200, 500)

        if estado == "MENU":
            tela.fill(PRETO)
            desenhar_texto(tela, "LABIRINTO DO TEMPO", 60, BRANCO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 50)
            desenhar_texto(tela, "Pressione ESPAÇO para Iniciar", 30, AMARELO, LARGURA_TELA // 2, ALTURA_TELA // 2 + 50)

        elif estado == "JOGANDO":
            teclas = pygame.key.get_pressed()

            processar_movimento(teclas, jogador, velocidade, LARGURA_TELA, ALTURA_TELA)

            pontos_antes = pontos
            pontos = coletar_cristal(jogador, cristal, pontos, LARGURA_TELA, ALTURA_TELA)
            if pontos > pontos_antes:
                audio.tocar_cristal()

            vidas_antes = vidas
            vidas = interagir_inimigo(jogador, inimigo, vidas, LARGURA_TELA, ALTURA_TELA)
            if vidas < vidas_antes:
                audio.tocar_dano()

            if jogador_perdeu(vidas):
                estado = "GAMEOVER"

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)

            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
            )

            tela.blit(chao, (0, 0))

            tela.blit(cristal["imagem"], cristal["rect"])
            tela.blit(inimigo["imagem"], inimigo["rect"])
            tela.blit(jogador["imagem"], jogador["rect"])
            
            desenhar_texto(tela, f"Pontos: {pontos}  |  Vidas: {vidas}", 24, PRETO, 120, 20)

        elif estado == "GAMEOVER":
            tela.fill(PRETO)
            desenhar_texto(tela, "FIM DE JOGO", 70, VERMELHO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 60)
            desenhar_texto(tela, f"Sua pontuação: {pontos}", 40, BRANCO, LARGURA_TELA // 2, ALTURA_TELA // 2)
            desenhar_texto(tela, "Pressione 'R' para recomeçar ou 'ESC' para sair", 25, AMARELO, LARGURA_TELA // 2, ALTURA_TELA // 2 + 80)

        elif estado == "VITORIA":
            tela.fill(PRETO)
            desenhar_texto(tela, "VOCÊ ESCAPOU!", 70, AMARELO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 60)
            desenhar_texto(tela, f"Pontuação Final: {pontos}", 40, BRANCO, LARGURA_TELA // 2, ALTURA_TELA // 2)
            desenhar_texto(tela, "Pressione 'R' para jogar novamente", 25, BRANCO, LARGURA_TELA // 2, ALTURA_TELA // 2 + 80)

        pygame.display.flip()

    pygame.quit()