import turtle
import traceback
from settings import FONT

timer_turtle = turtle.Turtle()


def countdown(time, screen, callback):
    """Geri sayımı başlatır."""
    try:
        if time <= 0:
            callback()
        else:
            timer_turtle.clear()
            timer_turtle.write(f"Time: {time}", align="center", font=FONT)
            screen.ontimer(lambda: countdown(time - 1, screen, callback), 1000)
    except Exception as e:
        print("countdown fonksiyonunda bir hata oluştu:")
        traceback.print_exc()
