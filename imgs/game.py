from pygame import *
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
Size = (SCREEN_WIDTH, SCREEN_HEIGHT)

window = display.set_mode(Size)
display.set_caption('Catch Me If You Can')
clock = time.Clock()  

background = transform.scale(image.load('imgs/Background.png'), Size)

GuySize = (80, 50)
CarSize = (100, 80)

Guy = transform.scale(image.load('imgs/guy.png'), GuySize)
car2 = transform.scale(image.load('imgs/car.png1.png'), CarSize)
car3 = transform.scale(image.load('imgs/car.png3.png'), CarSize)
car4 = transform.scale(image.load('imgs/car.png4.png'), CarSize)
car5 = transform.scale(image.load('imgs/car.png.png'), CarSize)

GuyPosx = 45
GuyPosy = 670
GuySpeed = 3

Car2Posx = SCREEN_WIDTH - CarSize[0]
Car2Posy = 230
Car2Speed = -5

Car3Posx = 0
Car3Posy = 730
Car3Speed = 6

Car4Posx = SCREEN_WIDTH - CarSize[0]
Car4Posy = 470
Car4Speed = -7

Car5Posx = 672
Car5Posy = 0
Car5Speed = 5

game = True
angle = 0

while game:
    clock.tick(200)  
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()

    dx, dy = 0, 0  
    if keys[K_LEFT]:
        dx -= GuySpeed
        angle = 180
    if keys[K_RIGHT]:
        dx += GuySpeed
        angle = 0
    if keys[K_UP]:
        dy -= GuySpeed
        angle = 90
    if keys[K_DOWN]:
        dy += GuySpeed
        angle = -90

    if keys[K_LEFT] and keys[K_DOWN]:
        angle = -135
    if keys[K_LEFT] and keys[K_UP]:
        angle = 135
    if keys[K_RIGHT] and keys[K_DOWN]:
        angle = -45
    if keys[K_RIGHT] and keys[K_UP]:
        angle = 45

    
    if dx != 0 and dy != 0:
        factor = GuySpeed / math.sqrt(dx**2 + dy**2)
        dx = int(dx * factor)
        dy = int(dy * factor)

    new_x = max(0, min(SCREEN_WIDTH - GuySize[0], GuyPosx + dx))
    new_y = max(0, min(SCREEN_HEIGHT - GuySize[1], GuyPosy + dy))

    
    guy_rect = Rect(new_x, new_y, GuySize[0], GuySize[1])
    collision = False
    for car_rect in [
        Rect(Car2Posx, Car2Posy, CarSize[0], CarSize[1]),
        Rect(Car3Posx, Car3Posy, CarSize[0], CarSize[1]),
        Rect(Car4Posx, Car4Posy, CarSize[0], CarSize[1]),
        Rect(Car5Posx, Car5Posy, CarSize[0], CarSize[1]),
    ]:
        if guy_rect.colliderect(car_rect):
            print("Écrasé ! Game Over.")
            collision = True
            game = False
            break

    if not collision:
        GuyPosx, GuyPosy = new_x, new_y

    Car2Posx += Car2Speed
    if Car2Posx <= 0 or Car2Posx >= SCREEN_WIDTH - CarSize[0]:
        Car2Speed *= -1

    Car3Posx += Car3Speed
    if Car3Posx <= 0 or Car3Posx >= SCREEN_WIDTH - CarSize[0]:
        Car3Speed *= -1

    Car4Posx += Car4Speed
    if Car4Posx <= 0 or Car4Posx >= SCREEN_WIDTH - CarSize[0]:
        Car4Speed *= -1

    Car5Posy += Car5Speed
    if Car5Posy <= 0 or Car5Posy >= SCREEN_HEIGHT - CarSize[1]:
        Car5Speed *= -1

    window.blit(background, (0, 0))
    window.blit(transform.rotate(Guy, angle), (GuyPosx, GuyPosy))
    window.blit(car2 if Car2Speed > 0 else transform.flip(car2, True, False), (Car2Posx, Car2Posy))
    window.blit(car3 if Car3Speed > 0 else transform.flip(car3, True, False), (Car3Posx, Car3Posy))
    window.blit(car4 if Car4Speed > 0 else transform.flip(car4, True, False), (Car4Posx, Car4Posy))

    car5_rotated = transform.rotate(car5, 90 if Car5Speed > 0 else -90)
    window.blit(car5_rotated, (Car5Posx, Car5Posy))

    display.update()

quit()