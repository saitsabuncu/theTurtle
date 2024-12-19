import turtle, random
from settings import GRID_SIZE, X_COORDINATES, Y_COORDINATES
from game_score import increase_score

turtle_list = []

def make_turtle(x, y):
    """Bir kaplumbağa nesnesi oluşturur."""
    t = turtle.Turtle()

    def handle_click(x, y):
        increase_score()

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * GRID_SIZE, y * GRID_SIZE)
    t.hideturtle()
    turtle_list.append(t)

def setup_turtles():
    """Tüm kaplumbağaları oluşturur."""
    for x in X_COORDINATES:
        for y in Y_COORDINATES:
            make_turtle(x, y)

def hide_turtles():
    """Tüm kaplumbağaları gizler."""
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly(game_over, screen):
    """Kaplumbağaları rastgele bir şekilde gösterir."""
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(lambda: show_turtles_randomly(game_over, screen), 500)
