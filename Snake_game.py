import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Simple Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.shape("circle")
head.color("yellow")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "Right"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align="center", font=("Arial", 24, "normal"))

segments = []

def go(direction):
    head.direction = direction

def move():
    if head.direction == "Up":
        head.sety(head.ycor() + 20)
    elif head.direction == "Down":
        head.sety(head.ycor() - 20)
    elif head.direction == "Left":
        head.setx(head.xcor() - 20)
    elif head.direction == "Right":
        head.setx(head.xcor() + 20)

def check_collision():
    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        reset_game()

    for segment in segments:
        if head.distance(segment) < 20:
            reset_game()

def reset_game():
    global score, delay, high_score

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Right"
    score = 0
    delay = 0.1
    pen.clear()
    pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

wn.listen()
wn.onkeypress(lambda: go("Up"), "Up")
wn.onkeypress(lambda: go("Down"), "Down")
wn.onkeypress(lambda: go("Left"), "Left")
wn.onkeypress(lambda: go("Right"), "Right")

while True:
    wn.update()
    move()
    check_collision()

    if head.distance(food) < 20:
        x, y = random.randint(-270, 270), random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].pos())

    if len(segments) > 0:
        segments[0].goto(head.pos())

    time.sleep(delay)
