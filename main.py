import pygame

pygame.init()

window = pygame.display.set_mode((1200, 400))

track1 = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))

car_x = 155
car_y = 300
focal_dis = 25
direction = 'up'

cam_x_offset = 0
cam_y_offset = 0

drive = True

clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    clock.tick(60)
    cam_x = cam_x_offset + car_x + 15
    cam_y = cam_y_offset + car_y + 15

    up_pix = window.get_at((cam_x, cam_y - focal_dis))[0]
    right_pix = window.get_at((cam_x + focal_dis, cam_y))[0]
    down_pix = window.get_at((cam_x, cam_y + focal_dis))[0]
    left_pix =  window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_pix, right_pix)

    #change direction
    if direction == 'up' and up_pix != 255 and right_pix == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)

    elif direction == 'right' and right_pix != 255 and down_pix == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)

    elif direction == 'down' and down_pix != 255 and right_pix == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)

    elif direction == 'right' and right_pix != 255 and up_pix == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)

    #drive
    if direction == 'up' and up_pix == 255:
        car_y = car_y - 2

    elif direction == 'right' and right_pix == 255:
        car_x = car_x + 2

    elif direction == 'down' and down_pix == 255:
        car_y = car_y + 2

    window.blit(track1, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()