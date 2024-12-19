import traceback
import turtle
from game_turtle import hide_turtles
from settings import FONT

count_down_turtle = turtle.Turtle()

def countdown(time, screen, game_over_callback):
    """Geri sayım işlemini yönetir."""
    try:
        if not screen._RUNNING:
            return
        top_height = screen.window_height() / 2
        y = top_height - top_height / 10
        count_down_turtle.hideturtle()
        count_down_turtle.penup()
        count_down_turtle.setposition(0, y - 30)
        count_down_turtle.clear()

        if time > 0:
            count_down_turtle.write(f"Time: {time}", align="center", font=FONT)
            screen.ontimer(lambda: countdown(time - 1, screen, game_over_callback), 1000)
        else:
            hide_turtles()
            count_down_turtle.write("Game Over!", align="center", font=FONT)
            game_over_callback()
    except Exception as e:
        print("countdown fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
