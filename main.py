import sys
import pygame
import math
from pygame import QUIT

# Cores
AZUL = (0, 56, 168)
BRANCO = (255, 255, 255)
VERMELHO = (206, 17, 38)

# Inicialização do Pygame
pygame.init()
largura, altura = 400, 300
DISPLAYSURF = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Bandeira de Cuba')

# Desenhar a bandeira de Cuba
faixa_altura = altura // 5

# Desenhar as faixas
faixa_posicoes = [(0, 0), (0, faixa_altura), (0, 2 * faixa_altura),
                  (0, 3 * faixa_altura), (0, 4 * faixa_altura)]
faixa_cores = [AZUL, BRANCO, AZUL, BRANCO, AZUL]

for posicao, cor in zip(faixa_posicoes, faixa_cores):
  pygame.draw.rect(DISPLAYSURF, cor,
                   (posicao[0], posicao[1], largura, faixa_altura))

# Desenhar o triângulo vermelho
pontos = [(0, 0), (0, altura), (largura // 2, altura // 2)]
pygame.draw.polygon(DISPLAYSURF, VERMELHO, pontos)

# Desenhar a estrela branca
x_estrela = largura // 6
y_estrela = altura // 2
raio_estrela = 50

angulo_rotacao = math.radians(-18)

# Pontos da estrela
pontos_estrela = []
for i in range(5):
  angulo = math.radians(
      i * 144) + angulo_rotacao  # Adiciona o ângulo de rotação
  x = x_estrela + raio_estrela * math.cos(angulo)
  y = y_estrela + raio_estrela * math.sin(angulo)
  pontos_estrela.append((x, y))

pontos_pentagono = []
for i in range(5):
  angulo = math.radians(
      i * 72) + angulo_rotacao  # 360 graus divididos por 5 pontos
  x = x_estrela + raio_estrela * 0.5 * math.cos(
      angulo)  # Raio reduzido para o pentágono
  y = y_estrela + raio_estrela * 0.5 * math.sin(angulo)
  pontos_pentagono.append((x, y))

pygame.draw.polygon(DISPLAYSURF, BRANCO, pontos_estrela)
pygame.draw.polygon(DISPLAYSURF, BRANCO, pontos_pentagono)

# Loop do jogo
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
