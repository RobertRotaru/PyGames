import turtle
import time
import random

delay = 0.2

counter = 0

segments = []

score = 0
highScore = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", "24", "normal"))


window = turtle.Screen()
window.title("Snake Game by @robert_rotaru18")
window.bgcolor("green")
window.setup(width = 600, height = 600)
window.tracer(0)

# Functions
def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def move():
	if head.direction == "up" :
		y = head.ycor()
		head.sety(y + 20)
	if head.direction == "down" :
		y = head.ycor()
		head.sety(y - 20)
	if head.direction == "right" :
		x = head.xcor()
		head.setx(x + 20)
	if head.direction == "left" :
		x = head.xcor()
		head.setx(x - 20)

def restart():
	time.sleep(1)
	head.goto(0, 0)
	head.direction = "stop"

	# Hide segments
	for segment in segments:
		segment.goto(1000, 1000)

	# Clear the segment list
	segments.clear()


def writeTheScore():
	pen.clear()
	pen.write("Score: {}  High Score: {}".format(score, highScore), align = "center", font = ("Courier", "24", "normal"))


# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Game loop
while True:
	window.update()

	# Check colision border
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		restart()
		score = 0
		delay = 0.2
		writeTheScore()


	if head.distance(food) < 20:
		# Move food to random spot
		x = random.randrange(-280, 280, 20)
		y = random.randrange(-280, 280, 20)
		food.goto(x, y)
		counter += 1

		# Add segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		# Update score
		score += 10
		if score > highScore:
			highScore = score
		
		# Write scores
		pen.clear()
		pen.write("Score: {}  High Score: {}".format(score, highScore), align = "center", font = ("Courier", "24", "normal"))

	# Move the segments
	for i in range(len(segments) - 1, 0, -1):
		x = segments[i - 1].xcor()
		y = segments[i - 1].ycor()
		segments[i].goto(x, y)
	
	# Move segment 0
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	
	if counter % 4 == 0 and delay > 0.05 and counter > 0:
		delay -= 0.025
		counter = 1


	move()

	# Check colision body
	for segment in segments:
		if head.distance(segment) < 20:
			restart()
			score = 0
			delay = 0.2
			writeTheScore()

	time.sleep(delay)

window.mainloop()