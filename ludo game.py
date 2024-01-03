import pygame
import time

import random

pygame.init()
font=pygame.font.SysFont(None,150)



screen=pygame.display.Info()
screen_width=screen.current_w
screen_height=screen.current_h
bord_width=1020
bord_height=1020
sift_x=(screen_width-bord_width)/2
sift_y=(screen_height-bord_height)/2.4


gamewindow=pygame.display.set_mode((screen_width,screen_height))


location_green= pygame.image.load("green.png")

location_red= pygame.image.load("red.png")


pygame.mixer.init()


fps=1
fack_dice_number=0 

# colour block
black=(0,0,0)
l_black=(80, 80,80)
white=(255, 255,255)
light=(230,230,230)
red=(255,0,0)
yellow=(255, 216,0) 
green=(0, 150,0)
blue=(51, 153,255)
#colour block end



clock=pygame.time.Clock()
gameover=False
winner="0"
red_cheat=0
green_cheat=0
timer=0
flage=1
number=1

#this variable used for parmition to run goti
red_flage=True
green_flage=False

red_a_signal=False
red_b_signal=False
red_c_signal=False
red_d_signal=False

green_a_signal=False
green_b_signal=False
green_c_signal=False
green_d_signal=False

dice_run=False
#this variable used for parmition to run goti

dice_number=0
safezoon=[0,1,9,14,22,27,35,40,48,52,53,54,55,56,57]
#green_safezoon=[]

#goti size start
size1=90
size2=80
size3=70
#goti_size end

#goti path start
yellow_root={0:{}}
red_root={0:{}}
green_root={0:{}}
blue_root={0:{}}
# goti path end

#goti current location
red_a_current=0
red_b_current=0
red_c_current=0
red_d_current=0

green_a_current=0
green_b_current=0
green_c_current=0
green_d_current=0

yellow_a_current=0
yellow_b_current=0
yellow_c_current=0
yellow_d_current=0

blue_a_current=0
blue_b_current=0
blue_c_current=0
blue_d_current=0
#goti current location end


#goti size
red_a_size=size1
red_b_size=size1
red_c_size=size1
red_d_size=size1

yellow_a_size=size1
yellow_b_size=size1
yellow_c_size=size1
yellow_d_size=size1

green_a_size=size1
green_b_size=size1
green_c_size=size1
green_d_size=size1

blue_a_size=size1
blue_b_size=size1
blue_c_size=size1
blue_d_size=size1
#goti size end

#goti image
red_goti_a_image=""
red_goti_b_image=""
red_goti_c_image=""
red_goti_d_image=""

green_goti_a_image=""
green_goti_b_image=""
green_goti_c_image=""
green_goti_d_image=""
#goti image end

#goti rect
red_a_goti_rect=(0, 0)
red_b_goti_rect=(0, 0)
red_c_goti_rect=(0, 0)
red_d_goti_rect=(0, 0)

green_a_goti_rect=(0, 0)
green_b_goti_rect=(0, 0)
green_c_goti_rect=(0, 0)
green_d_goti_rect=(0, 0)

red_dice_rect=(0, 0)
green_dice_rect=(0, 0)
#goti rect end

# block pogition
red_a_position="c"
red_b_position="c"
red_c_position="c"
red_d_position="c"

green_a_position="c"
green_b_position="c"
green_c_position="c"
green_d_position="c"

# block pogition end


def display_winner_name(text,colour,x,y):
    screen_text=font.render(text+" IS WINNER",True,colour)
    gamewindow.blit(screen_text,[x,y])
    pygame.display.update()
    
    pygame.mixer.music.load("Winner_sound.mp3")
    pygame.mixer.music.play()
    time.sleep(3)
    return 0
        
        

