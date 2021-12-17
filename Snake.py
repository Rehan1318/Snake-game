import pygame
import random
import os

pygame.mixer.init()
pygame.init()






x = random.randint(0 ,255)
y = random.randint(0 ,255)
z = random.randint(0 ,255)
a = random.randint(0 ,255)
b = random.randint(0 ,255)
c = random.randint(0 ,255)
ga = random.randint(0 ,255)
gam = random.randint(0 ,255)
game = random.randint(0 ,255)
pl = random.randint(0 ,255)
pla = random.randint(0 ,255)
play = random.randint(0 ,255)


Production = ((a , b ,c))
game_name = ((ga , gam ,game))
Play_Game = ((pl , pla ,play))

white = (255 , 255 ,255)
red = (255,0,0)
black = (0,0,0)
green = (0,128,0)

clock = pygame.time.Clock()



print("1. Slow")
print("2. Normal")
print("3. Fast")


sp = 0
while True:
    try:
        speed = input("Choose your speed from the above: ")
        speed = speed.lower()
        if speed == 'slow':
            sp = sp + 5
            
            break
        elif speed == 'normal':
            sp = sp + 8
            
            break
        elif speed == 'fast':
            sp = sp + 15
            
            break
    except:
        print("Please Write correct spelling!")


blue = (0,0,255)

width = 700
height = 500


gameWindow = pygame.display.set_mode((width , height))

img_path = "image\\backgroundimg.jpg"

bgimg = pygame.image.load(img_path)
bgimg = pygame.transform.scale(bgimg , (700 , 500)) .convert_alpha()




pygame.display.set_caption("Snake(v1.25.0)                                                                                                     Rehan_Productions")
pygame.display.update()


font = pygame.font.SysFont(None , 30)




def plot_snake(gameWindow, color , snake_list , snake_size ):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow , color, [x , y ,snake_size , snake_size])


Music_path = "Music\\game_over.mp3"



def score_(text , color , x , y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x , y))

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((x , y , z))

        score_("Rehan_Production presents" , Production  , 200, 170)
        score_("Snake",game_name , 290 , 210)
        score_("Press space to play" , Play_Game , 225 , 260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    gameloop()

        pygame.display.update()
        clock.tick(30)


            


def gameloop():
    Back_path = "Music\\Background.mp3"
    pygame.mixer.music.load(Back_path)
    pygame.mixer.music.play()
    sc = 0
    if speed == 'slow':
        sc += 3
    elif speed == 'normal':
        sc += 8
    elif speed == 'fast':
        sc += 15

    fps = 30
    score = 0
    exit_game = False
    game_over = False
    snk_l = []
    snake_list = []
    snake_lenght = 1 




    eye_x = 110
    eye_y = 160
    eye_size = 10

    snake_x = 100
    snake_y = 150
    snake_size = 25



    velocity_y = 0
    velocity_x = 0




    food_x = random.randint(40 ,500)
    food_y = random.randint(40 ,400)

    try:
        Hiscore_path = "data\\Hi.txt"
        with open(Hiscore_path , "r") as f:
            Hiscore = f.read()
    except:
        a = open(Hiscore_path , "w")
        a.write("0")
        a.close()



    
    while not exit_game:


        if game_over:
            with open(Hiscore_path , "w") as f:
                f.write(str(Hiscore))
                

            gameWindow.fill(white)
            

            score_("Game Over! Press Enter to Continue" , red , 150 , 200)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:#it will make to recognise what key is pressed on keyboard
                    if event.key == pygame.K_RIGHT:
                        velocity_x = sp
                        velocity_y  = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -sp
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -sp
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = sp
                        velocity_x = 0
                    
                    if event.key == pygame.K_s:
                        score += 1000

                            
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<23 and abs(snake_y - food_y)<23:
                
                    
                food_x = random.randint(40, 500)
                food_y = random.randint(40, 400)
                snake_lenght +=5
                score += 10
                if score>int(Hiscore):
                    Hiscore = score


            gameWindow.fill(white)
            gameWindow.blit(bgimg , (0,0))
            pygame.draw.rect(gameWindow , black, [0, 0 , 700, 35])
            pygame.draw.rect(gameWindow , black, [0, 0 , 35, 500])
            pygame.draw.rect(gameWindow , black, [0, 465 , 700, 35])
            pygame.draw.rect(gameWindow , black, [665, 0 , 35, 500])

            

            score_("Score: "+ str(score) + "                                                                              Hiscore: " + str(Hiscore), green , 5 , 5)
            
            

            

            pygame.draw.rect(gameWindow , red, [snake_x , snake_y , 20 , 20])
            
            pygame.draw.rect(gameWindow, blue, [food_x , food_y , 15 , 15])
            #Syntax = pygame.draw.rect(place , color, [x , y , size , size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_lenght:
                del snake_list[0]
                
           

            if head in snake_list[:-1]:
                
                pygame.mixer.music.load(Music_path)
                pygame.mixer.music.play()               
                game_over = True


                
            
            if snake_x < 35 or snake_x > 630 or snake_y < 35 or snake_y > 430:
                pygame.mixer.music.load(Music_path)
                pygame.mixer.music.play()                
                game_over = True


                
                


            plot_snake(gameWindow , red, snake_list , snake_size )

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()

    


    
