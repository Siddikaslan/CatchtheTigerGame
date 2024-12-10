import turtle
import random
import time

window = turtle.Screen()
window.title("Catch the Tiger")
window.bgcolor("light green")
window.setup(width=800, height=600)


score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(0, 250)
score_turtle.speed(0)


timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.color("white")
timer_turtle.penup()
timer_turtle.goto(0, 220)
timer_turtle.speed(0)


tiger = turtle.Turtle()
tiger.shape("turtle")
tiger.color("orange")
tiger.penup()
tiger.speed(0)
tiger.goto(random.randint(-390, 390), random.randint(-290, 290))


score = 0
time_left = 30


def update_score():
    score_turtle.clear()
    score_turtle.write(f"Skorunuz:  {score}", align="center", font=("Courier", 24, "normal"))

def update_timer():
    timer_turtle.clear()
    timer_turtle.write(f"Geri sayım: {time_left}", align="center", font=("Courier", 24, "normal"))


def tiger_clicked(x, y):
    global score
    tiger.goto(random.randint(-390, 390), random.randint(-290, 290))
    score += 1
    update_score()


def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        update_timer()
        window.ontimer(countdown, 1000)
    else:
        tiger.hideturtle()
        score_turtle.goto(0, 0)
        score_turtle.write("Oyun Bitti! \n "f"Skorunuz: {score}", align="center", font=("Courier", 36, "normal"))


tiger.onclick(tiger_clicked)


update_score()
update_timer()


countdown()


window.mainloop()