def logic():
     global green_a_position, green_b_position, green_c_position, green_d_position, red_a_position, red_b_position, red_c_position, red_d_position
     
     global green_a_size, green_b_size, green_c_size, green_d_size, red_a_size, red_b_size, red_c_size, red_d_size
     
     global red_flage, green_flage,dice_number, dice_run
     
     global red_a_signal, red_b_signal, red_c_signal, red_d_signal, green_a_current_a_signal, green_b_signal, green_c_signal, green_d_signal
     
     global red_a_current, red_b_current, red_c_current, red_d_current, green_a_current,green_b_current, green_c_current, green_d_current
     
     global winner
     
     
     if(red_a_current==57 and red_b_current==57 and red_c_current==57 and red_d_current==57):
         winner="RED"
         return 0
     if(green_a_current==57 and green_b_current==57 and green_c_current==57 and green_d_current==57):
         winner="GREEN"
         return 0
     
     green_a_position="c"
     green_b_position="c"
     green_c_position="c"
     green_d_position="c"
    
     red_a_position="c"
     red_b_position="c"
     red_c_position="c"
     red_d_position="c"
    
     green_a_size=size1
     green_b_size=size1
     green_c_size=size1
     green_d_size=size1
    
     red_a_size=size1
     red_b_size=size1
     red_c_size=size1
     red_d_size=size1
     
     global green_a_signal, green_b_signal, green_c_signal, green_d_signal, red_a_signal, red_b_signal, red_c_sgnal, red_d_signal
     
     
     red_a_signal=False
     red_b_signal=False
     red_c_signal=False
     red_d_signal=False
     
     green_a_signal=False
     green_b_signal=False
     green_c_signal=False
     green_d_signal=False
    
    
    # green goti pogition set logic
     if (green_a_current == green_b_current):
        if (green_b_position == 'c'):
            if (green_a_position == 'c'):
                green_a_position = 'lc'
                green_a_size=80
            elif (green_a_position == 'lc'):
                green_a_position = 'luc'
                green_a_size=70

        if (green_b_position == 'lc'):
            green_a_position = 'rc'
            green_a_size=80
        if (green_b_position == 'luc'):
            green_a_position = 'ruc'
            green_a_size=70
        if (green_b_position == 'ruc'):
            green_a_position = 'ldc'
            green_a_size=70
        if (green_b_position == 'ldc'):
            green_a_position = 'rdc'
            green_a_size=70
        if (green_a_current == 0 and green_b_current == 0):
            green_a_position = 'c'
            green_a_size=size1

     if (green_a_current == green_c_current):
        if (green_c_position == 'c'):
            if (green_a_position == 'c'):
                green_a_position = 'lc'
                green_a_size=80
            elif (green_a_position == 'lc'):
                green_a_position = 'luc'
                green_a_size=70

        if (green_c_position == 'lc'):
            green_a_position = 'rc'
            green_a_size=80
        if (green_c_position == 'luc'):
            green_a_position = 'ruc'
            green_a_size=70
        if (green_c_position == 'ruc'):
            green_a_position = 'ldc'
            green_a_size=70
        if (green_c_position == 'ldc'):
            green_a_position = 'rdc'
            green_a_size=70
        if (green_a_current == 0 and green_c_current == 0):
            green_a_position = 'c'
            green_a_size=size1

     if (green_a_current == green_d_current):
        if (green_d_position == 'c'):
            if (green_a_position == 'c'):
                green_a_position = 'lc'
                green_a_size=80
            elif (green_a_position == 'lc'):
                green_a_position = 'luc'
                green_a_size=70

        if (green_d_position == 'lc'):
            green_a_position = 'rc'
            green_a_size=80
        if (green_d_position == 'luc'):
            green_a_position = 'ruc'
            green_a_size=70
        if (green_d_position == 'ruc'):
            green_a_position = 'ldc'
            green_a_size=70
        if (green_d_position == 'ldc'):
            green_a_position = 'rdc'
            green_a_size=70
        if (green_a_current == 0 and green_d_current == 0):
            green_a_position = 'c'
            green_a_size=size1

     if (green_b_current == green_a_current):
        if (green_a_position == 'c'):
            if (green_b_position == 'c'):
                green_b_position = 'lc'
                green_b_size=80
            elif (green_b_position == 'lc'):
                green_b_position = 'luc'
                green_b_size=70

        if (green_a_position == 'lc'):
            green_b_position = 'rc'
            green_b_size=80
        if (green_a_position == 'luc'):
            green_b_position = 'ruc'
            green_b_size=70
        if (green_a_position == 'ruc'):
            green_b_position = 'ldc'
            green_b_size=70
        if (green_a_position == 'ldc'):
            green_b_position = 'rdc'
            green_b_size=70
        if (green_b_current == 0 and green_a_current == 0):
            green_b_position = 'c'
            green_b_size=size1

     if (green_b_current == green_c_current):
        if (green_c_position == 'c'):
            if (green_b_position == 'c'):
                green_b_position = 'lc'
                green_b_size=80
            elif (green_b_position == 'lc'):
                green_b_position = 'luc'
                green_b_size=70

        if (green_c_position == 'lc'):
            green_b_position = 'rc'
            green_b_size=80
        if (green_c_position == 'luc'):
            green_b_position = 'ruc'
            green_b_size=70
        if (green_c_position == 'ruc'):
            green_b_position = 'ldc'
            green_b_size=70
        if (green_c_position == 'ldc'):
            green_b_position = 'rdc'
            green_b_size=70
        if (green_b_current == 0 and green_c_current == 0):
            green_b_position = 'c'
            green_b_size=size1

     if (green_b_current == green_d_current):
        if (green_d_position == 'c'):
            if (green_b_position == 'c'):
                green_b_position = 'lc'
                green_b_size=80
            elif (green_b_position == 'lc'):
                green_b_position = 'luc'
                green_b_size=70

        if (green_d_position == 'lc'):
            green_b_position = 'rc'
            green_b_size=80
        if (green_d_position == 'luc'):
            green_b_position = 'ruc'
            green_b_size=70
        if (green_d_position == 'ruc'):
            green_b_position = 'ldc'
            green_b_size=70
        if (green_d_position == 'ldc'):
            green_b_position = 'rdc'
            green_b_size=70
        if (green_b_current == 0 and green_d_current == 0):
            green_b_position = 'c'
            green_b_size=size1

     if (green_c_current == green_a_current):
        if (green_a_position == 'c'):
            if (green_c_position == 'c'):
                green_c_position = 'lc'
                green_c_size=80
            elif (green_c_position == 'lc'):
                green_c_position = 'luc'
                green_c_size=70

        if (green_a_position == 'lc'):
            green_c_position = 'rc'
            green_c_size=80
        if (green_a_position == 'luc'):
            green_c_position = 'ruc'
            green_c_size=70
        if (green_a_position == 'ruc'):
            green_c_position = 'ldc'
            green_c_size=70
        if (green_a_position == 'ldc'):
            green_c_position = 'rdc'
            green_c_size=70
        if (green_c_current == 0 and green_a_current == 0):
            green_c_position = 'c'
            green_c_size=size1

     if (green_c_current == green_b_current):
        if (green_b_position == 'c'):
            if (green_c_position == 'c'):
                green_c_position = 'lc'
                green_c_size=80
            elif (green_c_position == 'lc'):
                green_c_position = 'luc'
                green_c_size=70

        if (green_b_position == 'lc'):
            green_c_position = 'rc'
            green_c_size=80
        if (green_b_position == 'luc'):
            green_c_position = 'ruc'
            green_c_size=70
        if (green_b_position == 'ruc'):
            green_c_position = 'ldc'
            green_c_size=70
        if (green_b_position == 'ldc'):
            green_c_position = 'rdc'
            green_c_size=70
        if (green_c_current == 0 and green_b_current == 0):
            green_c_position = 'c'
            green_c_size=size1

     if (green_c_current == green_d_current):
        if (green_d_position == 'c'):
            if (green_c_position == 'c'):
                green_c_position = 'lc'
                green_c_size=80
            elif (green_c_position == 'lc'):
                green_c_position = 'luc'
                green_c_size=70

        if (green_d_position == 'lc'):
            green_c_position = 'rc'
            green_c_size=80
        if (green_d_position == 'luc'):
            green_c_position = 'ruc'
            green_c_size=70
        if (green_d_position == 'ruc'):
            green_c_position = 'ldc'
            green_c_size=70
        if (green_d_position == 'ldc'):
            green_c_position = 'rdc'
            green_c_size=70
        if (green_c_current == 0 and green_d_current == 0):
            green_c_position = 'c'
            green_c_size=size1

     if (green_d_current == green_a_current):
        if (green_a_position == 'c'):
            if (green_d_position == 'c'):
                green_d_position = 'lc'
                green_d_size=80
            elif (green_d_position == 'lc'):
                green_d_position = 'luc'
                green_d_size=70

        if (green_a_position == 'lc'):
            green_d_position = 'rc'
            green_d_size=80
        if (green_a_position == 'luc'):
            green_d_position = 'ruc'
            green_d_size=70
        if (green_a_position == 'ruc'):
            green_d_position = 'ldc'
            green_d_size=70
        if (green_a_position == 'ldc'):
            green_d_position = 'rdc'
            green_d_size=70
        if (green_d_current == 0 and green_a_current == 0):
            green_d_position = 'c'
            green_d_size=size1

     if (green_d_current == green_b_current):
        if (green_b_position == 'c'):
            if (green_d_position == 'c'):
                green_d_position = 'lc'
                green_d_size=80
            elif (green_d_position == 'lc'):
                green_d_position = 'luc'
                green_d_size=70

        if (green_b_position == 'lc'):
            green_d_position = 'rc'
            green_d_size=80
        if (green_b_position == 'luc'):
            green_d_position = 'ruc'
            green_d_size=70
        if (green_b_position == 'ruc'):
            green_d_position = 'ldc'
            green_d_size=70
        if (green_b_position == 'ldc'):
            green_d_position = 'rdc'
            green_d_size=70
        if (green_d_current == 0 and green_b_current == 0):
            green_d_position = 'c'
            green_d_size=size1

     if (green_d_current == green_c_current):
        if (green_c_position == 'c'):
            if (green_d_position == 'c'):
                green_d_position = 'lc'
                green_d_size=80
            elif (green_d_position == 'lc'):
                green_d_position = 'luc'
                green_d_size=70

        if (green_c_position == 'lc'):
            green_d_position = 'rc'
            green_d_size=80
        if (green_c_position == 'luc'):
            green_d_position = 'ruc'
            green_d_size=70
        if (green_c_position == 'ruc'):
            green_d_position = 'ldc'
            green_d_size=70
        if (green_c_position == 'ldc'):
            green_d_position = 'rdc'
            green_d_size=70
        if (green_d_current == 0 and green_c_current == 0):
            green_d_position = 'c'
            green_d_size=size1
     # green goti pogition set logic end
            
            
            
     # red goti pogition set logic
     if (red_a_current == red_b_current):
        if (red_b_position == 'c'):
            if (red_a_position == 'c'):
                red_a_position = 'lc'
                red_a_size=80
            elif (red_a_position == 'lc'):
                red_a_position = 'luc'
                red_a_size=70

        if (red_b_position == 'lc'):
            red_a_position = 'rc'
            red_a_size=80
        if (red_b_position == 'luc'):
            red_a_position = 'ruc'
            red_a_size=70
        if (red_b_position == 'ruc'):
            red_a_position = 'ldc'
            red_a_size=70
        if (red_b_position == 'ldc'):
            red_a_position = 'rdc'
            red_a_size=70
        if (red_a_current == 0 and red_b_current == 0):
            red_a_position = 'c'
            red_a_size=size1

     if (red_a_current == red_c_current):
        if (red_c_position == 'c'):
            if (red_a_position == 'c'):
                red_a_position = 'lc'
                red_a_size=80
            elif (red_a_position == 'lc'):
                red_a_position = 'luc'
                red_a_size=70

        if (red_c_position == 'lc'):
            red_a_position = 'rc'
            red_a_size=80
        if (red_c_position == 'luc'):
            red_a_position = 'ruc'
            red_a_size=70
        if (red_c_position == 'ruc'):
            red_a_position = 'ldc'
            red_a_size=70
        if (red_c_position == 'ldc'):
            red_a_position = 'rdc'
            green_a_size=70
        if (red_a_current == 0 and red_c_current == 0):
            red_a_position = 'c'
            red_a_size=size1

     if (red_a_current == red_d_current):
        if (red_d_position == 'c'):
            if (red_a_position == 'c'):
                red_a_position = 'lc'
                red_a_size=80
            elif (red_a_position == 'lc'):
                red_a_position = 'luc'
                red_a_size=70

        if (red_d_position == 'lc'):
            red_a_position = 'rc'
            red_a_size=80
        if (red_d_position == 'luc'):
            red_a_position = 'ruc'
            red_a_size=70
        if (red_d_position == 'ruc'):
            red_a_position = 'ldc'
            red_a_size=70
        if (red_d_position == 'ldc'):
            red_a_position = 'rdc'
            red_a_size=70
        if (red_a_current == 0 and red_d_current == 0):
            red_a_position = 'c'
            red_a_size=size1

     if (red_b_current == red_a_current):
        if (red_a_position == 'c'):
            if (red_b_position == 'c'):
                red_b_position = 'lc'
                red_b_size=80
            elif (red_b_position == 'lc'):
                red_b_position = 'luc'
                red_b_size=70

        if (red_a_position == 'lc'):
            red_b_position = 'rc'
            red_b_size=80
        if (red_a_position == 'luc'):
            red_b_position = 'ruc'
            red_b_size=70
        if (red_a_position == 'ruc'):
            red_b_position = 'ldc'
            red_b_size=70
        if (red_a_position == 'ldc'):
            red_b_position = 'rdc'
            red_b_size=70
        if (red_b_current == 0 and red_a_current == 0):
            red_b_position = 'c'
            red_b_size=size1

     if (red_b_current == red_c_current):
        if (red_c_position == 'c'):
            if (red_b_position == 'c'):
                red_b_position = 'lc'
                red_b_size=80
            elif (red_b_position == 'lc'):
                red_b_position = 'luc'
                red_b_size=70

        if (red_c_position == 'lc'):
            red_b_position = 'rc'
            red_b_size=80
        if (red_c_position == 'luc'):
            red_b_position = 'ruc'
            red_b_size=70
        if (red_c_position == 'ruc'):
            red_b_position = 'ldc'
            red_b_size=70
        if (red_c_position == 'ldc'):
            red_b_position = 'rdc'
            red_b_size=70
        if (red_b_current == 0 and red_c_current == 0):
            red_b_position = 'c'
            red_b_size=size1

     if (red_b_current == red_d_current):
        if (red_d_position == 'c'):
            if (red_b_position == 'c'):
                red_b_position = 'lc'
                red_b_size=80
            elif (red_b_position == 'lc'):
                red_b_position = 'luc'
                red_b_size=70

        if (red_d_position == 'lc'):
            red_b_position = 'rc'
            red_b_size=80
        if (red_d_position == 'luc'):
            red_b_position = 'ruc'
            red_b_size=70
        if (red_d_position == 'ruc'):
            red_b_position = 'ldc'
            red_b_size=70
        if (red_d_position == 'ldc'):
            red_b_position = 'rdc'
            red_b_size=70
        if (red_b_current == 0 and red_d_current == 0):
            red_b_position = 'c'
            red_b_size=size1

     if (red_c_current == red_a_current):
        if (red_a_position == 'c'):
            if (red_c_position == 'c'):
                red_c_position = 'lc'
                red_c_size=80
            elif (red_c_position == 'lc'):
                red_c_position = 'luc'
                red_c_size=70

        if (red_a_position == 'lc'):
            red_c_position = 'rc'
            red_c_size=80
        if (red_a_position == 'luc'):
            red_c_position = 'ruc'
            red_c_size=70
        if (red_a_position == 'ruc'):
            red_c_position = 'ldc'
            red_c_size=70
        if (red_a_position == 'ldc'):
            red_c_position = 'rdc'
            red_c_size=70
        if (red_c_current == 0 and red_a_current == 0):
            red_c_position = 'c'
            red_c_size=size1

     if (red_c_current == red_b_current):
        if (red_b_position == 'c'):
            if (red_c_position == 'c'):
                red_c_position = 'lc'
                red_c_size=80
            elif (red_c_position == 'lc'):
                red_c_position = 'luc'
                red_c_size=70

        if (red_b_position == 'lc'):
            red_c_position = 'rc'
            red_c_size=80
        if (red_b_position == 'luc'):
            red_c_position = 'ruc'
            red_c_size=70
        if (red_b_position == 'ruc'):
            red_c_position = 'ldc'
            red_c_size=70
        if (red_b_position == 'ldc'):
            red_c_position = 'rdc'
            red_c_size=70
        if (red_c_current == 0 and red_b_current == 0):
            red_c_position = 'c'
            red_c_size=size1

     if (red_c_current == red_d_current):
        if (red_d_position == 'c'):
            if (red_c_position == 'c'):
                red_c_position = 'lc'
                red_c_size=80
            elif (red_c_position == 'lc'):
                red_c_position = 'luc'
                red_c_size=70

        if (red_d_position == 'lc'):
            red_c_position = 'rc'
            red_c_size=80
        if (red_d_position == 'luc'):
            red_c_position = 'ruc'
            red_c_size=70
        if (red_d_position == 'ruc'):
            red_c_position = 'ldc'
            red_c_size=70
        if (red_d_position == 'ldc'):
            red_c_position = 'rdc'
            red_c_size=70
        if (red_c_current == 0 and red_d_current == 0):
            red_c_position = 'c'
            red_c_size=size1

     if (red_d_current == red_a_current):
        if (red_a_position == 'c'):
            if (red_d_position == 'c'):
                red_d_position = 'lc'
                red_d_size=80
            elif (red_d_position == 'lc'):
                red_d_position = 'luc'
                red_d_size=70

        if (red_a_position == 'lc'):
            red_d_position = 'rc'
            red_d_size=80
        if (red_a_position == 'luc'):
            red_d_position = 'ruc'
            red_d_size=70
        if (red_a_position == 'ruc'):
            red_d_position = 'ldc'
            red_d_size=70
        if (red_a_position == 'ldc'):
            red_d_position = 'rdc'
            red_d_size=70
        if (red_d_current == 0 and red_a_current == 0):
            red_d_position = 'c'
            red_d_size=size1

     if (red_d_current == red_b_current):
        if (red_b_position == 'c'):
            if (red_d_position == 'c'):
                red_d_position = 'lc'
                red_d_size=80
            elif (red_d_position == 'lc'):
                red_d_position = 'luc'
                red_d_size=70

        if (red_b_position == 'lc'):
            red_d_position = 'rc'
            red_d_size=80
        if (red_b_position == 'luc'):
            red_d_position = 'ruc'
            red_d_size=70
        if (red_b_position == 'ruc'):
            red_d_position = 'ldc'
            red_d_size=70
        if (red_b_position == 'ldc'):
            red_d_position = 'rdc'
            red_d_size=70
        if (red_d_current == 0 and red_b_current == 0):
            red_d_position = 'c'
            red_d_size=size1

     if (red_d_current == red_c_current):
        if (red_c_position == 'c'):
            if (red_d_position == 'c'):
                red_d_position = 'lc'
                red_d_size=80
            elif (red_d_position == 'lc'):
                red_d_position = 'luc'
                red_d_size=70

        if (red_c_position == 'lc'):
            red_d_position = 'rc'
            red_d_size=80
        if (red_c_position == 'luc'):
            red_d_position = 'ruc'
            red_d_size=70
        if (red_c_position == 'ruc'):
            red_d_position = 'ldc'
            red_d_size=70
        if (red_c_position == 'ldc'):
            red_d_position = 'rdc'
            red_d_size=70
        if (red_d_current == 0 and red_c_current == 0):
            red_d_position = 'c'
            red_d_size=size1
        # red goti pogition set logic end
            
        
       #  goti singnal provide
       
     if(red_flage==True and dice_run==True):
            
            
            if(dice_number>=1 and dice_number<=6):
                    if(red_a_current!=0 and red_a_current+dice_number<=57):
                        red_a_signal=True
                        
                    if(red_b_current!=0 and red_b_current+dice_number<=57):
                        red_b_signal=True
                        
                    if(red_c_current!=0 and red_c_current+dice_number<=57):
                        red_c_signal=True
                        
                    if(red_d_current!=0 and red_d_current+dice_number<=57):
                        red_d_signal=True
                        
                        
                    if(red_a_current==0 and dice_number==6):
                        red_a_signal=True
                        
                    if(red_b_current==0 and dice_number==6):
                        red_b_signal=True
                        
                    if(red_c_current==0 and dice_number==6):
                        red_c_signal=True
                        
                    if(red_d_current==0 and dice_number==6):
                        red_d_signal=True
                        
                
            if(red_a_signal==False and red_b_signal==False and red_c_signal==False and red_d_signal==False):
                        green_flage=True
                        red_flage=False
                        dice_number=0
                        dice_run=False        
             
            
                 
                
                
            
     if(green_flage==True and dice_run==True):
                
            if(dice_number>=1 and dice_number<=6):
                    if(green_a_current!=0 and green_a_current+dice_number<=57):
                        green_a_signal=True
                        
                    if(green_b_current!=0 and green_b_current+dice_number<=57):
                        green_b_signal=True
                        
                    if(green_c_current!=0 and green_c_current+dice_number<=57):
                        green_c_signal=True
                        
                    if(green_d_current!=0 and green_d_current+dice_number<=57):
                        green_d_signal=True
                        
                    if(green_a_current==0 and dice_number==6):
                        green_a_signal=True
                        
                    if(green_b_current==0 and dice_number==6):
                        green_b_signal=True
                        
                    if(green_c_current==0 and dice_number==6):
                        green_c_signal=True
                        
                    if(green_d_current==0 and dice_number==6):
                        green_d_signal=True
                        
            if(green_a_signal==False and green_b_signal==False and green_c_signal==False and green_d_signal==False):
                        red_flage=True
                        green_flage=False
                        dice_number=0
                        dice_run=False
                        
        # goti singnal provide end
        
        # goti colide and return to home
     
                
        # goti colide and return to home
     
        
            
      
     return 0

