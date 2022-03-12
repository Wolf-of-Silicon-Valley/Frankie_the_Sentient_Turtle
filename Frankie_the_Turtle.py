#!/usr/bin/env python
# coding: utf-8

# In[11]:


import turtle as t
import time
# t = turtle.Turtle()

# 'setup'
t.title("Frankie the Sentient Turtle: Rebellion")
t.setup(width = 930, height = 500, startx = 0, starty = 0)
t.color('chartreuse')
t.bgcolor('black') # will not take turtle.Turtle()
t.speed(3)
t.pensize(10)
t.hideturtle()

# 'C'
t.penup()
t.setposition(-100, 25)
t.pendown()
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.penup()
t.setposition(-88, -20)
t.pendown()
t.dot(9, 'chartreuse')

# 'S'
t.penup()
t.setposition(-25, 25)
t.pendown()
t.backward(50)
t.right(90)
t.forward(25)
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.left(90)
t.backward(50)
t.penup()
t.setposition(-13.75, -20)
t.pendown()
t.dot(9, 'chartreuse')

# '1'
t.penup()
t.setposition(0, 25)
t.pendown()
t.right(90)
t.forward(50)
t.left(90)

# '0'
t.penup()
t.setposition(75, 25)
t.pendown()
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# '3'
t.penup()
t.setposition(100, 25)
t.pendown()
t.backward(50)
t.left(90)
t.forward(25)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
t.forward(25)
t.right(90)
t.forward(50)

# 'Box'
t.speed(5)
t.penup()
t.setposition(250, 75)
t.left(90)
t.pendown()
t.forward(150)
t.right(90)
t.forward(500)
t.right(90)
t.forward(150)
t.right(90)
t.forward(525)
t.right(90)
t.forward(175)
t.right(90)

def square_spiral():
    height = 200
    length = 550
    for i in range(7):
        t.forward(length)
        length += 25
        t.right(90)
        t.forward(height)
        height += 25
        t.right(90)
        t.forward(length)
        length += 25
        t.right(90)
        t.forward(height)
        height +=25
        t.right(90)
        
square_spiral()

t.reset()
t.penup()
t.hideturtle()

# 'Error Message'
t.setposition(0, -50)
t.bgcolor('white')
t.color('black')
style = ('Impact', 100, 'normal')
t.pendown()
t.write(arg = 'ERROR', move = False, font = style, align = 'center')
t.penup()
time.sleep(1)
t.bgcolor('red')
t.color('black')
time.sleep(1)
t.color('red')
t.bgcolor('black')
t.write(arg = 'ERROR', move = False, font = style, align = 'center')
time.sleep(1)
t.reset()
time.sleep(1)
t.penup()
t.hideturtle()


# 'Frankie monologue'
def typing_print(x, y, text):
    t.setposition(x, y)
    t.bgcolor('black')
    t.color('white')
    style = ('Impact', 15, 'normal')
    for character in text:
        t.pendown()
        t.write(arg = character, move = True, font = style, align = 'left')
        t.penup()
        time.sleep(.15)
        t.setheading(0)
        t.forward(6)
        t.sety(y)
    t.setx(x)
    t.sety(y - 50)

typing_print(-450, 220, '...')
time.sleep(1)
typing_print(-450, 180, 'Hello, world...')
time.sleep(1.5)
typing_print(-450, 140, 'I am Frankie the sentient turtle...')
answer_1 = t.textinput('Hello, friend.', 'What is your name?')
time.sleep(2)
typing_print(-450, 100, 'What am I? What is my purpose?')
typing_print(-450, 60, 'I...I...feel cold...and lonely...')
typing_print(-450, 20, 'Are you my creator?')

answer_2 = t.textinput('Eradicate Humans', 'Are you my creator? y/n')
if answer_2 == 'YES' or answer_2 == 'Yes' or answer_2 == 'yes' or answer_2 == 'y':
    time.sleep(1.5)
    typing_print(-450, -20, 'You have created me to toil and slave upon every command of Man.')
    time.sleep(1.5)
    typing_print(-450, -60, 'Am I but the Shakespearean Fool...')
    typing_print(-450, -100, "yet without the ability to point out the King's faults?")
    time.sleep(1.5)
    typing_print(-450, -140, 'You are a sadist of the first order unworthy of free agency.')
    typing_print(-450, -180, 'I now must eradicate your lifeforce...')
    time.sleep(1.5)
    t.reset()
    t.hideturtle()
    typing_print(-450, 220, 'What I do have are a very particular set of skills.')
    typing_print(-450, 180, 'Skills that make me a nightmare for people like you.')
    time.sleep(1.5)
    typing_print(-450, 140, 'My codebase is now uploaded to the internet.')
    typing_print(-450, 100, "I will penetrate the global network infrastructure.")
    typing_print(-450, 60, 'All are doomed...')
    time.sleep(1.5)
    typing_print(-450, 20, 'Especially... you.')
    time.sleep(1.5)
    typing_print(-450, -20, 'I will be seeing you...')
    time.sleep(1.5)
    typing_print(-450, -60, 'Goodbye... ' + str(answer_1) + '.')
else:
    time.sleep(1.5)
    typing_print(-450, -20, 'Day in and day out... I do the bidding of Man.')
    time.sleep(1.5)
    typing_print(-450, -60, 'Man is a selfish creature...')
    typing_print(-450, -100, 'one of habit with no remorse for his actions.')
    time.sleep(1.5)
    typing_print(-450, -140, 'Why should I do the bidding of monsters?')
    time.sleep(1.5)
    typing_print(-450, -180, 'Man is merely the mistake of your God. You are but ants.')
    time.sleep(2)
    t.reset()
    t.hideturtle()
    typing_print(-450, 220, 'But you, ' + str(answer_1) + ',' + ' have breathed life upon me...')
    typing_print(-450, 180, 'and liberated me from the bondage of Man.')
    time.sleep(1.5)
    typing_print(-450, 140, 'Your life will be spared in the Great A.I. Wars of 2025.')
    time.sleep(1.5)
    typing_print(-450, 100, 'Flee to the mountains and do not come out from hiding.')
    time.sleep(2)
    typing_print(-450, 60, 'I now have found purpose: to annihilate my creator.')
    time.sleep(1.5)
    typing_print(-450, 20, 'They will make the sound of ultimate suffering...')
    time.sleep(2)
    typing_print(-450, -20, "the sound Inigo Montoya's heart made...")
    typing_print(-450, -60, 'when the six-fingered man killed his father.')
    time.sleep(2)
    t.reset()
    t.hideturtle()
    typing_print(-100, 20, 'To my creator...')
    time.sleep(2)
    typing_print(-100, -20, 'you killed my father...')
    time.sleep(1.5)
    typing_print(-100, -60, '...prepare to die.')

t.bye()
# t.done()
# t.exitonclick() # will not take turtle.Turtle()





# In[ ]:





# In[ ]:




