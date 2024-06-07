import turtle


def get_imagename_not_unid(n):
    return f"assets/overhand-knot-{n}.gif"

def get_imagename_unid(n):
    return f"assets/long-knot-{n}.gif"


turtle.speed(10)

# Hide the turtle pointer
turtle.hideturtle()

turtle.tracer(0, 0)  # Turn off animation, set delay to 0


# Set up the screen
screen = turtle.Screen()
screen.title("Turtle with an Image")

# Register the GIF image
screen.addshape("assets/end-knot.gif")  
screen.addshape("assets/grid.gif")  
screen.addshape("assets/primary-cord.gif")  
screen.addshape("assets/pendant-cord.gif")  
screen.addshape("assets/long-knot-1.gif")  
screen.addshape("assets/long-knot-2.gif")  
screen.addshape("assets/long-knot-3.gif")  
screen.addshape("assets/long-knot-4.gif")  
screen.addshape("assets/long-knot-5.gif")  
screen.addshape("assets/long-knot-6.gif")  
screen.addshape("assets/long-knot-7.gif")  
screen.addshape("assets/long-knot-8.gif")  
screen.addshape("assets/long-knot-9.gif")  
screen.addshape("assets/overhand-knot-1.gif")  
screen.addshape("assets/overhand-knot-2.gif")  
screen.addshape("assets/overhand-knot-3.gif")  
screen.addshape("assets/overhand-knot-4.gif")  
screen.addshape("assets/overhand-knot-5.gif")  
screen.addshape("assets/overhand-knot-6.gif")  
screen.addshape("assets/overhand-knot-7.gif")  
screen.addshape("assets/overhand-knot-8.gif")  
screen.addshape("assets/overhand-knot-9.gif")  

IDX_MIL = 0
IDX_CEN = 1
IDX_DEC = 2
IDX_UNI = 3

numbers =[9999, 1034, 3944, 2546, 1001, 2341, 900, 23]

x = -350
y = -300

image_turtle0 = turtle.Turtle()
image_turtle0.shape("assets/end-knot.gif")  
image_turtle0.penup()
image_turtle0.goto(x-40, 30)  
image_turtle0.stamp() 

for number in numbers:

    str_number = f"{number:04}" 

    image_turtle1 = turtle.Turtle()
    image_turtle1.shape("assets/primary-cord.gif")  
    image_turtle1.penup()
    image_turtle1.goto(x, 30)  

    image_turtle2 = turtle.Turtle()
    image_turtle2.shape("assets/grid.gif")  
    image_turtle2.penup()
    image_turtle2.goto(x, -150)  

    image_turtle3 = turtle.Turtle()
    image_turtle3.shape("assets/pendant-cord.gif")  
    image_turtle3.penup()
    image_turtle3.goto(x, -190)  

    image_turtle4 = turtle.Turtle()
    if str_number[IDX_MIL] != '0':
        image_turtle4.shape(get_imagename_not_unid(str_number[IDX_MIL]))
        image_turtle4.penup()
        image_turtle4.goto(x, -40)  

    image_turtle5 = turtle.Turtle()
    if str_number[IDX_CEN] != '0':
        image_turtle5.shape(get_imagename_not_unid(str_number[IDX_CEN]))
        image_turtle5.penup()
        image_turtle5.goto(x, -150)  

    image_turtle6 = turtle.Turtle()
    if str_number[IDX_DEC] != '0':
        image_turtle6.shape(get_imagename_not_unid(str_number[IDX_DEC]))
        image_turtle6.penup()
        image_turtle6.goto(x, -260)  

    image_turtle7 = turtle.Turtle()
    if str_number[IDX_UNI] != '0':
        image_turtle7.shape(get_imagename_unid(str_number[IDX_UNI]))
        image_turtle7.penup()
        image_turtle7.goto(x, -370)  

    x = x + 50

    image_turtle1.stamp() 
    image_turtle2.stamp() 
    image_turtle3.stamp() 
    image_turtle4.stamp() 
    image_turtle5.stamp() 
    image_turtle6.stamp() 
    image_turtle7.stamp() 

turtle.mainloop()

#turtle.update()  # Update the screen only once after all changes are made
