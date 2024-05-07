import turtle


if __name__ == "__main__":

    # Define velocidad
    turtle.speed(0)

    # Define el color
    turtle.color("red")

    x = -300

    # Se posiciona origen
    turtle.penup()
    turtle.goto(x,0) 
    turtle.pendown()

    # Dibuja una linea
    turtle.forward(600)

    # inicia el relleno
    turtle.begin_fill()

    # millares
    for i in range(9):
        # Dibuja un círculo con un radio de 8 píxeles
        turtle.goto(x + 000 + 15 * (i + 1),0) 
        turtle.circle(7)

    # centenas
    for i in range(9):
        # Dibuja un círculo con un radio de 8 píxeles
        turtle.goto(x + 150 + 15 * (i + 1),0) 
        turtle.circle(7)

    # decenas
    for i in range(9):
        # Dibuja un círculo con un radio de 8 píxeles
        turtle.goto(x + 300 + 15 * (i + 1),0) 
        turtle.circle(7)

    # unidades
    for i in range(9):
        # Dibuja un círculo con un radio de 8 píxeles
        turtle.goto(x + 450 + 15 * (i + 1),0) 
        turtle.circle(7)

    # Finaliza el relleno
    turtle.end_fill()

    # Cierra la ventana cuando se hace clic en ella
    turtle.done()

