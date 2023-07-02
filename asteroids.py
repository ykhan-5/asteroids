import turtle
import time
from PIL import Image
import random

# myImage = Image.open("Spaceship.png")

points = 0
wn = turtle.Screen()
wn.title("Asteroids by Yusuf")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score = turtle.Turtle()
score.speed()
score.color("white")
score.penup() #keeps a line from forming
score.hideturtle()
score.goto(0,260) # top of the screen
score.write("Points: {}".format(points), align="center", font = ("Courier", 24, "normal"))


# Spaceship
Spaceship = turtle.Turtle()
Spaceship.speed(0)
Spaceship.shape("triangle")
Spaceship.color("blue")
Spaceship.shapesize(stretch_wid=1, stretch_len=1)
Spaceship.penup()
Spaceship.goto(-20, -250)
Spaceship.left(90)

# Bullet
bullets = []

def create_bullet():
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.color("red")
    bullet.shape("circle")
    bullet.shapesize(stretch_wid=0.1, stretch_len=0.1)
    bullet.penup()
    bullet.goto(Spaceship.xcor(), Spaceship.ycor())
    bullet.setheading(90)
    return bullet

def fire_bullet():
    bullet = create_bullet()
    bullets.append(bullet)


# Asteroids
asteroids = []


def create_asteroid():
    asteroid = turtle.Turtle()
    asteroid.speed(1)  # Adjust asteroid speed as needed
    asteroid.color("white")
    asteroid.shape("circle")
    asteroid.shapesize(stretch_wid=1, stretch_len=1)
    asteroid.penup()
    x = random.choice([-380, 380])
    y = random.randint(200, 300)  # Start asteroids from a random y-position near the top of the screen
    asteroid.goto(x, y)
    heading = random.randint(200, 340)  # Randomize the initial heading within a range
    asteroid.setheading(heading)
    return asteroid

def spawn_asteroid():
    asteroid = create_asteroid()
    asteroids.append(asteroid)

def move_asteroids():
    global points
    for asteroid in asteroids:
        asteroid.forward(1)  # Adjust asteroid speed by changing the distance it moves in each iteration
        # Check if asteroid goes off the screen
        x, y = asteroid.position()
        if x < -400 or x > 400 or y < -300 or y > 300:
            asteroids.remove(asteroid)
            asteroid.clear()
            asteroid.hideturtle()
        # Check for collision with bullets
        for bullet in bullets:
            if bullet.distance(asteroid) < 15:  # Adjust the collision distance as needed
                bullets.remove(bullet)
                bullet.clear()
                bullet.hideturtle()
                asteroids.remove(asteroid)
                asteroid.clear()
                asteroid.hideturtle()
                score.clear()
                points += 1
                score.write("Points: {}".format(points), align="center", font=("Courier", 24, "normal"))




# Spaceship movement
def ship_up():
    y = Spaceship.ycor()
    y += 10
    Spaceship.sety(y)

def ship_down():
    y = Spaceship.ycor()
    y -= 10
    Spaceship.sety(y)

def ship_right():
    x = Spaceship.xcor()
    x += 20
    Spaceship.setx(x)

def ship_left():
    x = Spaceship.xcor()
    x -= 20
    Spaceship.setx(x)

# Bullet movement
def move_bullets():
    for bullet in bullets:
        y = bullet.ycor()
        y += 10
        bullet.sety(y)

# Keyboard binding
wn.listen()

# Spaceship keys
wn.onkeypress(ship_up, "w")
wn.onkeypress(ship_down, "s")
wn.onkeypress(ship_right, "d")
wn.onkeypress(ship_left, "a")

# Bullet keys
wn.onkeypress(fire_bullet, 'g')

# Game loop
while True:
    wn.update()
    move_bullets()
    move_asteroids()
    time.sleep(0.01)

    # Randomly spawn asteroids
    if random.random() < 0.05:  # Adjust the probability to control the frequency of asteroid spawns
        spawn_asteroid()