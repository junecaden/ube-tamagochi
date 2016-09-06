# Python: Lab 10
# Junmanee Cadenhead

'''
Ube, the purple-sweet-potato-Ice-cream loves to play Rock, Paper Scissors!
Press the Play button to begin!

Ube is created by four different classes:
    -StaticPet class that shows no emotion
    -HappyPet class that  draws a happy mood
    -NeutralPet that draws a neutral mood
    -MadPet class that draws a mad mood

There is also a Rock, Paper, Scissors Class that defines how the game works
and determines who the winner is. Ube's mood reflects his score in the
Rock, Paper, Scissors game.

The hunger meter reflects Ube's hunger level, press the 'Feed' button to make
sure Ube doesn't play on an empty stomach!

The game is played through typing your move into the Python Shell. 
'''

from graphics import *
from button import *
import random

#------------------Drawing the static body parts of Ube----------------------

class StaticPet:

    '''StaticPet: creates and draws the static components of the Tamagotchi'''

    def __init__(self):
        #arms
        self.arms = Oval(Point(-30, -2), Point(30, -25))
        self.arms.setFill("lavender")
        self.arms.setOutline("lavender")


        #arm holes
        self.armhole = Oval(Point(-24, -4), Point(24, -23))
        self.armhole.setFill("gray")
        self.armhole.setOutline("gray")
       

        #hands
        self.hands = Oval(Point(-15, -30), Point(15, -15))
        self.hands.setFill("lavender")
        self.hands.setOutline("lavender")


        #cone
        self.cone = Polygon(Point(-25, 10), Point(0, -50), Point(25, 10))
        self.cone.setFill("lemon chiffon")
        self.cone.setOutline("lemon chiffon")


        #scoop
        self.scoop = Circle(Point(0, 30), 30)
        self.scoop.setFill("lavender")
        self.scoop.setOutline("lavender")


        #sprinkles
        self.h1 = Text(Point(0, 64), "\ | /" )
        self.h1.setSize(36)
        self.h1.setTextColor('pink')


        #left eye
        self.leye = Circle(Point(-15, 35), 15)
        self.leye.setFill("white")
        self.leye.setOutline("white")


        #left pupil
        self.lpupil = Circle(Point(-15, 35), 10)
        self.lpupil.setFill("gray44")
        self.lpupil.setOutline("gray44")


        #right eye
        self.reye = Circle(Point(15, 35), 15)
        self.reye.setFill("white")
        self.reye.setOutline("white")


        #right pupil
        self.rpupil = Circle(Point(15, 35), 10)
        self.rpupil.setFill("gray44")
        self.rpupil.setOutline("gray44")


        #press play to play again
        self.h1 = Text(Point(0, -80), "press the 'play button' to play!" )
        self.h1.setSize(30)
        self.h1.setTextColor('white')


    def setMood(self, moodRPS):
        self.petMood = moodRPS
        return self.petMood


    def draw(self, win):
        self.arms.draw(win)
        self.armhole.draw(win)
        self.hands.draw(win)
        self.cone.draw(win)
        self.scoop.draw(win)
        self.leye.draw(win)
        self.lpupil.draw(win)
        self.reye.draw(win)
        self.rpupil.draw(win)
        self.h1.draw(win)
       

#-------------Drawing / Undrawing Ube's happy expression--------------

class HappyPet:

    '''Creates and draws the happy expression of the Tamagotchi'''

    def __init__(self):
        #left cheek
        self.lcheek = Circle(Point(-15,15), 15)
        self.lcheek.setFill("lavender")
        self.lcheek.setOutline("lavender")


        #right cheeck
        self.rcheek = Circle(Point(15,15), 15)
        self.rcheek.setFill("lavender")
        self.rcheek.setOutline("lavender")

        #smile
        self.smile = Circle(Point(0,15), 10)
        self.smile.setFill("RosyBrown1")
        self.smile.setOutline("RosyBrown1")


        #upper-lip
        self.lip = Rectangle(Point(-15, 25), Point(15,15))
        self.lip.setFill("lavender")
        self.lip.setOutline("lavender")


    def draw(self, win):
        self.lcheek.draw(win)
        self.rcheek.draw(win)
        self.smile.draw(win)
        self.lip.draw(win)


    def undraw(self, win):
        self.lcheek.undraw()
        self.rcheek.undraw()
        self.smile.undraw()
        self.lip.undraw()


