import turtle
import random
import traceback
from settings import GRID_SIZE

turtle_list = []


def setup_turtles():
    """Kaplumbağaları ekrana yerleştirir."""
    try:
        for x in range(-2, 3):  # Koordinatları ayarlayın
            for y in range(-2, 3):
                make_turtle(x * GRID_SIZE, y * GRID_SIZE)
    except Exception as e:
        print("setup_turtles fonksiyonunda bir hata oluştu:")
        traceback.print_exc()


def make_turtle(x, y):
    """Bir kaplumbağa nesnesi oluşturur."""
    try:
        t = turtle.Turtle()
        t.penup()
        t.shape("turtle")
        t.shapesize(2, 2)
        t.color("green")
        t.goto(x, y)
        t.hideturtle()
        turtle_list.append(t)

        # Tıklama olayını bağla
        def handle_click(x, y):
            from game_score import increase_score
            increase_score()
            t.hideturtle()

        t.onclick(handle_click)
    except Exception as e:
        print("make_turtle fonksiyonunda bir hata oluştu:")
        traceback.print_exc()


def hide_turtles():
    """Tüm kaplumbağaları gizler."""
    try:
        for t in turtle_list:
            t.hideturtle()
    except Exception as e:
        print("hide_turtles fonksiyonunda bir hata oluştu:")
        traceback.print_exc()


def show_turtles_randomly(game_over, screen, interval=500):
    """Kaplumbağaları rastgele bir şekilde gösterir."""
    try:
        if game_over or not getattr(screen, "_RUNNING", True):
            return
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(lambda: show_turtles_randomly(game_over, screen, interval), interval)
    except Exception as e:
        print("show_turtles_randomly fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
