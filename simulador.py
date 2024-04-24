import turtle

# CONSIDERAR VS
def dibujar_cuerda(color, numeros, i):
    # Configura el color y posición inicial de la cuerda
    turtle.color(color)
    x_start = -300
    y_start = -200 + 100*i  #50 * len(numeros)
    turtle.penup()
    turtle.goto(x_start, y_start)
    turtle.pendown()

    # Dibuja la cuerda
    turtle.forward(600)
    
    # Establece color de los circulos
    turtle.fillcolor(color)

    # Dibuja los nudos en la cuerda
    for numero in numeros:
        turtle.penup()
        turtle.goto(x_start + 20, y_start)
        turtle.pendown()
        k = 1
        for _ in range(numero):
            turtle.begin_fill()
            turtle.circle(7)  # Dibuja un círculo para cada "nudo"
            turtle.end_fill()
            turtle.penup()
            turtle.goto(x_start + 20   + 15*k, y_start)  # Espacio entre nudos
            k = k + 1
            turtle.pendown()
        x_start += 150  # Espacio entre grupos de nudos

def main():
    turtle.speed(-1)
    quipu = {
        'red': [3, 1, 4],  # Cada lista representa los nudos en una cuerda
        'green': [1, 5, 9, 2],
        'blue': [6, 1, 8],
        'orange': [2, 4, 2, 7],
        'purple': [7, 3, 4, 5]
    }
    
    # Dibuja cada cuerda del quipu
    for i, (color, nums) in enumerate(quipu.items()):
        dibujar_cuerda(color, nums, i)
    
    turtle.done()

if __name__ == "__main__":
    main()
