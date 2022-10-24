import random
apple=Actor("apple")
def draw():
    screen.clear()
    apple.draw()
def place_apple():
    apple.x=random.randint(10,800)
    apple.y=random.randint(10,600)
def on_mouse_down(pos):
    count=0
    count+=1
    if apple.collidepoint(pos):
        
        print(count)
        print('good shot!')
        
        place_apple()
    else:
        print('you missed!')
        quit()
        
  
