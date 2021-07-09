# -*- coding: utf-8 -*-
import time
import pygame
import os
import json
import random
import libRec.libLibras as R

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 165, 223)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE_LINE=(2,120,161)
pygame.init()
with open('data.json') as json_file:
	 data=json.load(json_file)
	 random.shuffle(data)
	 objs=data
print(len(objs))

for i in range(0,len(objs)):
	obj=data[i]["objeto"]
	img=data[i]["img"]
	qtd=data[i]["quantidade"]
	texto=""
	l=0
	screen = pygame.display.set_mode((1720, 800))
	# carregando fonte
	font = pygame.font.SysFont(None, 150)

	pygame.display.set_caption('Oque É?')

	# preenchendo o fundo com azul

	while True:
		screen.fill(BLUE)
		# desenhando na superfície
		pygame.draw.line(screen,BLUE_LINE, [3, 600], [1200, 600], 6)
		pygame.draw.line(screen,BLUE_LINE, [1200, 3], [1200, 797], 6)
		pygame.draw.line(screen,BLUE_LINE, [1200, 500], [1717, 500], 6)
		image=pygame.image.load(os.path.join('imgs', img))
		image = pygame.transform.scale(image, (280, 320))
		image=pygame.transform.rotate(image,(90))
		screen.blit(image, (1300, 60))

		# definindo o texto
		espaco=""
		tamanho=len(texto)
		espaco=texto;
		if tamanho==qtd:
			break
		for x in range(0,qtd-tamanho):
			espaco=espaco+"_ "

		text = font.render(espaco, True, WHITE)
		# copiando o texto para a superficie
		screen.blit(text, [80, 200])

		# atualizando a tela
		pygame.display.flip()
		letra=R.reconhece()
		image=pygame.image.load(os.path.join('libRec/temp/',"img.png"))
		image = pygame.transform.scale(image, (150, 150))
		screen.blit(image, (1300, 600))
		print(letra)

		t = font.render(letra, True, WHITE)
		screen.blit(t, [1500, 600])
		if letra== obj[l]:
			l+=1
			texto+=letra

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				break
			if event.type == pygame.KEYDOWN:
				if event.unicode==obj[l]:
					l+=1
					texto+=event.unicode
				print(event.unicode)
		pygame.display.update()
		time.sleep(1)
pygame.quit()