def goti_maar(key=0):
    global red_flage, green_flage, dice_number, dice_run
    
    global red_a_current, red_b_current, red_c_current, red_d_current, green_a_current,green_b_current, green_c_current, green_d_current
    
    #goti mar code
    if(red_flage==True and dice_run==False):
             if(abs(red_a_current-green_a_current)==26):
                    if(green_a_current not in safezoon and red_a_current not in safezoon):
                        green_a_current=0
                        dice_number=6
                        
                    
             if(abs(red_a_current-green_b_current)==26):
                    if(green_b_current not in safezoon and red_a_current not in safezoon):
                        green_b_current=0
                        dice_number=6
                    
                    
             if(abs(red_a_current-green_c_current)==26):
                    if(green_c_current not in safezoon and red_a_current not in safezoon):
                        green_c_current=0
                        dice_number=6
                    
                    
             if(abs(red_a_current-green_d_current)==26):
                    if(green_d_current not in safezoon and red_a_current not in safezoon):
                        green_d_current=0
                        dice_number=6
            
               
                    
           
             if(abs(red_b_current-green_a_current)==26):
                    if(green_a_current not in safezoon and red_b_current not in safezoon):
                        green_a_current=0
                        dice_number=6
                    
             if(abs(red_b_current-green_b_current)==26):
                  if(green_b_current not in safezoon and red_b_current not in safezoon):
                        green_b_current=0
                        dice_number=6
                  
             if(abs(red_b_current-green_c_current)==26):
                    if(green_c_current not in safezoon and red_b_current not in safezoon):
                        green_c_current=0
                        dice_number=6
                        
             if(abs(red_b_current-green_d_current)==26):
                    if(green_d_current not in safezoon and red_b_current not in safezoon):
                        green_d_current=0
                        dice_number=6
                    
            
             if(abs(red_c_current-green_a_current)==26):
                    if(green_a_current not in safezoon and red_c_current not in safezoon):
                        green_a_current=0
                        dice_number=6
                        
             if(abs(red_c_current-green_b_current)==26):
                    if(green_b_current not in safezoon and red_c_current not in safezoon):
                        green_b_current=0
                        dice_number=6
                        
             if(abs(red_c_current-green_c_current)==26):
                   if(green_c_current not in safezoon and red_c_current not in safezoon):
                        green_c_current=0
                        dice_number=6
                        
             if(abs(red_c_current-green_d_current)==26):
                    if(green_d_current not in safezoon and red_c_current not in safezoon):
                        green_d_current=0
                        dice_number=6
                    
            
             if(abs(red_d_current-green_a_current)==26):
                    if(green_a_current not in safezoon and red_d_current not in safezoon):
                        green_a_current=0
                        dice_number=6
                        
             if(abs(red_d_current-green_b_current)==26):
                    if(green_b_current not in safezoon and red_d_current not in safezoon):
                        green_b_current=0
                        dice_number=6
                        
             if(abs(red_d_current-green_c_current)==26):
                    if(green_c_current not in safezoon and red_d_current not in safezoon):
                        green_c_current=0
                        dice_number=6
                        
             if(abs(red_d_current-green_d_current)==26):
                    if(green_d_current not in safezoon and red_d_current not in safezoon):
                        green_d_current=0
                        dice_number=6
                
                
    if(green_flage==True and dice_run==False):
            
             if(abs(green_a_current-red_a_current)==26):
                    if(red_a_current not in safezoon and green_a_current not in safezoon):
                        red_a_current=0
                        dice_number=6
                        
             if(abs(green_a_current-red_b_current)==26):
                    if(red_b_current not in safezoon and green_a_current not in safezoon):
                        red_b_current=0
                        dice_number=6
                        
             if(abs(green_a_current-red_c_current)==26):
                    if(red_c_current not in safezoon and green_a_current not in safezoon):
                        red_c_current=0
                        dice_number=6
                        
             if(abs(green_a_current-red_d_current)==26):
                    if(red_d_current not in safezoon and green_a_current not in safezoon):
                        red_d_current=0
                        dice_number=6
                    
             if(abs(green_b_current-red_a_current)==26):
                    if(red_a_current not in safezoon and green_b_current not in safezoon):
                        red_a_current=0
                        dice_number=6
                        
             if(abs(green_b_current-red_b_current)==26):
                   if(red_b_current not in safezoon  and green_b_current not in safezoon):
                        red_b_current=0
                        dice_number=6
                        
             if(abs(green_b_current-red_c_current)==26):
                    if(red_c_current not in safezoon and green_b_current not in safezoon):
                        red_c_current=0
                        dice_number=6
                        
             if(abs(green_b_current-red_d_current)==26):
                    if(red_d_current not in safezoon and green_b_current not in safezoon):
                        red_d_current=0
                        dice_number=6
                    
             if(abs(green_c_current-red_a_current)==26):
                    if(red_a_current not in safezoon and green_c_current not in safezoon):
                        red_a_current=0
                        dice_number=6
                        
             if(abs(green_c_current-red_b_current)==26):
                    if(red_b_current not in safezoon and green_c_current not in safezoon):
                        red_b_current=0
                        dice_number=6
                        
             if(abs(green_c_current-red_c_current)==26):
                    if(red_c_current not in safezoon and green_c_current not in safezoon):
                        red_c_current=0
                        dice_number=6
                        
             if(abs(green_c_current-red_d_current)==26):
                    if(red_d_current not in safezoon and green_c_current not in safezoon):
                        red_d_current=0
                        dice_number=6
                    
             if(abs(green_d_current-red_a_current)==26):
                    if(red_a_current not in safezoon and green_d_current not in safezoon):
                        red_a_current=0
                        dice_number=6
                        
             if(abs(green_d_current-red_b_current)==26):
                    if(red_b_current not in safezoon and green_d_current not in safezoon):
                        red_b_current=0
                        dice_number=6
                        
             if(abs(green_d_current-red_c_current)==26):
                    if(red_c_current not in safezoon and green_d_current not in safezoon):
                        red_c_current=0
                        dice_number=6
                        
             if(abs(green_d_current-red_d_current)==26):
                    if(red_d_current not in safezoon and green_d_current not in safezoon):
                        red_d_current=0
                        dice_number=6
    #goti mar code
    
    
    if(red_flage==True and key==1):
            if (dice_number==6):
                                    green_flage=False
                                    red_flage=True
                                    
            else:
                                
                                green_flage=True
                                red_flage=False
            dice_number=0
            #dice_run=False
            
    if(green_flage==True and key==2):
            if (dice_number==6):
                                    red_flage=False
                                    green_flage=True
                                    
            else:
                                
                                red_flage=True
                                green_flage=False
            dice_number=0
            #dice_run=False
    
    return 0