#-------------Drawing / Undrawing Ube's neutral expression--------------
       

class NeutralPet:

    '''Creates and draws the neutral expression of the Tamagotchi'''

    def __init__(self):
        #chin
        self.chin = Oval(Point(-30, 0), Point(30, 20))
        self.chin.setFill("lavender")
        self.chin.setOutline("lavender")

        #mouth
        self.mouth = Rectangle(Point(-5,5), Point(5,7))
        self.mouth.setFill("RosyBrown1")
        self.mouth.setOutline("RosyBrown1")

    def draw(self, win):
        self.chin.draw(win)
        self.mouth.draw(win)

    def undraw(self, win):
        self.chin.undraw()
        self.mouth.undraw()

        

#-----------------Drawing / Undrawing Ube's mad expression-------------------


class MadPet:

    '''Creates and draws the mad expression of the Tamagotchi'''

    def __init__(self):
        #chin
        self.chin = Oval(Point(-30, 0), Point(30, 20))
        self.chin.setFill("lavender")
        self.chin.setOutline("lavender")
       

        #eyeborws
        self.brow = Oval(Point(-25, 55), Point(25, 40))
        self.brow.setFill("lavender")
        self.brow.setOutline("lavender")


        #mouth
        self.mouth = Rectangle(Point(-5,5), Point(5,7))
        self.mouth.setFill("RosyBrown1")
        self.mouth.setOutline("RosyBrown1")
        

        #bite marks
        self.bite1 = Circle(Point(25, 35), 8)
        self.bite1.setFill("gray")
        self.bite1.setOutline("gray")

        self.bite2 =Circle(Point(15, 42), 8)
        self.bite2.setFill("gray")
        self.bite2.setOutline("gray")

        self.bite3 =Circle(Point(13, 53), 8)
        self.bite3.setFill("gray")
        self.bite3.setOutline("gray")

        self.bite4 =Circle(Point(20, 50), 11)
        self.bite4.setFill("gray")
        self.bite4.setOutline("gray")

        
    def draw(self, win):
        self.chin.draw(win)
        self.brow.draw(win)
        self.mouth.draw(win)
        self.bite1.draw(win)
        self.bite2.draw(win)
        self.bite3.draw(win)
        self.bite4.draw(win)

    def undraw(self, win):
        self.chin.undraw()
        self.brow.undraw()
        self.mouth.undraw()
        self.bite1.undraw()
        self.bite2.undraw()
        self.bite3.undraw()
        self.bite4.undraw()

#========================Creating Buttons========================


class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):

        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()


    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False



#==========================Rock, Paper, Scissors===========================

class RockPaperScissors:

    def __init__(self, playerRPS, moodRPS, happy, neutral, mad):
        self.getMood = neutral       

        #User Input
        self.playerRPS = playerRPS
        self.moodRPS = moodRPS
        
        #Determining Ube's random move
        self.iceRPS = random.randint(1,3)
        if self.iceRPS == 1:
            self.iceRPS = 'rock'
        elif self.iceRPS == 2:
            self.iceRPS = 'paper'
        elif self.iceRPS == 3:
            self.iceRPS = 'scissors'
        print("Ube's Move: ", self.iceRPS)

        #Determining who the winner is
        if (self.playerRPS == self.iceRPS):
                print("It's a Draw!");
                self.moodRPS = neutral
        elif (self.playerRPS == "rock"):
                if (self.iceRPS == "paper"):
                        print("Ube FTW!")
                        self.moodRPS = happy
                else:
                        print("You win!");
                        self.moodRPS = mad
        elif (self.playerRPS == "paper"):
                if (self.iceRPS == "rock"):
                        print("You win!");
                        self.moodRPS = mad
                else:
                        print("Ube FTW!")
                        self.moodRPS = happy
        elif (self.playerRPS == "scissors"):
                if (self.iceRPS == "rock"):
                        print("Ube FTW!")
                        self.moodRPS = happy
                else:
                        print("You win!");
                        self.moodRPS = mad



    def setMood(self, mood):
        self.moodRPS = mood

    def undraw(self, win):
        self.moodRPS.undraw(win)

    def draw(self, win):
        self.moodRPS.draw(win)



