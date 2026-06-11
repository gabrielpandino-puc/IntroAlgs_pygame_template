import pygame
from src.funcoes import verificar_colisao

def test_verificar_colisao_com_sucesso():
    """Testa se a função de colisão detecta quando dois retângulos se sobrepõem."""
    # Cria dois retângulos na mesma posição
    rect1 = pygame.Rect(100, 100, 50, 50)
    rect2 = pygame.Rect(100, 100, 50, 50)
    
    # O teste espera que a função retorne True
    assert verificar_colisao(rect1, rect2) == True

def test_verificar_colisao_sem_sucesso():
    """Testa se a função de colisão funciona quando os retângulos estão distantes."""
    rect1 = pygame.Rect(10, 10, 50, 50)
    rect2 = pygame.Rect(500, 500, 50, 50)
    
    # O teste espera que a função retorne False
    assert verificar_colisao(rect1, rect2) == False