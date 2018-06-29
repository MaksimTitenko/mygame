import pygame

pygame.init()
win = pygame.display.set_mode((1000, 640))

pygame.display.set_caption("sounds/Cubes Game")
music = pygame.mixer.Sound('sounds/Music.ogg')
music_channel = music.play(loops=-1)
music_channel.set_volume(0.5)

walkRight = [pygame.image.load('images/pygame_trump_run_right_1.png'),
             pygame.image.load('images/pygame_trump_run_right_2.png'),
             pygame.image.load('images/pygame_trump_run_right_3.png'),
             pygame.image.load('images/pygame_trump_run_right_4.png'),
             pygame.image.load('images/pygame_trump_run_right_5.png'),
             pygame.image.load('images/pygame_trump_run_right_6.png')]

walkLeft = [pygame.image.load('images/pygame_trump_run_left_1.png'),
            pygame.image.load('images/pygame_trump_run_left_2.png'),
            pygame.image.load('images/pygame_trump_run_left_3.png'),
            pygame.image.load('images/pygame_trump_run_left_4.png'),
            pygame.image.load('images/pygame_trump_run_left_5.png'),
            pygame.image.load('images/pygame_trump_run_left_6.png')]

playerStand = pygame.image.load('images/pygame_idle.png')
bg = pygame.image.load('images/bg.png')

clock = pygame.time.Clock()

x = 25
y = 230
width = 256
height = 256
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = 'right'


class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           self.radius)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 60:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 10], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 10], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


run = True
bullets = []

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 1000 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:

        if lastMove == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y +
                                                                height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 1000 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()
pygame.quit()
