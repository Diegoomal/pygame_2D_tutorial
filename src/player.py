import pygame

from configs import SCREEN_WIDTH, MAP_COLLISION_LAYER
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        #Load the spritesheet of frames for this player
        self.sprites = SpriteSheet("resources/player.png", (30, 42))
    
        self.stillRight = self.sprites.image_at(0, 0)
        self.stillLeft = self.sprites.image_at(0, 1)
        
        #List of frames for each animation
        self.runningRight = [self.sprites.image_at(i, 2) for i in range(5)]
        self.runningLeft =  [self.sprites.image_at(i, 3) for i in range(5)]
        self.jumpingRight = [self.sprites.image_at(i, 0) for i in (1, 2, 3)]
        self.jumpingLeft  = [self.sprites.image_at(i, 1) for i in (1, 2, 3)]

        self.image = self.stillRight
        
        #Set player position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        #Set speed and direction
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
        #Boolean to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()
        
        #Players current level, set after object initialized in game constructor
        self.currentLevel = None

    def do_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = "left"
                self.running = True
                self.changeX = -3
            elif event.key == pygame.K_RIGHT:
                self.direction = "right"
                self.running = True
                self.changeX = 3
            elif event.key == pygame.K_UP:
                self.jump()
            elif event.key == pygame.K_SPACE:
                print(self)
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.changeX < 0:
                self.running = False
                self.changeX = 0
            elif event.key == pygame.K_RIGHT and self.changeX > 0:
                self.running = False
                self.changeX = 0
        
    def update(self):
        #Update player position by change
        self.rect.x += self.changeX
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        if len(tileHitList) > 0:
            print(tileHitList)
        
        #Move player to correct side of that block
        for tile in tileHitList:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right
        
        #Move screen if player reaches screen bounds
        if self.rect.right >= SCREEN_WIDTH - 200:
            difference = self.rect.right - (SCREEN_WIDTH - 200)
            self.rect.right = SCREEN_WIDTH - 200
            self.currentLevel.shiftLevel(-difference)
        
        #Move screen is player reaches screen bounds
        if self.rect.left <= 200:
            difference = 200 - self.rect.left
            self.rect.left = 200
            self.currentLevel.shiftLevel(difference)
        
        #Update player position by change
        self.rect.y += self.changeY
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
       
        #If there are tiles in that list
        if len(tileHitList) > 0:
            #Move player to correct side of that tile, update player frame
            for tile in tileHitList:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1
                    
                    if self.direction == "right":
                        self.image = self.stillRight
                    else:
                        self.image = self.stillLeft
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        #If there are not tiles in that list
        else:
            #Update player change for jumping/falling and player frame
            self.changeY += 0.2
            if self.changeY > 0:
                if self.direction == "right":
                    self.image = self.jumpingRight[1]
                else:
                    self.image = self.jumpingLeft[1]
        
        #If player is on ground and running, update running animation
        if self.running and self.changeY == 1:
            if self.direction == "right":
                self.image = self.runningRight[self.runningFrame]
            else:
                self.image = self.runningLeft[self.runningFrame]
        
        #When correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 4:
                self.runningFrame = 0
            else:
                self.runningFrame += 1

    def animate(self):
        t = pygame.time.get_ticks()
        if t - self.t0 > 50:
            self.t0 = t
            self.runningFrame = (self.runningFrame + 1) % 4

            if self.running and self.changeY == 1:
                if self.direction == "right":
                    self.image = self.runningRight[self.runningFrame]
                else:
                    self.image = self.runningLeft[self.runningFrame]

    #Make player jump
    def jump(self):
        #Check if player is on ground
        self.rect.y += 2
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 2
        
        if len(tileHitList) > 0:
            if self.direction == "right":
                self.image = self.jumpingRight[0]
            else:
                self.image = self.jumpingLeft[0]
                
            self.changeY = -6
    
    #Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def __str__(self):
        return f'Player at {self.rect.center} dir:{self.direction}'
