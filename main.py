import turtle
from game_score import setup_score_turtle
from game_turtle import setup_turtles, show_turtles_randomly
from game_timer import countdown

game_over = False

def game_over_callback():
    """Oyun bittiğinde çağrılır."""
    global game_over
    game_over = True

def start_game():
    """Oyunu başlatır."""
    global game_over
    game_over = False

    screen = turtle.Screen()
    screen.title("Catch the Turtle")
    setup_score_turtle(screen)
    setup_turtles()
    show_turtles_randomly(game_over, screen)
    countdown(10, screen, game_over_callback)

    screen.mainloop()

# Oyunu başlat
start_game()
