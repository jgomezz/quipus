import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle with an Image")

# Register the GIF image

screen.addshape("assets/pendant-cord.gif")  
screen.addshape("assets/overhand-knot-5.gif")  
screen.addshape("assets/overhand-knot-6.gif")  
screen.addshape("assets/overhand-knot-7.gif")  
screen.addshape("assets/overhand-knot-8.gif")  

# Create a turtle to display the image
image_turtle = turtle.Turtle()
image_turtle.shape("assets/pendant-cord.gif")  
image_turtle.penup()
image_turtle.goto(0, 9)  # Central position

image_turtle2 = turtle.Turtle()
image_turtle2.shape("assets/overhand-knot-6.gif")
image_turtle2.penup()
image_turtle2.goto(0, 0)  # Slightly offset to create an overlay effect

image_turtle3 = turtle.Turtle()
image_turtle3.shape("assets/overhand-knot-5.gif")
image_turtle3.penup()
image_turtle3.goto(0, 100)  # Slightly offset to create an overlay effect

#image_turtle.shape("assets/overhand-knot-7.gif")
#image_turtle.shape("assets/overhand-knot-8.gif")

image_turtle.stamp()  # Stamps the image onto the screen
image_turtle2.stamp()  # Stamps the image onto the screen
image_turtle3.stamp()  # Stamps the image onto the screen

# Keep the window open until it is closed by the user
turtle.mainloop()