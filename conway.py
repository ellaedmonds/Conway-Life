"""
conway.py
Author: Ella Edmonds
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

#print("Press the space bar to pause or play simulation.")
#print("When the simulation is paused, click to remove or add cells.")
print("Green Cells are babies and yellow cells are older")
print("A cell will survive if it has 2-3 neighbors, and a dead cell will create life if it has 3 neighbors.")

w = int(input("How wide would you like youre grid? "))
l = int(input("How long would you like youre grid? "))

class DeadCell(Sprite):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
    def __init__(self,position):
        super().__init__(DeadCell.square,position)

class BabyCell(Sprite):
    green = Color(0x00ff00,.8)
    side = LineStyle(1,green)
    square1 = RectangleAsset(8,8,side,green)
    
    def __init__(self,position):
        super().__init__(BabyCell.square1,position)
        
class LiveCell(Sprite):
    yellow = Color(0xffff00,.8)
    side = LineStyle(1,yellow)
    square2 = RectangleAsset(8,8,side,yellow)
    
    def __init__(self,position):
        super().__init__(LiveCell.square2,position)


class Game(App):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
        
    def __init__(self, width, height):
        super().__init__(width, height)
        Game.listenMouseEvent("click",self.baby)
        
        
        a = []
        x = []
        y = []
        
        b=[]
        
        for m in range(w):
            x.append(10+(8*m))
            y.append(10)
            b.append(10+(8*m))
            
        for m in b:
            for n in range(l):
                x.append(m)
                y.append(18+(n*8))
            
        
        d = zip(x,y)
        Cells=[]
        
        for m in d:
            DeadCell((m[0],m[1]))
            Cells.append((m[0],m[1]))
        
        
        #for n in range(len(d)):
         #   Cell((x,y))
        
    
    def baby(self,event):
        click = []
        print(event.x,event.y)
        BabyCell((event.x,event.y))
        click.append((event.x,event.y))
        
    def inbetween(self,position):
        for m in Cells:
            if click[0] == m[0] or click[0] <= m[0]+8:
                LiveCell((m[0],m[1]))
        
        
    




myapp = Game(500, 500)
myapp.run()