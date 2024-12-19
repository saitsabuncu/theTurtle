import traceback, turtle
from game_score import setup_score_turtle
from game_turtle import setup_turtles, show_turtles_randomly, hide_turtles
from game_timer import countdown

game_over = False

def game_over_callback():
    """Oyun bittiğinde çağrılır."""
    global game_over
    game_over = True
    try:
        hide_turtles()  # Tüm kaplumbağaları gizle
        score_turtle.clear()  # Skor kaplumbağasını temizle
        count_down_turtle.clear()  # Zamanlayıcı kaplumbağasını temizle
        turtle.bye()  # Ekranı kapat
    except Exception as e:
        print("game_over_callback fonksiyonunda bir hata oluştu:")
        traceback.print_exc()


def start_game():
    try:
        global game_over
        game_over = False

        screen = turtle.Screen()
        screen.title("Catch the Turtle")
        setup_score_turtle(screen)
        setup_turtles()
        hide_turtles()
        show_turtles_randomly(game_over, screen)
        countdown(10, screen, game_over_callback)

        screen.mainloop()
    except Exception as e:
        print("start_game fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

# Oyunu başlat
start_game()
