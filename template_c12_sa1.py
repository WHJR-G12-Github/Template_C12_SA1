# Importing 'random'
import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
# Inverting the pipe image and loading it into the 'images' dictionary
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
groundx=0
speed=0
class Bird:
    bird=pygame.Rect(100,250,30,30)
    
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    # The following line is commented as it is no longer required
    #bpipe=pygame.Rect(250,400,40,320)
    
    # Defining the constructor __init__()
    def __init__(self,x):
        self.height=random.randint(150,400)
        self.tpipe=pygame.Rect(x,self.height-400,40,400)
        self.bpipe=pygame.Rect(x,self.height+150,40,400)
        
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
      
    # Define a method named 'move()'
    
        # Decrement the value of 'self.tpipe.x'
        
        # Decrement the value of 'self.bpipe.x'
        
bird1=Bird()
# Creating an object 'pipe1' for the 'Pipe' class by passing x-coordinate value as the argument
pipe1=Pipe(150)
while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  
  # Call the method 'move()' using the 'pipe1' object
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
