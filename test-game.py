import pygame
import sys

pygame.init()

def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):
  newSurf = pygame.Surface((newWidth, newHeight), pygame.SRCALPHA, 32)
  newSurf.blit(image, (0,0), (cropWidth, cropHeight, newWidth, newHeight))

  return newSurf

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("My First Game")

grassImage = pygame.image.load("grass-1.png").convert()
grassImage = pygame.transform.scale(grassImage, screenDim)

screen.blit(grassImage, (0,0))

rescale = 3
player = pygame.image.load("./PNG/Green/characterGreen-1.png").convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(player, (playerWidth*rescale, playerHeight*rescale))
player = pygame.transform.rotate(player, 90)

foot = pygame.image.load("./PNG/Green/characterGreen-foot-1.png").convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(foot, (footWidth*rescale, footHeight*rescale))
foot = pygame.transform.rotate(foot, 90)

rescaleBall = 2
ball = pygame.image.load("./PNG/Equipment/ball_soccer2.png").convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(ball, (ballWidth*rescaleBall, ballHeight*rescaleBall))

goalLeft = pygame.image.load("./PNG/Elements/element-32.png").convert_alpha()
goalLeft = pygame.transform.scale(goalLeft, (270,270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
adjust = 12
goalLeft = cropSurface(goalLeftWidth/2+adjust,
  goalLeftHeight/2+adjust,
  goalLeftWidth/2-adjust,
  goalLeftHeight/2-adjust,
  goalLeft)

goalMiddle = pygame.image.load("./PNG/Elements/element-33.png").convert_alpha()
goalMiddle = pygame.transform.scale(goalMiddle, (270,270))
goalMiddleWidth = goalMiddle.get_rect().width
goalMiddleHeight = goalMiddle.get_rect().height
adjust = 12
goalMiddle = cropSurface(goalMiddleWidth,
  goalMiddleHeight/2+adjust,
  0,
  goalMiddleHeight/2-adjust,
  goalMiddle)

goalRight = pygame.image.load("./PNG/Elements/element-36.png").convert_alpha()
goalRight = pygame.transform.scale(goalRight, (270,270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height
goalRight = cropSurface(goalRightWidth/2+adjust,
  goalRightHeight/2+adjust,
  0,
  goalRightWidth/2-adjust,
  goalRight)

goalStart = (width-goalLeft.get_rect().width-
  goalMiddle.get_rect().width-
  goalRight.get_rect().width)/2

screen.blit(goalLeft, (goalStart,0))
screen.blit(goalMiddle, (goalStart+
  goalLeft.get_rect().width,
  0))
screen.blit(goalRight, (goalStart+
  goalLeft.get_rect().width+
  goalMiddle.get_rect().width
  ,0))

playerX = width/2
playerY = 530
screen.blit(player, (playerX-player.get_rect().width/2,
  playerY-player.get_rect().height/2))

ballX = width/2
ballY = 450
screen.blit(ball, (ballX-ball.get_rect().width/2,
  ballY-ball.get_rect().height/2))
  
# screen.blit(foot, (0,0))


finished = False
while finished == False:
  for event in pygame.event.get():
    # handle events

    #quit the game when x pressed on window
    if event.type == pygame.QUIT:
      finished = True
      pygame.quit()
      sys.exit()

  pygame.display.flip() #loading next frame

# pygame.quit()
