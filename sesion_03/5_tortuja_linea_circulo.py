import turtle


if __name__ == "__main__":

    # Define velocidad
    turtle.speed(1)

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

    # Dibuja un círculo con un radio de 8 píxeles
    turtle.goto(x + 15,0) 
    turtle.circle(7)

    # Dibuja un círculo con un radio de 8 píxeles
    turtle.goto(x + 30,0) 
    turtle.circle(7)

    # Dibuja un círculo con un radio de 8 píxeles
    turtle.goto(x + 45,0) 
    turtle.circle(7)

    # Finaliza el relleno
    turtle.end_fill()

    # Cierra la ventana cuando se hace clic en ella
    turtle.done()