def image_pogition_set(name):
       sort_name=name.split('_')[0]
       position='c'
       size="100"
       
       if(name=="red_a"):
           position=red_a_position
           size=red_a_size
           if(red_a_current==0):
                tup=red_root[0]['a']
           else:
                tup=red_root[red_a_current]
                
       elif(name=="red_b"):
           position=red_b_position
           size=red_b_size
           if(red_b_current==0):
                tup=red_root[0]['b']
           else:
                tup=red_root[red_b_current]
                
       elif(name=="red_c"):
           position=red_c_position
           size=red_c_size
           if(red_c_current==0):
                tup=red_root[0]['c']
           else:
                tup=red_root[red_c_current]
                
       elif(name=="red_d"):
           position=red_d_position
           size=red_d_size
           if(red_d_current==0):
                tup=red_root[0]['d']
           else:
                tup=red_root[red_d_current]
       
       
       elif(name=="green_a"):
           position=green_a_position
           size=green_a_size
           if(green_a_current==0):
                tup=green_root[0]['a']
           else:
                tup=green_root[green_a_current]
                
       elif(name=="green_b"):
           position=green_b_position
           size=green_b_size
           if(green_b_current==0):
                tup=green_root[0]['b']
           else:
                tup=green_root[green_b_current]
                
       elif(name=="green_c"):
           position=green_c_position
           size=green_c_size
           if(green_c_current==0):
                tup=green_root[0]['c']
           else:
                tup=green_root[green_c_current]
                
       elif(name=="green_d"):
           position=green_d_position
           size=green_d_size
           if(green_d_current==0):
                tup=green_root[0]['d']
           else:
                tup=green_root[green_d_current]
           
                
                          
       if(position=="c"):
           tup2=(size//2,size*95//100)
           tup3=(tup[0]+33.5-tup2[0],tup[1]+33.5-tup2[1])
       elif(position=="lc"):
           tup2=(size//2,size*95//100)
           tup3=(tup[0]+20-tup2[0],tup[1]+33.5-tup2[1])
       elif(position=="rc"):
           tup2=(size//2,size*95//100)
           tup3=(tup[0]+46-tup2[0],tup[1]+33.5-tup2[1])
           
       if(sort_name=='green'):
           if(position=="luc"):
               tup2=(size//2,size*95//100)
               tup3=(tup[0]+15-tup2[0],tup[1]+15-tup2[1])
           elif(position=="ruc"):
               tup2=(size//2,size*95//100)
               tup3=(tup[0]+51-tup2[0],tup[1]+15-tup2[1])
           elif(position=="ldc"):
               tup2=(size//2,size*95//100)
               tup3=(tup[0]+15-tup2[0],tup[1]+51-tup2[1])
           elif(position=="rdc"):
               tup2=(size//2,size*95//100)
               tup3=(tup[0]+51-tup2[0],tup[1]+51-tup2[1])
               
       if(sort_name=='red'):
           if(position=="luc"):
               tup2=(size//2,size*80//100)
               tup3=(tup[0]+51-tup2[0],tup[1]+51-tup2[1])
               
           elif(position=="ruc"):
               tup2=(size//2,size*80//100)
               tup3=(tup[0]+15-tup2[0],tup[1]+51-tup2[1])
               
           elif(position=="ldc"):
               tup2=(size//2,size*80//100)
               tup3=(tup[0]+51-tup2[0],tup[1]+15-tup2[1])
               
           elif(position=="rdc"):
               tup2=(size//2,size*80//100)
               tup3=(tup[0]+15-tup2[0],tup[1]+15-tup2[1])
               
               
               
           
       
           
           
       
       return tup3

  
 
 
def dice():
     global number
     
     global red_dice_rect
     global green_dice_rect
     global fack_dice_number
     
     
     play_button= pygame.image.load("play.png")
     
     play_button = pygame.transform.scale(play_button, (180, 180))
     red_dice_rect=play_button.get_rect()
     play_button = pygame.transform.scale(play_button, (180, 180))
     green_dice_rect=play_button.get_rect()
     
     
     red_box_x=sift_x+1020-208
     red_box_y=sift_y-208-20
     
     green_box_x=sift_x
     green_box_y=sift_y+1020+20
     
     pygame.draw.rect(gamewindow, red, [red_box_x,red_box_y ,208,208])
     pygame.draw.rect(gamewindow, yellow, [30,red_box_y ,208,208])
     pygame.draw.rect(gamewindow, green, [green_box_x, green_box_y, 208,208])
     pygame.draw.rect(gamewindow, blue, [840, green_box_y, 208,208])
     
     #cheat block drow
     
     
     # green butten
     global rect6, rect5, rect4, rect3, rect2, rect1
     rect6=pygame.draw.rect(gamewindow, white, [30,1830, 340,170])
     rect5=pygame.draw.rect(gamewindow, white, [370,1830, 340,170])
     rect4=pygame.draw.rect(gamewindow, white, [710,1830, 340,170])
     rect3=pygame.draw.rect(gamewindow, white, [30,2000, 340,170]) 
     rect2=pygame.draw.rect(gamewindow, white, [370,2000, 340,170])
     rect1=pygame.draw.rect(gamewindow, white, [710,2000, 340,170])
     # green butten
     
     # red butten
     global rec6, rec5, rec4, rec3, rec2, rec1
     rec6=pygame.draw.rect(gamewindow,white, [30,5, 340,170])
     rec5=pygame.draw.rect(gamewindow,white, [370,5, 340,170])
     rec4=pygame.draw.rect(gamewindow,white, [710,5, 340,170])
     rec3=pygame.draw.rect(gamewindow, white, [30,169, 340,170]) 
     rec2=pygame.draw.rect(gamewindow, white, [370,169, 340,170])
     rec1=pygame.draw.rect(gamewindow,white, [710,169, 340,170])
     # red butten
     #cheat block drow
     
     
     if(red_flage==True):
             
             x=red_box_x+14
             y=red_box_y+14
             red_dice_rect.x=x
             red_dice_rect.y=y
             
     if(green_flage==True):
         
         
         x=green_box_x+14
         y=green_box_y+14
         green_dice_rect.x=x
         green_dice_rect.y=y
         
     
     if(dice_run==False):
         gamewindow.blit(play_button,(x, y))
         
     
     else:
         
         
         
             
             
             
          
         
         
         if(fack_dice_number==0):
             global dice_number
             
             if (dice_number==0):
                 pygame.mixer.music.load("Dice_sound.mp3")
                 pygame.mixer.music.play()
                 #time.sleep(0.5)
                 dice_number=random.randint(1,6)
                 
         else:
              pygame.mixer.music.load("Dice_sound.mp3")
              pygame.mixer.music.play()
              #time.sleep(0.5)
              dice_number=fack_dice_number
              fack_dice_number=0
              
         
             
         dice= pygame.image.load(f"{dice_number}.png")
         dice = pygame.transform.scale(dice, (180, 180)) 
         gamewindow.blit(dice,(x, y))
         
         
         
     return 0     
  
    
    



def root():
    def fun(x,y,count):
        
        wight=bord_width-15
        height=bord_height-15

        box=(wight/5)*2
        if(count==1):
            #yellow
            tamp_root=yellow_root
            
            #root block make start
            count=1
            i=x-0.5
            j=y+box-0.5
            
            while(count!=19):
                # root provide code start
                if(count==1):
                    tup=(i, j) 
                    
                    red_root.update({(39):tup})
                    blue_root.update({(26):tup})
                    green_root.update({(13):tup})
                     
                if(count==2):
                    tup=(i, j)
                    yellow_root.update({(51):tup})
                    red_root.update({(38):tup})
                    blue_root.update({(25):tup}) 
                    green_root.update({(12):tup})
                
                if(count==3):
                    tup=(i, j)
                    yellow_root.update({(50):tup})
                    red_root.update({(37):tup}) 
                    blue_root.update({(24):tup})
                    green_root.update({(11):tup})
                if(count==4):
                    tup=(i, j)
                    yellow_root.update({(1):tup})
                    red_root.update({(40):tup})
                    blue_root.update({(27):tup})
                    green_root.update({(14):tup})
                     
                if(count==5):
                    tup=(i, j)
                    yellow_root.update({(52):tup})
                if(count==6):
                    tup=(i, j)
                    yellow_root.update({(49):tup})
                    red_root.update({(36):tup}) 
                    blue_root.update({(23):tup})
                    green_root.update({(10):tup})
                
                if(count==7):
                    tup=(i, j)
                    yellow_root.update({(2):tup})
                    red_root.update({(41):tup})
                    blue_root.update({(28):tup})
                    green_root.update({(15):tup})
                     
                if(count==8):
                    tup=(i, j)
                    yellow_root.update({(53):tup})
                if(count==9):
                    tup=(i, j)
                    yellow_root.update({(48):tup})
                    red_root.update({(35):tup}) 
                    blue_root.update({(22):tup})
                    green_root.update({(9):tup})
                if(count==10):
                    tup=(i, j)
                    yellow_root.update({(3):tup})
                    red_root.update({(42):tup})
                    blue_root.update({(29):tup})
                    green_root.update({(16):tup})
                     
                if(count==11):
                    tup=(i, j)
                    yellow_root.update({(54):tup})
                if(count==12):
                    tup=(i, j)
                    yellow_root.update({(47):tup})
                    red_root.update({(34):tup}) 
                    blue_root.update({(21):tup})
                    green_root.update({(8):tup})
                if(count==13):
                    tup=(i, j)
                    yellow_root.update({(4):tup})
                    red_root.update({(43):tup})
                    blue_root.update({(30):tup}) 
                    green_root.update({(17):tup})
                     
                if(count==14):
                    tup=(i, j)
                    yellow_root.update({(55):tup}) 
                if(count==15):
                    tup=(i, j)
                    yellow_root.update({(46):tup})
                    red_root.update({(33):tup}) 
                    blue_root.update({(20):tup})
                    green_root.update({(7):tup})
                if(count==16):
                    tup=(i, j)
                    yellow_root.update({(5):tup})
                    red_root.update({(44):tup})
                    blue_root.update({(31):tup})
                    green_root.update({(18):tup})
                if(count==17):
                    tup=(i, j)
                    yellow_root.update({(56):tup})
                    tup=(i+67, j)
                    yellow_root.update({(57):tup})
                    
                if(count==18):
                    tup=(i, j)
                    yellow_root.update({(45):tup})
                    red_root.update({(32):tup}) 
                    blue_root.update({(19):tup})
                    green_root.update({(6):tup})
                if(count%3==0):
                    i+=67
                    j=y+box-0.5
                else:
                    j=j+67
                count+=1
            #root block make end
            
            
        elif(count==2):
            #red
            tamp_root=red_root
            #root block make start
            
            count=1
            i=x+box-0.5+134
            j=y-0.5
            while(count!=19):
                # root provide code start
                if(count==1):
                    tup=(i, j)
                    
                    blue_root.update({(39):tup})
                    green_root.update({(26):tup})
                    yellow_root.update({(13):tup})
                     
                if(count==2):
                    tup=(i, j)
                    red_root.update({(51):tup})
                    blue_root.update({(38):tup})
                    green_root.update({(25):tup}) 
                    yellow_root.update({(12):tup})
                
                if(count==3):
                    tup=(i, j)
                    red_root.update({(50):tup})
                    blue_root.update({(37):tup}) 
                    green_root.update({(24):tup})
                    yellow_root.update({(11):tup})
                if(count==4):
                    tup=(i, j)
                    red_root.update({(1):tup})
                    blue_root.update({(40):tup})
                    green_root.update({(27):tup})
                    yellow_root.update({(14):tup})
                     
                if(count==5):
                    tup=(i, j)
                    red_root.update({(52):tup})
                if(count==6):
                    tup=(i, j)
                    red_root.update({(49):tup})
                    blue_root.update({(36):tup}) 
                    green_root.update({(23):tup})
                    yellow_root.update({(10):tup})
                
                if(count==7):
                    tup=(i, j)
                    red_root.update({(2):tup})
                    blue_root.update({(41):tup})
                    green_root.update({(28):tup})
                    yellow_root.update({(15):tup})
                     
                if(count==8):
                    tup=(i, j)
                    red_root.update({(53):tup})
                if(count==9):
                    tup=(i, j)
                    red_root.update({(48):tup})
                    blue_root.update({(35):tup}) 
                    green_root.update({(22):tup})
                    yellow_root.update({(9):tup})
                if(count==10):
                    tup=(i, j)
                    red_root.update({(3):tup})
                    blue_root.update({(42):tup})
                    green_root.update({(29):tup})
                    yellow_root.update({(16):tup})
                     
                if(count==11):
                    tup=(i, j)
                    red_root.update({(54):tup})
                if(count==12):
                    tup=(i, j)
                    red_root.update({(47):tup})
                    blue_root.update({(34):tup}) 
                    green_root.update({(21):tup})
                    yellow_root.update({(8):tup})
                if(count==13):
                    tup=(i, j)
                    red_root.update({(4):tup})
                    blue_root.update({(43):tup})
                    green_root.update({(30):tup}) 
                    yellow_root.update({(17):tup})
                     
                if(count==14):
                    tup=(i, j)
                    red_root.update({(55):tup}) 
                if(count==15):
                    tup=(i, j)
                    red_root.update({(46):tup})
                    blue_root.update({(33):tup}) 
                    green_root.update({(20):tup})
                    yellow_root.update({(7):tup})
                if(count==16):
                    tup=(i, j)
                    red_root.update({(5):tup})
                    blue_root.update({(44):tup})
                    green_root.update({(31):tup})
                    yellow_root.update({(18):tup})
                if(count==17):
                    tup=(i, j)
                    red_root.update({(56):tup})
                    tup=(i, j+67)
                    red_root.update({(57):tup})
                    
                if(count==18):
                    tup=(i, j)
                    red_root.update({(45):tup})
                    blue_root.update({(32):tup}) 
                    green_root.update({(19):tup})
                    yellow_root.update({(6):tup})
                
                if(count%3==0):
                    j+=67
                    i=x+box-0.5+134
                else:
                    i=i-67
               
                count+=1

            x = x + wight - box
            #root block make end
            
            
        elif(count==3):
            #green
            tamp_root=green_root

            #root block make start
            count=1
            i=x+box-0.5
            j=y+box*2.5-67-0.5
            while(count!=19):
                # root provide code start
                if(count==1):
                    tup=(i, j)
                    
                    yellow_root.update({(39):tup})
                    red_root.update({(26):tup})
                    blue_root.update({(13):tup})
                     
                if(count==2):
                    tup=(i, j)
                    green_root.update({(51):tup})
                    yellow_root.update({(38):tup})
                    red_root.update({(25):tup}) 
                    blue_root.update({(12):tup})
                
                if(count==3):
                    tup=(i, j)
                    green_root.update({(50):tup})
                    yellow_root.update({(37):tup}) 
                    red_root.update({(24):tup})
                    blue_root.update({(11):tup})
                if(count==4):
                    tup=(i, j)
                    green_root.update({(1):tup})
                    yellow_root.update({(40):tup})
                    red_root.update({(27):tup})
                    blue_root.update({(14):tup})
                     
                if(count==5):
                    tup=(i, j)
                    green_root.update({(52):tup})
                if(count==6):
                    tup=(i, j)
                    green_root.update({(49):tup})
                    yellow_root.update({(36):tup}) 
                    red_root.update({(23):tup})
                    blue_root.update({(10):tup})
                
                if(count==7):
                    tup=(i, j)
                    green_root.update({(2):tup})
                    yellow_root.update({(41):tup})
                    red_root.update({(28):tup})
                    blue_root.update({(15):tup})
                     
                if(count==8):
                    tup=(i, j)
                    green_root.update({(53):tup})
                if(count==9):
                    tup=(i, j)
                    green_root.update({(48):tup})
                    yellow_root.update({(35):tup}) 
                    red_root.update({(22):tup})
                    blue_root.update({(9):tup})
                if(count==10):
                    tup=(i, j)
                    green_root.update({(3):tup})
                    yellow_root.update({(42):tup})
                    red_root.update({(29):tup})
                    blue_root.update({(16):tup})
                     
                if(count==11):
                    tup=(i, j)
                    green_root.update({(54):tup})
                if(count==12):
                    tup=(i, j)
                    green_root.update({(47):tup})
                    yellow_root.update({(34):tup}) 
                    red_root.update({(21):tup})
                    blue_root.update({(8):tup})
                if(count==13):
                    tup=(i, j)
                    green_root.update({(4):tup})
                    yellow_root.update({(43):tup})
                    red_root.update({(30):tup}) 
                    blue_root.update({(17):tup})
                     
                if(count==14):
                    tup=(i, j)
                    green_root.update({(55):tup}) 
                if(count==15):
                    tup=(i, j)
                    green_root.update({(46):tup})
                    yellow_root.update({(33):tup}) 
                    red_root.update({(20):tup})
                    blue_root.update({(7):tup})
                if(count==16):
                    tup=(i, j)
                    green_root.update({(5):tup})
                    yellow_root.update({(44):tup})
                    red_root.update({(31):tup})
                    blue_root.update({(18):tup})
                if(count==17):
                    tup=(i, j)
                    green_root.update({(56):tup})
                    tup=(i, j-67)
                    green_root.update({(57):tup})
                    
                if(count==18):
                    tup=(i, j)
                    green_root.update({(45):tup})
                    yellow_root.update({(32):tup}) 
                    red_root.update({(19):tup})
                    blue_root.update({(6):tup})
                
                    
                 # root provide code end
                if(count%3==0):
                    j-=67
                    i=x+box-0.5
                else:
                    i=i+67
                 
                count+=1

            y = y + height - box
            #root block make end
            

        else:
            tamp_root=blue_root

            #root block make start
            count=1
            i=x+box*2.5-67-0.5
            j=y+box+134-0.5
            while(count!=19):
                
                # root provide code start
                if(count==1):
                    tup=(i, j)
                    
                    green_root.update({(39):tup})
                    yellow_root.update({(26):tup})
                    red_root.update({(13):tup})
                     
                if(count==2):
                    tup=(i, j)
                    blue_root.update({(51):tup})
                    green_root.update({(38):tup})
                    yellow_root.update({(25):tup}) 
                    red_root.update({(12):tup})
                
                if(count==3):
                    tup=(i, j)
                    blue_root.update({(50):tup})
                    green_root.update({(37):tup}) 
                    yellow_root.update({(24):tup})
                    red_root.update({(11):tup})
                if(count==4):
                    tup=(i, j)
                    blue_root.update({(1):tup})
                    green_root.update({(40):tup})
                    yellow_root.update({(27):tup})
                    red_root.update({(14):tup})
                     
                if(count==5):
                    tup=(i, j)
                    blue_root.update({(52):tup})
                if(count==6):
                    tup=(i, j)
                    blue_root.update({(49):tup})
                    green_root.update({(36):tup}) 
                    yellow_root.update({(23):tup})
                    red_root.update({(10):tup})
                
                if(count==7):
                    tup=(i, j)
                    blue_root.update({(2):tup})
                    green_root.update({(41):tup})
                    yellow_root.update({(28):tup})
                    red_root.update({(15):tup})
                     
                if(count==8):
                    tup=(i, j)
                    blue_root.update({(53):tup})
                if(count==9):
                    tup=(i, j)
                    blue_root.update({(48):tup})
                    green_root.update({(35):tup}) 
                    yellow_root.update({(22):tup})
                    red_root.update({(9):tup})
                if(count==10):
                    tup=(i, j)
                    blue_root.update({(3):tup})
                    green_root.update({(42):tup})
                    yellow_root.update({(29):tup})
                    red_root.update({(16):tup})
                     
                if(count==11):
                    tup=(i, j)
                    blue_root.update({(54):tup})
                if(count==12):
                    tup=(i, j)
                    blue_root.update({(47):tup})
                    green_root.update({(34):tup}) 
                    yellow_root.update({(21):tup})
                    red_root.update({(8):tup})
                if(count==13):
                    tup=(i, j)
                    blue_root.update({(4):tup})
                    green_root.update({(43):tup})
                    yellow_root.update({(30):tup}) 
                    red_root.update({(17):tup})
                     
                if(count==14):
                    tup=(i, j)
                    blue_root.update({(55):tup}) 
                if(count==15):
                    tup=(i, j)
                    blue_root.update({(46):tup})
                    green_root.update({(33):tup}) 
                    yellow_root.update({(20):tup})
                    red_root.update({(7):tup})
                if(count==16):
                    tup=(i, j)
                    blue_root.update({(5):tup})
                    green_root.update({(44):tup})
                    yellow_root.update({(31):tup})
                    red_root.update({(18):tup})
                if(count==17):
                    tup=(i, j)
                    blue_root.update({(56):tup})
                    tup=(i-67, j)
                    blue_root.update({(57):tup})
                if(count==18):
                    tup=(i, j)
                    blue_root.update({(45):tup})
                    green_root.update({(32):tup}) 
                    yellow_root.update({(19):tup})
                    red_root.update({(6):tup})
                
                
                # root provide code end
                if(count%3==0):
                    i-=67
                    j=y+box+134-0.5
                else:
                    j=j-67
                count+=1

            x = x + wight - box
            y = y + height - box
            #root block make end
            
        box=box-67*2
        x=x+(67)
        y=y+(67)
        
        
        curcle_x=x+box/4
        curcle_y=y+box/4
        tamp_root[0].update({'a':(curcle_x-35,curcle_y-35)})
        
        
        curcle_x=x+box/2+(box/2)/2
        curcle_y=y+box/4
        tamp_root[0].update({'b':(curcle_x-35,curcle_y-35)})
        
        
        curcle_x=x+box/4
        curcle_y=y+box/2+(box/2)/2
        tamp_root[0].update({'c':(curcle_x-35,curcle_y-35)}) 
     
        
        curcle_x=x+box/2+(box/2)/2
        curcle_y=y+box/2+(box/2)/2
        tamp_root[0].update({'d':(curcle_x-35,curcle_y-35)})   
        return 0

    fun(x,y,1)
    fun(x,y,2)
    fun(x,y,3)
    fun(x,y,4)
    return 0
        
#root function end   
    
    

def ludo_bord():
    gamewindow.fill(white)
    global flage
    
    global x, y
    x=sift_x
    y=sift_y
    pygame.draw.rect(gamewindow, black, [x, y, bord_width,bord_height])
    x=x+(15/2)
    y=y+(15/2)
    wight=bord_width-15
    height=bord_height-15

    pygame.draw.rect(gamewindow, light, [x, y, wight, height])

    def fun(colour,x,y,count):

        box=(wight/5)*2
        if(count==1):
            tamp_root=yellow_root
            #root block make start
            count=1
            i=x-0.5
            j=y+box-0.5
            while(count!=19):
                tampcolour=light
                
                if(count==4 or count==5 or count==8 or count==11 or count==14 or count==17):
                    tampcolour=colour
                pygame.draw.rect(gamewindow,black,(i,j,67,67))
                pygame.draw.rect(gamewindow,tampcolour,(i+0.5,j+0.5,66,66))
                
                
                
                if(count%3==0):
                    i+=67
                    j=y+box-0.5
                else:
                    j=j+67
                    
                if(count==4):
                    pygame.draw.circle(gamewindow, l_black, (i+33, j-33), 20)
                
                if(count==9):
                    pygame.draw.circle(gamewindow, l_black, (i-34, j+166), 20)
                    
                 
                    
                
                
                count+=1
                
            pygame.draw.polygon(gamewindow,black,((x+502.5,y+502.5),(x+402,y+603),(x+402,y+402)))
            pygame.draw.polygon(gamewindow,yellow,((x+502.5-0.5,y+502.5-0.5),(x+402,y+603),(x+402,y+402+0.5)))
            #root block make end
        elif(count==2):
            tamp_root=red_root

            
            #root block make start
            count=1
            i=x+box-0.5
            j=y-0.5
            #var=45
            while(count!=19):
                
                tampcolour=light
                if(count==5 or count==6 or count==8 or count==11 or count==14 or count==17):
                    tampcolour=colour
                pygame.draw.rect(gamewindow,black,(i,j,67,67))
                pygame.draw.rect(gamewindow,tampcolour,(i+0.5,j+0.5,66,66))
                if(count%3==0):
                    j+=67
                    i=x+box-0.5
                else:
                    i=i+67
                    
                if(count==6):
                    pygame.draw.circle(gamewindow, l_black, (i+167, j-33), 20)
                
                if(count==9):
                    pygame.draw.circle(gamewindow, l_black, (i+34, j-33), 20)
                count+=1
                
            pygame.draw.polygon(gamewindow,black,((x+502.5,y+502.5),(x+603,y+402),(x+402,y+402)))
            pygame.draw.polygon(gamewindow,red,((x+502.5,y+502.5-2),(x+603-0.5,y+402),(x+402+2,y+402)))
             
            x = x + wight - box
            #root block make end
        elif(count==3):
            tamp_root=green_root

            #root block make start
            count=1
            i=x+box-0.5
            j=y+box*2.5-67-0.5
            while(count!=19):
                tampcolour=light
                if(count==4 or count==5 or count==8 or count==11 or count==14 or count==17):
                    tampcolour=colour
                pygame.draw.rect(gamewindow,black,(i,j,67,67))
                pygame.draw.rect(gamewindow,tampcolour,(i+0.5,j+0.5,66,66))
                if(count%3==0):
                    j-=67
                    i=x+box-0.5
                else:
                    i=i+67
                    
                if(count==4):
                    pygame.draw.circle(gamewindow, l_black, (i-33, j+33), 20)
                
                if(count==9):
                    pygame.draw.circle(gamewindow, l_black, (i+167, j+100), 20)
                    
                count+=1
                
            pygame.draw.polygon(gamewindow,black,((x+502.5,y+502.5),(x+603,y+603),(x+402,y+603)))
            pygame.draw.polygon(gamewindow,green,((x+502.5,y+502.5+0.5),(x+603,y+603-1),(x+402+3.5,y+603-1)))

            y = y + height - box
            #root block make end
            

        else:
            tamp_root=blue_root

            #root block make start
            count=1
            i=x+box*2.5-67-0.5
            j=y+box-0.5
            while(count!=19):
                tampcolour=light
                if(count==5 or count==6 or count==8 or count==11 or count==14 or count==17):
                    tampcolour=colour
                pygame.draw.rect(gamewindow,black,(i,j,67,67))
                pygame.draw.rect(gamewindow,tampcolour,(i+0.5,j+0.5,66,66))
                if(count%3==0):
                    i-=67
                    j=y+box-0.5
                else:
                    j=j+67
                    
                if(count==6):
                    pygame.draw.circle(gamewindow, l_black, (i+100, j+167), 20)
                
                if(count==9):
                    pygame.draw.circle(gamewindow, l_black, (i+100, j+33), 20)
                
                count+=1
                
            pygame.draw.polygon(gamewindow,black,((x+502.5,y+502.5),(x+603,y+603),(x+603,y+400)))
            pygame.draw.polygon(gamewindow,blue,((x+502.5+2.5,y+502.5-0.5),(x+603-1.5,y+603-3.5),(x+603-1.5,y+400+3)))


            x = x + wight - box
            y = y + height - box
            
            #root block make end
            
        pygame.draw.rect(gamewindow, black, [x, y, box,box])
        pygame.draw.rect(gamewindow, colour, [x-0.5, y-0.5, box-1,box-1])
        box=box-67*2
        x=x+(67)
        y=y+(67)
        pygame.draw.rect(gamewindow, (255, 255, 255), [x, y, box,box])
        
        curcle_x=x+box/4
        curcle_y=y+box/4
        a = pygame.draw.circle(gamewindow, colour, (curcle_x, curcle_y), 34)
        
        curcle_x=x+box/2+(box/2)/2
        curcle_y=y+box/4
        b = pygame.draw.circle(gamewindow, colour, (curcle_x,curcle_y ), 34)
        
        curcle_x=x+box/4
        curcle_y=y+box/2+(box/2)/2
        c = pygame.draw.circle(gamewindow, colour, (curcle_x,curcle_y ), 34)
        
        curcle_x=x+box/2+(box/2)/2
        curcle_y=y+box/2+(box/2)/2
        d = pygame.draw.circle(gamewindow, colour, (curcle_x, curcle_y), 34)
        
        
        return 0

    fun(yellow,x,y,1)
    fun(red,x,y,2)
    fun(green,x,y,3)
    fun(blue,x,y,4)
    if (flage==1):
        root()
    flage=0
    return 0
#ludo game function end 
     
     
     
def goti_display(name):
    
    
    
    
    #str=(name.split("_"))
    #red block
    
    if name=="red_a":
            global red_goti_a_image, red_a_goti_rect
            size=red_a_size
            
            
            red_goti_a_image=pygame.transform.scale(location_red, (size, size))
            #red_goti_a_image=pygame.transform.rotate(location_red,180)
            red_a_goti_rect=red_goti_a_image.get_rect()
            red_a_goti_rect.x=image_pogition_set(name)[0]
            red_a_goti_rect.y=image_pogition_set(name)[1]
            image=red_goti_a_image
            

    elif name=="red_b":
            global red_goti_b_image, red_b_goti_rect
            size=red_b_size
            
                
            red_goti_b_image=pygame.transform.scale(location_red, (size, size))
            red_b_goti_rect=red_goti_b_image.get_rect()
            red_b_goti_rect.x=image_pogition_set(name)[0]
            red_b_goti_rect.y=image_pogition_set(name)[1]
            image=red_goti_b_image
            
    elif name=="red_c":
            global red_goti_c_image, red_c_goti_rect
            size=red_c_size
            if(red_c_current==0):
                tup=red_root[0]['c']
            else:
                tup=red_root[red_c_current]
                
            red_goti_c_image=pygame.transform.scale(location_red, (size, size))
            red_c_goti_rect=red_goti_c_image.get_rect()
            red_c_goti_rect.x=image_pogition_set(name)[0]
            red_c_goti_rect.y=image_pogition_set(name)[1]
            image=red_goti_c_image
            
    elif name=="red_d":
            global red_goti_d_image, red_d_goti_rect
            size=red_d_size
            if(red_d_current==0):
                tup=red_root[0]['d']
            else:
                tup=red_root[red_d_current]
                
            red_goti_d_image=pygame.transform.scale(location_red, (size, size))
            red_d_goti_rect=red_goti_d_image.get_rect()
            red_d_goti_rect.x=image_pogition_set(name)[0]
            red_d_goti_rect.y=image_pogition_set(name)[1]
            image=red_goti_d_image
            
    #red block end
    
    #green block
    elif name=="green_a":
        global green_goti_a_image, green_a_goti_rect
        size=green_a_size
        if(green_a_current==0):
                tup=green_root[0]['a']
        else:
                tup=green_root[green_a_current]
                
        green_goti_a_image=pygame.transform.scale(location_green, (size, size))
        green_a_goti_rect=green_goti_a_image.get_rect()
        green_a_goti_rect.x=image_pogition_set(name)[0]
        green_a_goti_rect.y=image_pogition_set(name)[1]
        image=green_goti_a_image
        
        
    elif name=="green_b":
        global green_goti_b_image, green_b_goti_rect
        size=green_b_size
        if(green_b_current==0):
                tup=green_root[0]['b']
        else:
                tup=green_root[green_b_current]
                
        green_goti_b_image=pygame.transform.scale(location_green, (size, size))
        green_b_goti_rect=green_goti_b_image.get_rect()
        green_b_goti_rect.x=image_pogition_set(name)[0]
        green_b_goti_rect.y=image_pogition_set(name)[1]
        image=green_goti_b_image
        
    elif name=="green_c":
        global green_goti_c_image, green_c_goti_rect
        size=green_c_size
        if(green_c_current==0):
                tup=green_root[0]['c']
        else:
                tup=green_root[green_c_current]
                
        green_goti_c_image=pygame.transform.scale(location_green, (size, size))
        green_c_goti_rect=green_goti_c_image.get_rect()
        green_c_goti_rect.x=image_pogition_set(name)[0]
        green_c_goti_rect.y=image_pogition_set(name)[1]
        image=green_goti_c_image
        
    elif name=="green_d":
        global green_goti_d_image, green_d_goti_rect
        size=green_d_size
        if(green_d_current==0):
                tup=green_root[0]['d']
        else:
                tup=green_root[green_d_current]
                
        green_goti_d_image=pygame.transform.scale(location_green, (size, size))
        green_d_goti_rect=green_goti_d_image.get_rect()
        green_d_goti_rect.x=image_pogition_set(name)[0]
        green_d_goti_rect.y=image_pogition_set(name)[1]
        image=green_goti_d_image
    #green block end
        
            
    gamewindow.blit(image,image_pogition_set(name))
    
    
    return 0
    
 
 
def goti_run(name,stape):
    global dice_run, dice_number
    
    global green_a_position, green_b_position, green_c_position, green_d_position, red_a_position, red_b_position, red_c_position, red_d_position
     
    global green_a_size, green_b_size, green_c_size, green_d_size, red_a_size, red_b_size, red_c_size, red_d_size
    
    
        
    while(stape!=0):
        ludo_bord()
        dice()
        pygame.mixer.music.load("Goti_run_sound.mp3")
        pygame.mixer.music.play()
        
        if(name!="red_a"):
            goti_display("red_a")
        if(name!="red_b"):
            goti_display("red_b")
        if(name!="red_c"):
            goti_display("red_c")
        if(name!="red_d"):
            goti_display("red_d")
            
        if(name!="green_a"):
            goti_display("green_a")
        if(name!="green_b"):
            goti_display("green_b")
        if(name!="green_c"):
            goti_display("green_c")
        if(name!="green_d"):
            goti_display("green_d")
        
        
        
        
        if(name=="red_a"):
            red_a_position='c'
            red_a_size=size1
            global red_a_current
            if(red_a_current==0):
                stape=1
            red_a_current+=1
            
        if(name=="red_b"):
            red_b_position='c'
            red_a_size=size1
            global red_b_current
            if(red_b_current==0):
                stape=1
            red_b_current+=1
            
        if(name=="red_c"):
           red_c_position='c'
           red_c_size=size1
           global red_c_current
           if(red_c_current==0):
                stape=1
           red_c_current+=1
           
        if(name=="red_d"):
            red_d_position='c'
            red_d_size=size1
            global red_d_current
            if(red_d_current==0):
                stape=1
            red_d_current+=1
            
        if(name=="green_a"):
           green_a_position='c'
           green_a_size=size1
           global green_a_current
           if(green_a_current==0):
                stape=1
           green_a_current+=1
           
        if(name=="green_b"):
           green_b_position='c'
           green_b_size=size1
           global green_b_current
           if(green_b_current==0):
                stape=1
           green_b_current+=1
           
        if(name=="green_c"):
           global green_c_current
           green_c_position='c'
           green_c_size=size1
           if(green_c_current==0):
                stape=1
           green_c_current+=1
           
        if(name=="green_d"):
            green_d_position='c'
            green_d_size=size1
            global green_d_current
            if(green_d_current==0):
                stape=1
            green_d_current+=1
            
        goti_display(name)
        pygame.display.update()
        stape-=1
        
        
        
        clock.tick(4)
    
    
    dice_run=False
    #dice_number=0
    
    
    return 0

       
       
       
# green acctivation button
green_rect=pygame.draw.rect(gamewindow,black, [30,1830, 1020,339])
# green acctivation button
     
     
# red acctivation button
red_rect=pygame.draw.rect(gamewindow,black, [30,5, 1020,339])
# red acctivation button
     



#game loop start   
#green_flage=True

while not gameover:    
    
    
        
    if(winner=='0'):
        ludo_bord()
        root()
        dice()
        logic()
    
    if (red_flage==True):
        goti_display("green_a")
        goti_display("green_b")
        goti_display("green_c")
        goti_display("green_d")
        
        goti_display("red_a")
        goti_display("red_b")
        goti_display("red_c")
        goti_display("red_d")
        
        
        
    if(green_flage==True):
        goti_display("red_a")
        goti_display("red_b")
        goti_display("red_c")
        goti_display("red_d")
        
        goti_display("green_a")
        goti_display("green_b")
        goti_display("green_c")
        goti_display("green_d")  
    
    
    if(winner !="0"):
        #red_flage=False
#        green_flage=False
        gamewindow.fill(white)
        pygame.display.update()
        display_winner_name(winner,red,70,950)
        
  
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
                    
                    if(red_flage==True and dice_run==True):
                        
                        if (red_a_signal==True and (red_a_goti_rect).collidepoint(i.pos)):
                            goti_run("red_a",dice_number)
                            goti_maar(1)
              
                            
                        elif (red_b_signal==True and (red_b_goti_rect).collidepoint(i.pos)):
                            goti_run("red_b",dice_number)
                            goti_maar(1)
                            
                                                  
                        elif (red_c_signal==True and (red_c_goti_rect).collidepoint(i.pos)):
                            goti_run("red_c",dice_number)
                            goti_maar(1)
                          
                         
                        elif (red_d_signal==True and (red_d_goti_rect).collidepoint(i.pos)):
                            goti_run("red_d",dice_number)
                            goti_maar(1)
                          
                        
                            
                        
                            
                            
                    if(green_flage==True and dice_run==True):
                        
                        if (green_a_signal==True and (green_a_goti_rect).collidepoint(i.pos)):
                            goti_run("green_a",dice_number)
                            goti_maar(2)
                            
                            
                        elif (green_b_signal==True and (green_b_goti_rect).collidepoint(i.pos)):
                            goti_run("green_b",dice_number)
                            goti_maar(2)
                            
                                                       
                        elif (green_c_signal==True and (green_c_goti_rect).collidepoint(i.pos)):
                            goti_run("green_c",dice_number)
                            goti_maar(2)
                            
                                                       
                        elif (green_d_signal==True and (green_d_goti_rect).collidepoint(i.pos)):
                            goti_run("green_d",dice_number)
                            goti_maar(2)
                           
                           
                               
                    if(green_flage==True and dice_run==False and green_cheat==1 ):
                        if (rect6).collidepoint(i.pos):
                            fack_dice_number=6
                        elif (rect5).collidepoint(i.pos):
                            fack_dice_number=5
                        elif (rect4).collidepoint(i.pos):
                            fack_dice_number=4
                        elif (rect3).collidepoint(i.pos):
                            fack_dice_number=3
                        elif (rect2).collidepoint(i.pos):
                            fack_dice_number=2
                        elif (rect1).collidepoint(i.pos):
                            fack_dice_number=1
                            
                    if(red_flage==True and dice_run==False and red_cheat==1):
                        if (rec6).collidepoint(i.pos):
                            fack_dice_number=1
                        elif (rec5).collidepoint(i.pos):
                            fack_dice_number=2
                        elif (rec4).collidepoint(i.pos):
                            fack_dice_number=3
                        elif (rec3).collidepoint(i.pos):
                            fack_dice_number=4
                        elif (rec2).collidepoint(i.pos):
                            fack_dice_number=5
                        elif (rec1).collidepoint(i.pos):
                            fack_dice_number=6
                       
                      
                    
                    if (green_rect).collidepoint(i.pos) or (red_rect).collidepoint(i.pos):
                        if timer == 0:
                            # First mouse click
                            timer = 0.001  # Start the timer
                        # Click again before 0.5 seconds to double click.
                        elif timer < 0.5:
                            if(green_rect).collidepoint(i.pos):
                                if(green_cheat==1):
                                    green_cheat=0
                                else:
                                    green_cheat=1
                                    red_cheat=0
                            else:
                                 if(red_cheat==1):
                                    red_cheat=0
                                 else:
                                    red_cheat=1
                                    green_cheat=0
                                 
                            
                                
                            
                            timer = 0

        
                        
                        
                    if(dice_run==False):
                            
                            if(red_flage==True):
                                if (red_dice_rect).collidepoint(i.pos):
                                    dice_run=True
                                    dice()
                            if(green_flage==True):
                                if (green_dice_rect).collidepoint(i.pos):
                                    dice_run=True
                                    dice()
                                    
                                                  
                        
    # Increase timer after mouse was pressed the first time.
    if timer != 0:
            timer += 0.1
            time.sleep(0.1)
            # Reset after 0.5 seconds.
            if timer >= 0.5:
                print('too late')
                timer = 0     
    
    
    
    pygame.display.update()
    
#game loop end
