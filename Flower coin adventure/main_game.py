import random
import pygame

pygame.init()
pygame.mixer.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lavaris")

# Images
background = pygame.image.load("assets/background.jpg")
player = pygame.image.load("assets/gp2.png")
coin = pygame.image.load("assets/coins2.png")
monster = pygame.image.load("assets/enemy1.png")
play_button = pygame.image.load("assets/play2.png")
game_bg = pygame.image.load("assets/images.jpg")
pygame.mixer.music.load("assets/background.mp3")
pygame.mixer.music.set_volume(0.5)

# Resize Images
background = pygame.transform.scale(background, (800, 600))
player = pygame.transform.scale(player, (160, 230))
coin = pygame.transform.scale(coin, (50, 50))
monster = pygame.transform.scale(monster, (150, 150))
play_button = pygame.transform.scale(play_button, (250, 100))
game_bg = pygame.transform.scale(game_bg, (800, 600))

# Font
title_font = pygame.font.SysFont("Georgia", 45, bold=True)

# Player Position
player_x = 100
player_y = 500

# Play Button Position
play_x = 275
play_y = 250

# Game State
game_state = "menu"

running = True
clock = pygame.time.Clock()

# Player physics
player_speed = 5
velocity_y = 0
gravity = 0.6
jump_speed = -22

# Ground level
ground = 270
on_ground = True

# Monster Position
monster_x = 900
monster_y = 350
monster_speed = 3

# Collision rectangles
player_rect = pygame.Rect(player_x + 30, player_y + 50, 70, 120)
monster_rect = pygame.Rect(monster_x, monster_y, 100, 100)
coin_rect = coin.get_rect()

jump_count = 0

score = 0
score_font = pygame.font.SysFont("Trebuchet MS", 35, bold=True)
with open("highscore.txt", "r") as file:
    highscore = int(file.read())

coin_x = random.randint(250, 700)
coin_y = random.randint(150, 350)

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if game_state == "gameover":

               if event.key == pygame.K_r:

                  # Reset player
                  player_x = 100
                  player_y = 500
                  velocity_y = 0
                  on_ground = True
                  jump_count = 0

                  # Reset monster
                  monster_x = 900

                  # Reset coin
                  coin_x = 500
                  coin_y = 300

                  # Reset score
                  score = 0
                  

                  # Start game again
                  game_state = "playing"

                  pygame.mixer.music.play(-1)

        if event.type == pygame.QUIT:
            running = False

        # Clicking Play Button
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if game_state == "menu":

                if (play_x <= mouse_x <= play_x + 250) and (play_y <= mouse_y <= play_y + 100):
                    game_state = "playing"

        # Pause / Resume
        if event.type == pygame.KEYDOWN:

           if event.key == pygame.K_p:

               if game_state == "playing":
                    game_state = "paused"

               elif game_state == "paused":
                   game_state = "playing"            

    # ---------------- MENU ----------------

    if game_state == "menu":

        screen.blit(background, (0, 0))

        title = title_font.render("Lavaris", True, (0, 51, 153))
        title_rect = title.get_rect(center=(400, 90))

        screen.blit(title, title_rect)
        screen.blit(play_button, (play_x, play_y))

    # ---------------- GAME ----------------

    elif game_state == "playing":

        

         # keyboard
        keys = pygame.key.get_pressed()   

        # left right movement
        if keys[pygame.K_LEFT]:
          player_x -= player_speed

        if keys[pygame.K_RIGHT]:
          player_x += player_speed

         # jump
        if keys[pygame.K_UP] and on_ground:
          velocity_y = jump_speed
          jump_count += 1
          on_ground = False

         # gravity
        velocity_y += gravity
        player_y += velocity_y

         # landing
        if player_y >= ground:
          player_y = ground
          velocity_y = 0
          on_ground = True
          jump_count = 0

        # monster movement
        
        monster_x -= monster_speed

        if monster_x < -150:
          monster_x = 800

        # Update collision positions
        player_rect.topleft = (player_x + 30, player_y + 50)
        monster_rect.topleft = (monster_x + 20, monster_y + 20)
        coin_rect.topleft = (coin_x, coin_y) 

        # Monster collision
        if player_rect.colliderect(monster_rect):


            print("Game Over!")

            game_state = "gameover"

        # Coin collision
        if player_rect.colliderect(coin_rect):

         score += 1
         if score > highscore:
             highscore = score

             with open("highscore.txt", "w") as file:
                 file.write(str(highscore))

         coin_x = random.randint(250, 750)
         coin_y = random.randint(150, 350)    

        # draw everything
        screen.blit(game_bg, (0, 0))

        screen.blit(player, (player_x, player_y))

        screen.blit(coin, (coin_x, coin_y))

        screen.blit(monster, (monster_x, monster_y))


        score_text = score_font.render(f"Coins: {score}", True, (255, 255, 255))
        highscore_text = score_font.render(
            f"High Score: {highscore}",
            True,
            (255, 255, 255)
        )    


        screen.blit(highscore_text, (20, 60))
        screen.blit(score_text, (20, 20))

    elif game_state == "paused":

       # Draw the game as it was
         screen.blit(game_bg, (0, 0))
         screen.blit(player, (player_x, player_y))
         screen.blit(monster, (monster_x, monster_y))
         screen.blit(coin, (coin_x, coin_y))

        # Draw score
         score_text = score_font.render(f"Coins: {score}", True, (255, 255, 255))
         screen.blit(score_text, (20, 20))

         highscore_text = score_font.render(f"High Score: {highscore}", True, (255, 255, 255))
         screen.blit(highscore_text, (20, 60))

         # Pause message
           # Sky blue box
         pygame.draw.rect(screen, (135, 206, 235), (200, 210, 400, 130), border_radius=20)

           # White border
         pygame.draw.rect(screen, (255, 255, 255), (200, 210, 400, 130), 4, border_radius=20)

           # Smaller fonts
         pause_font = pygame.font.SysFont("Georgia", 32, bold=True)
         resume_font = pygame.font.SysFont("Georgia", 22, bold=True)

           # Pause title
         pause_text = title_font.render("GAME PAUSED", True, (255, 255, 255))
         pause_rect = pause_text.get_rect(center=(400, 245))
         screen.blit(pause_text, pause_rect)

           # Resume text
         resume_text = score_font.render("Press P to Resume", True, (255, 255, 255))
         resume_rect = resume_text.get_rect(center=(400, 290))
         screen.blit(resume_text, resume_rect)


    elif game_state == "gameover":

         pygame.mixer.music.stop()

         screen.fill((0, 0, 0))

         game_over_text = title_font.render(
        "Monster caught you!",
         True,
        (255, 255, 255)
    )

         screen.blit(
               game_over_text,
               (150, 250)
    )      
         restart_text = pygame.font.SysFont("Trebuchet MS", 30).render(
             "Press R to Play Again",
              True,
              (255, 20, 147)
        )

         screen.blit(restart_text, (230, 320))  

    pygame.display.update()
    clock.tick(60)

pygame.quit()