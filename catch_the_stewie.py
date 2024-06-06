import turtle
import random
import time

# Score and time display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 380)

time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(0, 350)

# Score and time at beginning
score = 0
total_time = 20 # Second
start_time = time.time()

# Game screen
board = turtle.Screen()
board.bgcolor('light green')
board.title('Catch the Stewie')
board.register_shape('stewie.gif')

# Stewie 
stewie = turtle.Turtle()
stewie.shape('stewie.gif')
stewie.speed(0)
stewie.penup()

# Update score and time
def update_time():
    time_display.clear()
    # time.time() is current time
    remaining_time = total_time - (time.time() - start_time)
    remaining_min = int(remaining_time //  60)
    remaining_sec = int(remaining_time %  60)
    time_display.write(f"Remaining Time: {remaining_min}:{remaining_sec:02}", align="center", font=("Verdana", 16, "bold")) 

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Verdana", 16, "bold"))

# Increase score
def increase_score(x, y):
    global score
    stewie_position = stewie.pos()
    stewie_x = stewie_position[0]
    stewie_y = stewie_position[1]

    if x > stewie_x - 60 and x < stewie_x + 60 and y > stewie_y - 60 and y < stewie_y + 60:
        score += 10
        print(f"Congratulations! You earned {score} points.")

def start_game():
    while time.time() - start_time < total_time:
        update_score()
        update_time()
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        stewie.setx(x)
        stewie.sety(y)
        time.sleep(1)

board.onclick(increase_score)

start_game()
turtle.mainloop()
