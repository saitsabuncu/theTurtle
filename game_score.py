import turtle, traceback
from settings import FONT

score = 0  # Başlangıç skoru
score_turtle = turtle.Turtle()

def setup_score_turtle(screen):
    """Skor göstergesini kurar ve gizli tutar."""
    try:
        score_turtle.hideturtle()  # Kaplumbağayı gizle
        score_turtle.color("blue")
        score_turtle.penup()
        top_height = screen.window_height() / 2
        y = top_height - top_height / 10
        score_turtle.setposition(0, y)
        update_score()  # İlk skoru ekrana yazdır
    except Exception as e:
        print("setup_score_turtle fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

def update_score():
    """Skor göstergesini günceller."""
    try:
        global score
        if not score_turtle.screen._RUNNING: # Ekranın çalışıp çalışmadığını kontrol
            return
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="center", font=FONT)
    except Exception as e:
        print("update_score fonksiyonunda bir hata oluştu:")
        traceback.print_exc()

def increase_score():
    """Skoru artırır."""
    try:
        global score
        score += 1
        update_score()
    except Exception as e:
        print("increase_score fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
