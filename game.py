import pygame 
import sys
import random
import time 

pygame.init()

clock = pygame.time.Clock()

myfnt= pygame.font.SysFont("monospace",30)
myfnt2= pygame.font.SysFont("monospace",30)
score=0

screen_width = 800
screen_height = 600
player_color = (255,0,0)
score_color= (255,255,255)
bgcolor = (0,0,0)
square_dimension = 50
player_pos = [375,525]  

min_speed = 5
max_speed = 8

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dodge")

gameover= False
xp = player_pos[0]
enemy_color = (0,255,0)
enemy_pos1 = [random.randint(0,screen_width-square_dimension),0]

enemy_list=[enemy_pos1]

def drop_enemy(enemy_list):
    delay = random.random()
    if len(enemy_list)<=10 and delay<0.1:
        ene=[random.randint(0,screen_width-square_dimension),0]
        enemy_list.append(ene)

def put_enemy(enemy_list,score,min_speed,max_speed) :
    for enemy_pos in enemy_list :
        score = set_speed(enemy_pos,score,min_speed,max_speed)
        pygame.draw.rect(screen,enemy_color,(enemy_pos[0],enemy_pos[1],square_dimension,square_dimension))
    return score

def set_speed(enemy_pos,score,min_speed,max_speed):
    if enemy_pos[1]>=0 and enemy_pos[1] <screen_height-square_dimension :
        new_min_speed = min_speed+0.01*score
        new_max_speed = max_speed+0.1*score
        enemy_pos[1]+=random.uniform(min_speed,new_max_speed)
    else :
        enemy_pos[0]= random.randint(0,screen_width-square_dimension)
        enemy_pos[1]=0
        score+=1
    return score
def collision(pla,ene):
    if ene[1] >= pla[1]-square_dimension and ene[1]<=pla[1]+square_dimension :
        if ene[0] >= pla[0]-square_dimension and ene[0]<=pla[0]+square_dimension :
            return True
        else :
            return False
    else :
        return False

while not gameover :
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            pygame.display.quit()
            try :
                sys.exit()
            except :
                pass
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key ==  pygame.K_a and xp>=0 :
                    xp-= square_dimension
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and xp <=600 :
                    xp+= square_dimension

    try :
        screen.fill(bgcolor)
    except :
        pass
    
    drop_enemy(enemy_list)
    score = put_enemy(enemy_list,score,min_speed,max_speed)

    text = "Score : " + str(score)
    lable = myfnt.render(text,1,score_color)
    screen.blit(lable,(screen_width-200,screen_height-40))

    pla = [xp,player_pos[1]]
    for ene in enemy_list:
        if collision(pla,ene) :
            gameover = True

    if gameover == True :
        txt = "Game over ... Final "+text    
        lable = myfnt2.render(txt,5,score_color)
        screen.blit(lable,(100,screen_height/2))    

    pygame.draw.rect(screen,player_color,(xp,player_pos[1],square_dimension,square_dimension))
    
    clock.tick(30)
    pygame.display.update()
    if gameover == True :
        time.sleep(2)