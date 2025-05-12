import turtle
import datetime

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Analog Clock")
screen.tracer(0)  # Turns off screen updates

# Create the clock face
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.hideturtle()
clock_face.penup()
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.circle(200)

# Create the hour hand
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.shape("arrow")
hour_hand.color("black")
hour_hand.shapesize(stretch_wid=0.5, stretch_len=10)
hour_hand.penup()

# Create the minute hand
minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.shape("arrow")
minute_hand.color("black")
minute_hand.shapesize(stretch_wid=0.5, stretch_len=15)
minute_hand.penup()

# Create the second hand
second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.5, stretch_len=18)
second_hand.penup()

# Function to update the clock hands
def update_clock():
    now = datetime.datetime.now()
    hour_angle = (now.hour % 12) * 30 + now.minute * 0.5
    minute_angle = now.minute * 6
    second_angle = now.second * 6

    hour_hand.setheading(-hour_angle)
    minute_hand.setheading(-minute_angle)
    second_hand.setheading(-second_angle)

    screen.update()
    screen.ontimer(update_clock, 1000)  # Update every 1 second

# Call the update_clock function to start the clock
update_clock()

# Start the turtle graphics main loop
turtle.done()