#========================Hunger Meter=========================

class HungerMeter:

    def __init__(self, hungerlevel, win):
        self.w = 10
        self.h = 30
        self.y = -20
        self.x = -65
        self.boxHM = Rectangle(Point(self.x + self.w,self.y + self.h), Point(self.x,self.y))
        self.setHM = Rectangle(Point(self.x, self.y), Point(self.x,self.y))
        self.boxHM.draw(win)
        
        self.hungerlevel = hungerlevel
        
        self.mathy = self.y + self.h /5 * self.hungerlevel
        self.setHM = Rectangle(Point(self.x + self.w, self.y), Point(self.x, self.mathy))
        self.setHM.setFill("lavender")
        self.setHM.draw(win)

    def eat(self, win):
        self.setHM.undraw() 
        if self.hungerlevel == 5:
            self.hungerlevel = 4             
        elif self.hungerlevel == 4:           
            self.hungerlevel = 3                            
        elif self.hungerlevel == 3:
            self.hungerlevel = 2             
        elif self.hungerlevel == 2:
            self.hungerlevel = 1


        print('hunger level: ', self.hungerlevel)
        
        self.mathy = self.y + self.h /5 * self.hungerlevel
        self.setHM = Rectangle(Point(self.x + self.w, self.y), Point(self.x, self.mathy))
        self.setHM.setFill("lavender")

        self.setHM.draw(win)


    def feed(self, win):
        self.setHM.undraw()
        if self.hungerlevel == 1:
            self.hungerlevel = 2            
        elif self.hungerlevel == 2:           
            self.hungerlevel = 3                             
        elif self.hungerlevel == 3:
            self.hungerlevel = 4              
        elif self.hungerlevel == 4:
            self.hungerlevel = 5
        
        self.mathy = self.y + self.h /5 * self.hungerlevel
        self.setHM = Rectangle(Point(self.x + self.w, self.y), Point(self.x, self.mathy))
        self.setHM.setFill("lavender")
        self.setHM.draw(win)
       


#==================================================================        

def main():

    win = GraphWin( "Ube's Moods", 500, 500, autoflush = False)
    win.setBackground('gray')
    win.setCoords(-100, -100, 100, 100)

    playing = True
    body = StaticPet()
    body.draw(win)
    happy = HappyPet()
    neutral = NeutralPet()
    mad = MadPet()


    hungerlevel = 5
    meter = HungerMeter(hungerlevel, win)
    moodRPS = neutral
#-------------------------Draw Buttons---------------------------

    width = 20
    height = 10   

    #Play Button
    center = Point(50, 80)
    label = 'Play!'
    Play_button = Button(win, center, width, height, label)
    Play_button.activate()


    #Feed Button
    center = Point(-60, -30)
    label = 'Feed'
    Feed_button = Button(win, center, width, height, label)

    #Quit Button
    center = Point(-50, 80)
    label = 'Quit?'
    Quit_button = Button(win, center, width, height, label)
    Quit_button.activate()


    while playing:    

#----------------------Play Button Response------------------------

        MousePosition = win.getMouse()

            
        if Play_button.clicked(MousePosition):
            Feed_button.activate()
            meter.eat(win)

#------------------User Input for Game and Emotions-------------------
                
            playerRPS = input("Enter your choice (rock/paper/scissors): ")
            
            happy.undraw(win)
            neutral.undraw(win)
            mad.undraw(win)
            
##        if meter.eat(win) == 1:
##            Play_button.deactivate()
              
            RPS = RockPaperScissors(playerRPS, moodRPS, happy, neutral, mad)
            RPS.draw(win)

#------------------------Other Button Response------------------------
           
        if Feed_button.clicked(MousePosition):
            meter.feed(win)

        if Quit_button.clicked(MousePosition):
            win.close()
            playing = False


main()

