

# N O T E : My program first draws the gallows , then hangman's body parts and in the end the rope by which is hung.

import stddraw

def draw_hangman(i):
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(-1, 1)

    stddraw.setPenColor(stddraw.BLACK)


    if i == 8:                      #Draw the gallows ( without the hanging rope )
        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8,0.10)
        stddraw.show(0)

    elif i== 7:                     #Draw face

        stddraw.circle(-0.7, 0.75, 0.05)

        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i==6:                       #Draw neck
        stddraw.circle(-0.7, 0.75, 0.05)
        stddraw.line(-0.7, 0.70, -0.7, 0.65)

        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i==5:                       #Draw left hand
        stddraw.circle(-0.7, 0.75, 0.05)

        stddraw.line(-0.7, 0.70, -0.7, 0.65)
        stddraw.line(-0.7, 0.65, -0.8, 0.60)
        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i==4:                        #Draw right hand
        stddraw.circle(-0.7, 0.75, 0.05)
        stddraw.line(-0.7, 0.70, -0.7, 0.65)
        stddraw.line(-0.7, 0.65, -0.8, 0.60)
        stddraw.line(-0.7, 0.65, -0.6, 0.60)
        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i==3:                                 #Draw body
        stddraw.circle(-0.7, 0.75, 0.05)
        stddraw.line(-0.7, 0.70, -0.7, 0.65) #neck
        stddraw.line(-0.7, 0.65, -0.8, 0.60) #left hand
        stddraw.line(-0.7, 0.65, -0.6, 0.60) #right hand
        stddraw.line(-0.7, 0.65, -0.7, 0.40) #body

        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)
        stddraw.show(0)

    elif i == 2:                        #Draw left leg
        stddraw.circle(-0.7, 0.75, 0.05)
        stddraw.line(-0.7, 0.70, -0.7, 0.65)  # neck
        stddraw.line(-0.7, 0.65, -0.8, 0.60)  # left hand
        stddraw.line(-0.7, 0.65, -0.6, 0.60)  # right hand
        stddraw.line(-0.7, 0.65, -0.7, 0.40)  # body
        stddraw.line(-0.7, 0.40, -0.8, 0.35)  # left leg

        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i == 1:                           #Draw right leg
        stddraw.circle(-0.7, 0.75, 0.05)

        stddraw.line(-0.7, 0.70, -0.7, 0.65)  # neck
        stddraw.line(-0.7, 0.65, -0.8, 0.60)  # left hand
        stddraw.line(-0.7, 0.65, -0.6, 0.60)  # right hand
        stddraw.line(-0.7, 0.65, -0.7, 0.40)  # body
        stddraw.line(-0.7, 0.40, -0.8, 0.35)  # left leg
        stddraw.line(-0.7, 0.40, -0.6, 0.35)  # right leg
        stddraw.line(-0.7, 0.40, -0.6, 0.35)
        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)

        stddraw.show(0)

    elif i == 0:                            # finally draw the hanging rope
        stddraw.circle(-0.7, 0.75, 0.05)
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(-0.7, 0.90, -0.7, 0.80)  #hangrope
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.line(-0.7, 0.70, -0.7, 0.65)  # neck
        stddraw.line(-0.7, 0.65, -0.8, 0.60)  # left hand
        stddraw.line(-0.7, 0.65, -0.6, 0.60)  # right hand
        stddraw.line(-0.7, 0.65, -0.7, 0.40)  # body
        stddraw.line(-0.7, 0.40, -0.8, 0.35)  # left leg
        stddraw.line(-0.7, 0.40, -0.6, 0.35)  # right leg
        stddraw.line(-0.7, 0.40, -0.6, 0.35)
        stddraw.line(-0.7, 0.90, -0.5, 0.90)
        stddraw.line(-0.5, 0.90, -0.5, 0.10)
        stddraw.line(-0.5, 0.10, -0.9, 0.10)
        stddraw.line(-0.9, 0.10, -0.9, 0)
        stddraw.line(-0.9, 0, -0.1, 0)
        stddraw.line(-0.1, 0, -0.1, 0.10)
        stddraw.line(-0.1, 0.10, -0.8, 0.10)


        stddraw.show(0)

def word(i):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(40)
    stddraw.text(-0.2,-0.5,i)
    stddraw.show(0)

def wrong_guesses(i):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-1, -1, 2, 0.2)
    stddraw.setPenColor(stddraw.RED)
    stddraw.setFontSize(40)
    stddraw.text(-0.2,-0.9,i)
    stddraw.show(0)

def correct_word(i):
    stddraw.setFontSize(40)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.text(-0.2,-0.7,"The word was: "+i)
    stddraw.show(0)
