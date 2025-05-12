import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a list of colors for the fireworks
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Create a turtle for drawing the fireworks
firework = turtle.Turtle()
firework.speed(0)  # Set the speed of drawing to the fastest

# Hide the turtle shape and only show the pen
firework.hideturtle()
firework.penup()

# Function to draw a single firework
def draw_firework():
    firework.color(random.choice(colors))  # Choose a random color
    firework.begin_fill()
    firework.circle(2)  # Draw the center of the firework
    firework.end_fill()
    firework.pendown()

    # Draw the explosion of the firework
    for _ in range(15):
        firework.color(random.choice(colors))
        firework.forward(25)
        firework.right(144)

    firework.penup()
    firework.home()  # Return the turtle to the center position

# Function to animate the fireworks
def animate_fireworks():
    screen.tracer(0)  # Turn off turtle animation

    for _ in range(5):  # Draw multiple fireworks per frame for a denser effect
        firework.goto(random.randint(-200, 200), random.randint(-200, 200))
        draw_firework()

    screen.update()  # Update the screen with all the fireworks

    screen.ontimer(animate_fireworks, 50)  # Schedule the next frame after 50 milliseconds

# Start the animation
animate_fireworks()

# Run the turtle main loop
turtle.mainloop()
