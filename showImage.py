import turtle

def get_imagename_not_unid(n):
    return f"assets/overhand-knot-{n}.gif"

def get_imagename_unid(n):
    return f"assets/long-knot-{n}.gif"

def get_imagename_top_not_unid(n):
    return f"assets/top-overhand-knot-{n}.gif"

def get_imagename_top_unid(n):
    return f"assets/top-long-knot-{n}.gif"

#turtle.speed(10)

# Hide the turtle pointer
# turtle.hideturtle()

turtle.tracer(0, 0)  # Turn off animation, set delay to 0

# Set up the screen
screen = turtle.Screen()
screen.title("Quipu")
# Use setup to make the window large enough to fill the screen
screen.setup(width=0.99, height=0.99)  # Use almost full width and height of the display

# Register the GIF image
screen.addshape("assets/end-knot.gif")  
screen.addshape("assets/grid.gif")  
screen.addshape("assets/top-cord.gif")  
screen.addshape("assets/top-grid.gif")  
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
screen.addshape("assets/top-long-knot-1.gif")  
screen.addshape("assets/top-long-knot-2.gif")  
screen.addshape("assets/top-long-knot-3.gif")  
screen.addshape("assets/top-long-knot-4.gif")  
screen.addshape("assets/top-long-knot-5.gif")  
screen.addshape("assets/top-long-knot-6.gif")  
screen.addshape("assets/top-long-knot-7.gif")  
screen.addshape("assets/top-long-knot-8.gif")  
screen.addshape("assets/top-long-knot-9.gif")  
screen.addshape("assets/top-overhand-knot-1.gif")  
screen.addshape("assets/top-overhand-knot-2.gif")  
screen.addshape("assets/top-overhand-knot-3.gif")  
screen.addshape("assets/top-overhand-knot-4.gif")  
screen.addshape("assets/top-overhand-knot-5.gif")  
screen.addshape("assets/top-overhand-knot-6.gif")  
screen.addshape("assets/top-overhand-knot-7.gif")  
screen.addshape("assets/top-overhand-knot-8.gif")  
screen.addshape("assets/top-overhand-knot-9.gif")  

IDX_MIL = 0
IDX_CEN = 1
IDX_DEC = 2
IDX_UNI = 3

IDX_SUM_DEC_MIL = 0
IDX_SUM_UNI_MIL = 1
IDX_SUM_CEN     = 2
IDX_SUM_DEC     = 3
IDX_SUM_UNI     = 4


numbers =[1000, 2024, 1234 , 5234, 120, 1000]

numbers =[1, 20, 12 , 10, 1, 3]

_sum = sum(numbers)
print(_sum)

x = -350
y =  80 # 30

image_turtle0 = turtle.Turtle()
image_turtle0.shape("assets/end-knot.gif")  
image_turtle0.penup()
image_turtle0.goto(x-40, y)  
image_turtle0.stamp() 

for number in numbers[:3]:

    str_number = f"{number:04}" 

    image_turtle1 = turtle.Turtle()
    image_turtle1.shape("assets/primary-cord.gif")  
    image_turtle1.penup()
    image_turtle1.goto(x, y)  

    image_turtle2 = turtle.Turtle()
    image_turtle2.shape("assets/grid.gif")  
    image_turtle2.penup()
    image_turtle2.goto(x, y-180)  

    image_turtle3 = turtle.Turtle()
    image_turtle3.shape("assets/pendant-cord.gif")  
    image_turtle3.penup()
    image_turtle3.goto(x, y-220)  

    image_turtle4 = turtle.Turtle()
    if str_number[IDX_MIL] != '0':
        image_turtle4.shape(get_imagename_not_unid(str_number[IDX_MIL]))
        image_turtle4.penup()
        image_turtle4.goto(x, y-70)  

    image_turtle5 = turtle.Turtle()
    if str_number[IDX_CEN] != '0':
        image_turtle5.shape(get_imagename_not_unid(str_number[IDX_CEN]))
        image_turtle5.penup()
        image_turtle5.goto(x, y-180)  

    image_turtle6 = turtle.Turtle()
    if str_number[IDX_DEC] != '0':
        image_turtle6.shape(get_imagename_not_unid(str_number[IDX_DEC]))
        image_turtle6.penup()
        image_turtle6.goto(x, y-290)  

    image_turtle7 = turtle.Turtle()
    if str_number[IDX_UNI] != '0':
        image_turtle7.shape(get_imagename_unid(str_number[IDX_UNI]))
        image_turtle7.penup()
        image_turtle7.goto(x, y-400)  

    x = x + 50

    image_turtle1.stamp() 
    image_turtle2.stamp() 
    image_turtle3.stamp() 
    image_turtle4.stamp() 
    image_turtle5.stamp() 
    image_turtle6.stamp() 
    image_turtle7.stamp() 

