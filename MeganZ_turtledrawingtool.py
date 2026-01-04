# Turtle Drawing Tool
# Author: Megan Zhang
# Date: June 13, 2023

import turtle
import time
import math

# Define the variables
colour_list = ["sienna", "firebrick", "dark orange", "gold", "forest green",
               "dark cyan", "cornflower blue", "slate blue", "pale violet red",
               "black"]
# Note: you must have the gifs downloaded for it to work
brush_icon = ["brush_b.gif", "brush_r.gif", "brush_o.gif", "brush_y.gif",
              "brush_g.gif","brush_c.gif", "brush_b1.gif", "brush_p.gif",
              "brush_p1.gif", "brush_b2.gif"] 
FPS = 1000

# Set up the window
window = turtle.Screen()
window.tracer(0)

# Define the brush
brush = turtle.Turtle()
brush.width(5)
turtle.register_shape("brush_b2.gif")
brush.shape("brush_b2.gif")

# Set up the canvas
def draw_perimeter(x, y, width, height):
    """Draw the perimeter of the canvas."""
    setup_peri = turtle.Turtle()
    setup_peri.hideturtle()
    # Set up the colour of the border and the fill colour
    setup_peri.pencolor("alice blue")
    setup_peri.fillcolor("alice blue")
    setup_peri.penup()
    setup_peri.goto(x, y)
    setup_peri.begin_fill()
    setup_peri.pendown()
    setup_peri.seth(0)
    setup_peri.forward(width)
    setup_peri.seth(270)
    setup_peri.forward(height)
    setup_peri.seth(180)
    setup_peri.forward(width)
    setup_peri.seth(90)
    setup_peri.forward(height)
    setup_peri.end_fill()


def draw_canvas():
    """Set up the canvas with the tools and colour options."""
    # Draw the perimeter of the canvas
    setup = turtle.Turtle()
    # Set the window popup size 
    turtle.setup(700, 685)
    setup.hideturtle()
    setup.penup()
    circle_xcor = -315
    # Create colour swatches for each colour
    for colour in colour_list:
        setup.goto(circle_xcor, 290)
        setup.pendown()
        setup.fillcolor(colour)
        setup.begin_fill()
        setup.circle(16)
        setup.end_fill()
        setup.penup()
        circle_xcor += 70

    
# Create icons for the toolbar on the bottom of the canvas
def create_tool(x, shape):
    """Creates the tool icons for the toolbar."""
    tool = turtle.Turtle()
    tool.penup()
    tool.goto(x, -305)
    # Register the .gif images as shapes
    turtle.register_shape(shape)
    tool.shape(shape)

    
# Have turtle follow the user's mouse when they click and drag
def follow_mouse(x, y):
    """Animation of turtle following the user's mouse when click and dragged."""    
    brush.ondrag(None)
    brush.setheading(brush.towards(x, y))
    brush.goto(x, y)
    brush.ondrag(follow_mouse)
    # Check whether the mouse has gone out of bounds
    if x <= -330 or x >= 320 or y <= -277 or y >= 270 or brush.shape() == "mouse.gif":
        brush.penup()
    # If the mouse comes back into bounds, continue drawing
    elif x >= -330 and x <= 320 and y >= -277 and y <= 270:
        brush.pendown()

       
# Change tools when selecting a tool icon 
def change_tool(x, y):
    """Changes the tool and colour when the user selects a tool icon."""
    # Check whether the user selects on the paint swatch
    swatch_xcor = [315, 245, 175, 105, 35, -35, -105, -175, -245, -315]
    for i in range(len(swatch_xcor)):
        xcor = swatch_xcor[i]
        colour = colour_list[i]
        # Check whether the click was within the circle's radius
        if math.sqrt((x + xcor)**2 + (y - 290)**2) < 16:
            brush.pencolor(colour)
            # Change paint brush icons when selecting a colour
            brush_shape = brush_icon[i]
            turtle.register_shape(brush_shape)
            brush.shape(brush_shape)

    # Changes the tool to a mouse if user clicks on icon
    if math.sqrt((x + 175)**2 + (y + 305)**2) < 16:
        brush.shape("mouse.gif")
        brush.penup()
    # Changes to an eraser if user selects the eraser icon
    if math.sqrt((x + 105)**2 + (y + 305)**2) < 16:
        brush.shape("eraser.gif")
        brush.pencolor("white")
    # Clears all of the brush's drawings if user clicks on clearall icon
    if math.sqrt((x + 35)**2 + (y + 305)**2) < 16:
        brush.clear()   
    # Changes the size to small if user clicks on icon
    if math.sqrt((x - 35)**2 + (y + 305)**2) < 16:
        brush.width(2)
    # Changes the size to medium if user clicks on icon
    if math.sqrt((x - 105)**2 + (y + 305)**2) < 16:
        brush.width(5)
    # Changes the size to medium if user clicks on icon
    if math.sqrt((x - 175)**2 + (y + 305)**2) < 16:
        brush.width(10)


# Create a smooth animation for drawing
def animate():
    """Create a continuous animation loop."""
    window.update()
    window.ontimer(animate, int(1 / FPS))
        
# Run the program

# Left side panel
draw_perimeter(-350, 340, 675, 65)
# Top panel
draw_perimeter(-350, 340, 18, 675)
# Bottom panel
draw_perimeter(-350, -280, 675, 65)
# Right side panel
draw_perimeter(325, 340, 18, 685)
# Draw the canvas
draw_canvas()
# Create the toolbar on the bottom of the canvas
create_tool(-175, "mouse.gif")
create_tool(-105, "eraser.gif")
create_tool(-35, "clearall.gif")
create_tool(35, "small_size.gif")
create_tool(105, "medium_size.gif")
create_tool(175, "large_size.gif")
# Allow the user to drag the brush around to draw
follow_mouse(0, 0)
screen = turtle.Screen()
screen.listen()
screen.onscreenclick(change_tool)
animate()
