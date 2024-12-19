import traceback
import turtle
from game_score import setup_score_turtle
from game_turtle import setup_turtles, show_turtles_randomly
from game_timer import countdown
from settings import SCREEN_TITLE, GAME_DURATION

# Oyun durumu
game_over = False


def game_over_callback():
    """Oyun bittiğinde çağrılır."""
    global game_over
    game_over = True
    try:
        print("Oyun sona erdi. Ekran kapatılıyor...")
        turtle.bye()  # Ekranı kapat
    except Exception as e:
        print("game_over_callback fonksiyonunda bir hata oluştu:")
        traceback.print_exc()


def start_game():
    """Oyunu başlatır."""
    global game_over
    game_over = False

    # Ekranı başlat
    screen = turtle.Screen()
    screen.title(SCREEN_TITLE)

    # Skor ve kaplumbağa ayarları
    setup_score_turtle(screen)
    setup_turtles()

    # Kaplumbağaları rastgele göster ve zamanlayıcıyı başlat
    show_turtles_randomly(game_over, screen)
    countdown(GAME_DURATION, screen, game_over_callback)

    screen.mainloop()


# Oyunu başlat
if __name__ == "__main__":
    try:
        start_game()
    except Exception as e:
        print("start_game fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