image_turtle10 = turtle.Turtle()
image_turtle10.shape("assets/primary-cord.gif")  
image_turtle10.penup()
image_turtle10.goto(x, y)  

image_turtle11 = turtle.Turtle()
image_turtle11.shape("assets/top-cord.gif")  
image_turtle11.penup()
image_turtle11.goto(x+250, y+140)  

image_turtle12 = turtle.Turtle()
image_turtle12.shape("assets/top-grid.gif")  
image_turtle12.penup()
image_turtle12.goto(x+235, y+265)  

##
str_sum = f"{_sum:05}"

# DEC MIL
image_turtle13 = turtle.Turtle()
if str_sum[IDX_SUM_DEC_MIL] != '0':
    image_turtle13.shape(get_imagename_top_not_unid(str_sum[IDX_SUM_DEC_MIL])) 
    image_turtle13.penup()
    image_turtle13.goto(x+80, y+60)  

# MIL
image_turtle14 = turtle.Turtle()
if str_sum[IDX_SUM_UNI_MIL] != '0':
    image_turtle14.shape(get_imagename_top_not_unid(str_sum[IDX_SUM_UNI_MIL])) 
    image_turtle14.penup()
    image_turtle14.goto(x+180, y+118)  

# CENT
image_turtle15 = turtle.Turtle()
if str_sum[IDX_SUM_CEN] != '0':
    image_turtle15.shape(get_imagename_top_not_unid(str_sum[IDX_SUM_CEN])) 
    image_turtle15.penup()
    image_turtle15.goto(x+280, y+175)  

# DEC
image_turtle16 = turtle.Turtle()
if str_sum[IDX_SUM_DEC] != '0':
    image_turtle16.shape(get_imagename_top_not_unid(str_sum[IDX_SUM_DEC]))  
    image_turtle16.penup()
    image_turtle16.goto(x+380, y+230)  

# UNID
image_turtle17 = turtle.Turtle()
if str_sum[IDX_SUM_UNI] != '0':
    image_turtle17.shape(get_imagename_top_unid(str_sum[IDX_SUM_UNI]))   
    image_turtle17.penup()
    image_turtle17.goto(x+470, y+280)  

image_turtle10.stamp() 
image_turtle11.stamp() 
image_turtle12.stamp() 

image_turtle13.stamp()
image_turtle14.stamp() 
image_turtle15.stamp() 
image_turtle16.stamp() 
image_turtle17.stamp() 

x = x + 50

for number in numbers[3:6]:

    str_number = f"{number:04}" 

    image_turtle1 = turtle.Turtle()
    image_turtle1.shape("assets/primary-cord.gif")  
    image_turtle1.penup()
    image_turtle1.goto(x, y)  

    image_turtle2 = turtle.Turtle()
    image_turtle2.shape("assets/grid.gif")  
    image_turtle2.penup()
    image_turtle2.goto(x, y-180)  

    image_turtle3 = turtle.Turtle()
    image_turtle3.shape("assets/pendant-cord.gif")  
    image_turtle3.penup()
    image_turtle3.goto(x, y-220)  

    image_turtle4 = turtle.Turtle()
    if str_number[IDX_MIL] != '0':
        image_turtle4.shape(get_imagename_not_unid(str_number[IDX_MIL]))
        image_turtle4.penup()
        image_turtle4.goto(x, y-70)  

    image_turtle5 = turtle.Turtle()
    if str_number[IDX_CEN] != '0':
        image_turtle5.shape(get_imagename_not_unid(str_number[IDX_CEN]))
        image_turtle5.penup()
        image_turtle5.goto(x, y-180)  

    image_turtle6 = turtle.Turtle()
    if str_number[IDX_DEC] != '0':
        image_turtle6.shape(get_imagename_not_unid(str_number[IDX_DEC]))
        image_turtle6.penup()
        image_turtle6.goto(x, y-290)  

    image_turtle7 = turtle.Turtle()
    if str_number[IDX_UNI] != '0':
        image_turtle7.shape(get_imagename_unid(str_number[IDX_UNI]))
        image_turtle7.penup()
        image_turtle7.goto(x, y-400)  

    
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
