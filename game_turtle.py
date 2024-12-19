import traceback
import turtle
import random
from settings import GRID_SIZE, X_COORDINATES, Y_COORDINATES
from game_score import increase_score

turtle_list = []

def make_turtle(x, y):
    """Bir kaplumbağa nesnesi oluşturur."""
    try:
        t = turtle.Turtle()

        def handle_click(x, y):
            increase_score()  # Tıklanınca skoru artır

        t.onclick(handle_click)
        t.penup()
        t.shape("turtle")
        t.shapesize(2, 2)
        t.color("green")
        t.goto(x * GRID_SIZE, y * GRID_SIZE)
        t.hideturtle()  # Başlangıçta kaplumbağayı gizle
        turtle_list.append(t)
    except Exception as e:
        print("make_turtle fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

def setup_turtles():
    try:
        for x in X_COORDINATES:
            for y in Y_COORDINATES:
                make_turtle(x, y)
    except Exception as e:
        print("setup_turtles fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

def hide_turtles():
    try:
        for t in turtle_list:
            t.hideturtle()
    except Exception as e:
        print("hide_turtles fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

def show_turtles_randomly(game_over, screen, interval=500):
    """Kaplumbağaları rastgele bir şekilde gösterir."""
    try:
        if game_over or not screen._RUNNING:  # Oyun bitti mi ya da ekran kapandı mı?
            return
        hide_turtles()  # Önce tüm kaplumbağaları gizle
        if turtle_list:  # Turtle listesi boş değilse
            random.choice(turtle_list).showturtle()  # Rastgele bir kaplumbağa göster
        screen.ontimer(lambda: show_turtles_randomly(game_over, screen, interval), interval)
    except Exception as e:
        print("show_turtles_randomly fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
