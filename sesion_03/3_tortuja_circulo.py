import turtle


if __name__ == "__main__":

    turtle.speed(1)

    turtle.goto(0,0) 

    # Define el color
    turtle.color("red")

    # inicia el relleno
    turtle.begin_fill()

    # Dibuja un círculo con un radio de 100 píxeles
    turtle.circle(100)

    # Finaliza el relleno
    turtle.end_fill()

    # Cierra la ventana cuando se hace clic en ella
    turtle.done()

