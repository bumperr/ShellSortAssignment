import pygame 
import random
import math
import time
pygame.init()
pygame.display.init()

#-----------------Global constant-----------------------------

#-------------------SHELL SORT-----------------------------------------
def shell_sort(gameInfo,lst):
    n=len(lst)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):

            j = i
           
            
            
            while j >= interval and lst[j - interval] > lst[j]:
                draw_list(gameInfo,{i:gameInfo.BLUE,j:gameInfo.RED , j-interval: gameInfo.GREEN},True)
                time.sleep(0.2)
                
                #swap
                lst[j],lst[j - interval] = lst[j - interval],lst[j]
                draw_list(gameInfo,{i:gameInfo.BLUE,j:gameInfo.GREEN , j-interval: gameInfo.RED},True)
                time.sleep(0.2)
               
                j -= interval


        interval //= 2

    

    return lst

#---------------------PYGAME SETUP ---------------------------------------------
class gameInfo:

    WHITE= 254, 249, 239
    YELLOW= 255, 203, 119
    RED= 254, 109, 115
    GREEN= 23, 195, 178
    BLUE= 34, 124, 157
    BLACK=41, 31, 30
    BACKGROUND=WHITE
    SIDE_PADDING = 100
    TOP_PADDING = 150
    
    FONT = pygame.font.Font('ZilapGeometrik.ttf', 80)

    def __init__(self,width,height,lst):
        self.width=width
        self.height=height
        
        self.window=pygame.display.set_mode((width,height))
        pygame.display.set_caption("Shell sort Animation")

        self.list_setup(lst)

    def list_setup(self,lst):
        self.lst=lst
        self.minVal=min(lst)
        self.maxVal=max(lst)

        self.block_width=round((self.width-self.SIDE_PADDING)/len(lst))
        self.block_height=math.floor((self.height-self.TOP_PADDING)/(self.maxVal-self.minVal))

        self.start_coordinate=self.SIDE_PADDING//2

def draw(gameInfo):

    gameInfo.window.fill(gameInfo.BACKGROUND)
    title=gameInfo.FONT.render(f"Shell sort simulation",1,gameInfo.BLACK)
    gameInfo.window.blit(title,(gameInfo.width/2 - title.get_width()/2,5))
        
    draw_list(gameInfo)
    
    pygame.display.update()

def draw_list(gameInfo,coloration={}, clear_bg=False):
    array=gameInfo.lst
    
    if clear_bg:
        draw(gameInfo)
                
    for i, val in enumerate(array):
        x=gameInfo.start_coordinate + i*gameInfo.block_width
        y=gameInfo.height - (val-gameInfo.minVal) *gameInfo.block_height

        
        #actually draw

        if i in coloration:
            color = coloration[i] 
        else:
            color=get_colour_thickness(val,gameInfo.minVal,gameInfo.maxVal)


        pygame.draw.rect(gameInfo.window,color,(x,y-20,gameInfo.block_width,gameInfo.height))


        if clear_bg:
            pygame.display.update()


def generateList(n,min,max):
    lst=[]

    for i in range(n):
        val=random.randint(min,max)
        lst.append(val)
    return lst

def get_colour_thickness(value, min_value, max_value):
   
    value = max(min(value, max_value), min_value)
    
    # Calculate the thickness based on the value
    range_value = max_value - min_value
    thickness = 200 - int((value - min_value) / range_value * 200)
    
    return thickness,thickness,thickness





#---------------pygame main event loop
def main():
    pygame.display.init()
    running=True
    clock=pygame.time.Clock()

    numOfBar=10
    minValue=0
    maxValue=100
    
   

    array=generateList(numOfBar,minValue,maxValue)
    
    gameFlow=gameInfo(1920,1000,array)

    while running:
        clock.tick(60)

        pygame.display.update()

        draw(gameFlow)

      
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    array=generateList(numOfBar,minValue,maxValue)
                    gameFlow.list_setup(array)
                if event.key==pygame.K_RETURN:
                    shell_sort(gameFlow,gameFlow.lst)

    pygame.quit()


#-------------------user test code-------------

if __name__=="__main__":
    main()
    
