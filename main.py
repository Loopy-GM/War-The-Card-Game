import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Card Game: War")

clock = pygame.time.Clock()
doExit = False

class card:
  def __init__(self, suit, number):
    self.suit = suit
    self.number = number
  def draw(self, x, y):
    pygame.draw.rect(screen, (255,255,255), (x, y, 100, 80))
    pygame.draw.rect(screen, (0,0,0), (x, y, 100, 80), 3)
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render(str(self.number), 1, (0,0,0))
    text2 = font.render(str(self.suit), 1, (255,0,0))
    screen.blit(text, (x+30, y+30))
    screen.blit(text2, (x+10, y+60))

Deck = list()

for j in range(4):
  for i in range(13):
    Deck.append(card(j,i))

random.shuffle(Deck)

p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list()

for i in range(26):
  p1hand.append(Deck[i])
for j in range(26, 52):
  p2hand.append(Deck[j])

turn = False

while not doExit:
  clock.tick(60)

  event = pygame.event.wait()

  if event.type == pygame.QUIT:
      doExit = True
  if event.type == pygame.MOUSEBUTTONDOWN:
      turn = True
  if event.type == pygame.MOUSEBUTTONUP:
      turn = False
  if event.type == pygame.MOUSEMOTION:
      mousePos = event.pos

  screen.fill((0,150,0))#_________________________________

  for i in range(52):
    Deck[i].draw(20+i*5,20+i*3)

  pygame.display.flip()

pygame.quit()
