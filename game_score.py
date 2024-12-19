import turtle
from settings import FONT

score = 0  # Başlangıç skoru
score_turtle = turtle.Turtle()

def setup_score_turtle(screen):
    """Skor kaplumbağasını kurar."""
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0, y)
    update_score()

def update_score():
    """Skor göstergesini günceller."""
    global score
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=FONT)

def increase_score():
    """Skoru artırır ve günceller."""
    global score
    score += 1
    update_score()
