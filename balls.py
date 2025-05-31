import pyglet
import random

# window
WIDTH = 1920
HEIGHT = 1080

# images
red_ball = pyglet.image.load("red.png")
yellow_ball = pyglet.image.load("yellow.png")

labels = ["A=5", "B=3", "C=7", "D=1", "E=9", "F=2"]

class Ball:
    def __init__(self, hide_text):
        self.hide_text = hide_text

    def initialize(self):
        self.size = 64
        self.speed = 200
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]  # coordinates x, y
        self.direction = [random.uniform(-1, 1), random.uniform(-1, 1)]  #  in axes x, y
        self.ball_image = red_ball
        self.show_text = False

    def draw(self):
        self.picture = pyglet.sprite.Sprite(self.ball_image, self.position[0] - self.size // 2, self.position[1] - self.size // 2)
        self.picture.draw()
        self.label = pyglet.text.Label(self.hide_text, font_size=20, color=(0, 0, 0), x=self.position[0], y=self.position[1], anchor_x='center', anchor_y='center')
        if self.show_text == True:
            self.label.draw()

    def move(self, dt):
        self.position[0] += self.direction[0] * dt * self.speed
        self.position[1] += self.direction[1] * dt * self.speed

        # movement barriers
        if self.position[0] < self.size // 2:
            self.direction[0] = abs(self.direction[0])
        if self.position[0] > WIDTH - self.size // 2:
            self.direction[0] = -abs(self.direction[0])
        if self.position[1] < self.size // 2:
            self.direction[1] = abs(self.direction[1])
        if self.position[1] > HEIGHT - self.size // 2:
            self.direction[1] = -abs(self.direction[1])
    
    def show_label(self, x, y, button, modifiers):
        if x >= self.position[0] - self.size // 2 and x <= self.position[0] + self.size // 2:
            if y >= self.position[1] - self.size // 2 and y <= self.position[1] + self.size // 2:
                self.show_text = True
                self.ball_image = yellow_ball

                pyglet.clock.schedule_once(self.hide_label, 0.5)
                
    def hide_label(self, t):
        self.show_text = False
        self.ball_image = red_ball

# creating objects:
balls = []

# create balls with secret
for label in labels:
    ball = Ball(label)
    ball.initialize()
    balls.append(ball)

# create other balls
for ball in range(100):
    ball = Ball("X")
    ball.initialize()
    balls.append(ball)


window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
    window.clear()
    for ball in balls:
        ball.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    for ball in balls:
        ball.show_label(x, y, button, modifiers)

for ball in balls:
    pyglet.clock.schedule(ball.move)

pyglet.app.run()