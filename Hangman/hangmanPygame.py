import pygame 
# set up display
pygame.init()
WIDTH,HEIGHT = 800,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")
# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)
# set game variables
hangman_status = 0
# color variables
WHITE = (255,255,255)
# setup game loop
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE) # fill display by a color
    screen.blit(images[hangman_status],(150,100)) # draw image
    pygame.display.flip()
    # Checking for events like keyboard interrupts, mouse clicks etc.
    # Coordinate system in pygame - increase x move right, increase y move down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
        