import random
import turtle
import pygame
from game_difficulty import Difficulty

# Pygame'i başlat
pygame.init()

# Ses dosyalarını yükle
click_sound = pygame.mixer.Sound('sounds/click_sound.wav')
game_over_sound = pygame.mixer.Sound("game_over.wav")

# Ekran ve temel değişkenler
screen = turtle.Screen()
screen.title("Catch The Turtle")
game_over = False
score = 0
FONT = ('Arial', 30, 'normal')

# Kaplumbağa listesi ve diğer kaplumbağalar
turtle_list = []
count_down_turtle = turtle.Turtle()
score_turtle = turtle.Turtle()

# Zorluk sınıfını başlat
difficulty = Difficulty()


def setup_game():
    """Oyunu başlatmadan önce kullanıcıdan zorluk seviyesi al."""
    level = screen.textinput("Zorluk Seviyesi", "Kolay (easy), Orta (medium), Zor (hard):")
    if level:
        level = level.lower()
    try:
        difficulty.set_difficulty(level)
    except ValueError:
        screen.textinput("Hata", "Geçerli bir zorluk seviyesi girin! Varsayılan: Kolay")
        difficulty.set_difficulty("easy")


def make_turtle(x, y):
    """Bir kaplumbağa nesnesi oluştur ve başlangıç pozisyonuna yerleştir."""
    t = turtle.Turtle()

    def handle_click(x, y):
        """Tıklama işlemiyle puan güncelle."""
        global score
        score += 1
        pygame.mixer.Sound.play(click_sound)  # Tıklama sesi çal
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * 10, y * 10)
    t.hideturtle()
    turtle_list.append(t)


def setup_turtles():
    """Kaplumbağa nesnelerini oluştur ve konumlandır."""
    global turtle_list
    x_coordinates = [-20, -10, 0, 10, 20]
    y_coordinates = [20, 10, 0, -10]

    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    """Tüm kaplumbağaları gizle."""
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    """Kaplumbağaları rastgele bir şekilde göster."""
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        speed = difficulty.get_settings()["speed"]  # Zorluk seviyesine göre hız
        screen.ontimer(show_turtles_randomly, speed)


def countdown(time):
    """Geri sayım işlemini gerçekleştirir."""
    global game_over
    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        pygame.mixer.Sound.play(game_over_sound)  # Game Over sesi çal
        count_down_turtle.write("Game Over!", align='center', font=FONT)


def setup_score_turtle():
    """Skor ekranını ayarlar."""
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2  # Ekranın üst kısmı
    y = top_height - top_height / 10  # Skorun görüneceği yer
    score_turtle.setposition(0, y)
    score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)


def start_game_up():
    """Oyunu başlatır."""
    global game_over
    game_over = False
    setup_game()  # Kullanıcıdan zorluk seviyesi al
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    time_limit = difficulty.get_settings()["time_limit"]  # Zorluk seviyesine göre süre
    countdown(time_limit)


# Oyunu başlat
start_game_up()
turtle.mainloop()

