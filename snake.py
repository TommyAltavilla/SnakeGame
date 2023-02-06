import turtle
import random

# Window Settings
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
level = 1

# Snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(-300, 0)
snake.dx = 0
snake.dy = 0

# Enemy

enemy = turtle.Turtle()
enemy.shape("square")
enemy.penup()
enemy.dx = 0
enemy.dy = 0
enemy.hideturtle()

# Checkpoint
check = turtle.Turtle()
check.speed(0)
check.shape("square")
check.color("green")
check.penup()
check.goto(300, 0)

# Level Counter
lc = turtle.Turtle()
lc.speed(0)
lc.color("white")
lc.penup()
lc.hideturtle()
lc.goto(0, 260)
lc.write("Level: 1", align="center", font=("Courier", 24, "normal"))


# Level 1 Borders
lvl11 = turtle.Turtle()
lvl11.speed(0)
lvl11.shape("square")
lvl11.color("white")
lvl11.shapesize(stretch_wid=0.15, stretch_len=50)
lvl11.penup()
lvl11.goto(0, 60)
lvl11.hideturtle()

lvl12 = turtle.Turtle()
lvl12.speed(0)
lvl12.shape("square")
lvl12.color("white")
lvl12.shapesize(stretch_wid=0.15, stretch_len=50)
lvl12.penup()
lvl12.goto(0, -60)
lvl12.hideturtle()

# Level 2 Borders
lvl21 = turtle.Turtle()
lvl21.speed(0)
lvl21.shape("square")
lvl21.color("white")
lvl21.shapesize(stretch_wid=0.15, stretch_len=35)
lvl21.penup()
lvl21.goto(0, 250)
lvl21.hideturtle()

lvl22 = turtle.Turtle()
lvl22.speed(0)
lvl22.shape("square")
lvl22.color("white")
lvl22.shapesize(stretch_wid=15, stretch_len=0.15)
lvl22.penup()
lvl22.goto(-350, 100)
lvl22.hideturtle()

lvl23 = turtle.Turtle()
lvl23.speed(0)
lvl23.shape("square")
lvl23.color("white")
lvl23.shapesize(stretch_wid=15, stretch_len=0.15)
lvl23.penup()
lvl23.goto(350, 100)
lvl23.hideturtle()

lvl24 = turtle.Turtle()
lvl24.speed(0)
lvl24.shape("square")
lvl24.color("white")
lvl24.shapesize(stretch_wid=0.15, stretch_len=25)
lvl24.penup()
lvl24.goto(0, 150)
lvl24.hideturtle()

lvl25 = turtle.Turtle()
lvl25.speed(0)
lvl25.shape("square")
lvl25.color("white")
lvl25.shapesize(stretch_wid=0.15, stretch_len=5)
lvl25.penup()
lvl25.goto(-300, -50)
lvl25.hideturtle()

lvl26 = turtle.Turtle()
lvl26.speed(0)
lvl26.shape("square")
lvl26.color("white")
lvl26.shapesize(stretch_wid=0.15, stretch_len=5)
lvl26.penup()
lvl26.goto(300, -50)
lvl26.hideturtle()

lvl27 = turtle.Turtle()
lvl27.speed(0)
lvl27.shape("square")
lvl27.color("white")
lvl27.shapesize(stretch_wid=10, stretch_len=0.15)
lvl27.penup()
lvl27.goto(250, 50)
lvl27.hideturtle()

lvl28 = turtle.Turtle()
lvl28.speed(0)
lvl28.shape("square")
lvl28.color("white")
lvl28.shapesize(stretch_wid=10, stretch_len=0.15)
lvl28.penup()
lvl28.goto(-250, 50)
lvl28.hideturtle()



# Functions
def snake_up():
    snake.dy = 1
    snake.dx = 0

def snake_down():
    snake.dy = -1
    snake.dx = 0

def snake_left():
    snake.dx = -1
    snake.dy = 0

def snake_right():
    snake.dx = 1
    snake.dy = 0

def enemyup():
    enemy.dy = 1

def enemydown():
    enemy.dy = -1

def hidelvl1():
    lvl11.hideturtle()
    lvl12.hideturtle()

def showlvl1():
    lvl11.showturtle()
    lvl12.showturtle()

def hidelvl2():
    lvl21.hideturtle()
    lvl22.hideturtle()
    lvl23.hideturtle()
    lvl24.hideturtle()
    lvl25.hideturtle()
    lvl26.hideturtle()
    lvl27.hideturtle()
    lvl28.hideturtle()

def showlvl2():
    lvl21.showturtle()
    lvl22.showturtle()
    lvl23.showturtle()
    lvl24.showturtle()
    lvl25.showturtle()
    lvl26.showturtle()
    lvl27.showturtle()
    lvl28.showturtle()

def reset():
    snake.goto(-300, 0)
    snake.dx = 0
    snake.dy = 0
    hidelvl2()
    showlvl1()
    level = 1
    
# Keyboard binding
wn.listen()
wn.onkeypress(snake_up, "w")
wn.onkeypress(snake_down, "s")
wn.onkeypress(snake_left, "a")
wn.onkeypress(snake_right, "d")

# Main game loop
while True:
    wn.update()

    # Move the Snake
    snake.sety(snake.ycor() + snake.dy)
    snake.setx(snake.xcor() + snake.dx)

    # Border Collision
    if snake.ycor() > 290:
        snake.sety(290)
        snake.dy = 0

    if snake.ycor() < -280:
        snake.sety(-280)
        snake.dy = 0

    if snake.xcor() > 380:
        snake.setx(380)
        snake.dx = 0
        
    if snake.xcor() < -390:
        snake.setx(-390)
        snake.dx = 0

    # Checkpoint Collision
    if (snake.xcor() > 280 and snake.xcor() < 320) and (snake.ycor() > -20 and snake.ycor() < 20):
        snake.goto(-300, 0)
        level +=1
        lc.clear()
        lc.write("Level: {}".format(level), align="center", font=("Courier", 24, "normal"))
        snake.dx = 0
        snake.dy = 0

    # Level 1
    if level == 1:
        showlvl1()
        if snake.ycor() > 50 or snake.ycor() < -50:
            reset()

    # Level 2
    if level == 2:
        hidelvl1()
        showlvl2()
        if snake.xcor() < -340 or snake.xcor() > 340 or snake.ycor() < -40 or snake.ycor() > 240:
            reset()
        elif (snake.xcor() > -260 and snake.xcor() < 260 and snake.ycor() < 160):
            reset()

        
            

    

    
