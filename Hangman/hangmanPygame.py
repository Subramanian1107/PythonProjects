import pygame 
import random
import math
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
with open("wordList.txt", 'r') as f:
    words = f.readlines()
word = random.choice(words)[:-1]
word = word.upper()
guesses = []
# color variables
WHITE = (255,255,255)
BLACK = (0,0,0)
# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(2*RADIUS+GAP)*12)/2)   #
starty = 400
for i in range(26):
    x = startx + (RADIUS*2+GAP)*(i%13)
    y = starty + ((i//13)*(GAP+RADIUS*2))
    letters.append([x,y,chr(65+i),True])

# font
LETTER_FONT = pygame.font.SysFont('Arial',30)
WORD_FONT = pygame.font.SysFont('Arial',60)
def draw():
    screen.fill(WHITE) # fill display by a color
    screen.blit(images[hangman_status],(150,100)) # draw image
    display_word = ""
    for letter in word:
        if letter not in guesses:
            display_word+= "_ "
        else:
            display_word+= letter+" "
    text = WORD_FONT.render(display_word,1,BLACK)
    screen.blit(text,(400,200))
    # draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
            pygame.draw.circle(screen,BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(ltr,1,BLACK)
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    pygame.display.flip()
# setup game loop
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    draw()
    # Checking for events like keyboard interrupts, mouse clicks etc.
    # Coordinate system in pygame - increase x move right, increase y move down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible = letter
                if visible:
                    distance = math.sqrt((x-mx)**2 + (y-my)**2)
                    if distance < RADIUS:
                        letter[3] = False
                        guesses.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    done = True
    for letter in word:
        if letter not in guesses:
            done = False
    
    if(done == True):
        print("Win")
        text = WORD_FONT.render("You Won!",1,BLACK)
        screen.blit(text,((WIDTH-text.get_width())/2,(HEIGHT-text.get_height())/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break
    if(hangman_status == 6):
        print("Loss")
        break
    
pygame.quit()
        