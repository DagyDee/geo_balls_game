import pyglet
import random

# window
WIDTH = 1920
HEIGHT = 1080

green_ball = pyglet.image.load("green.png")
red_ball = pyglet.image.load("red.png")
yellow_ball = pyglet.image.load("yellow.png")
purple_ball = pyglet.image.load("purple.png")
blue_ball = pyglet.image.load("blue.png")

class Ball:
    def __init__(self, hide_picture):
        self.hide_picture = hide_picture

    def initialize(self):
        self.size = 64
        self.speed = 500
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]  # coordinates x, y
        self.direction = [random.uniform(-1, 1), random.uniform(-1, 1)]  #  in axes x, y
        self.ball_image = green_ball

    def draw(self):
        self.picture = pyglet.sprite.Sprite(self.ball_image, self.position[0] - self.size // 2, self.position[1] - self.size // 2)
        self.picture.draw()

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
    
    def change_image(self, x, y, button, modifiers):
        if x >= self.position[0] - self.size // 2 and x <= self.position[0] + self.size // 2:
            if y >= self.position[1] - self.size // 2 and y <= self.position[1] + self.size // 2:
                self.ball_image = self.hide_picture
                pyglet.clock.schedule_once(self.change_image_back, 0.5)
                
    def change_image_back(self, t):
        self.ball_image = green_ball
        
code_ball = [red_ball, yellow_ball, purple_ball]
balls = []
for code in code_ball:
    ball = Ball(code)
    ball.initialize()
    balls.append(ball)

for ball in range(10):
    ball = Ball(blue_ball)
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
        ball.change_image(x, y, button, modifiers)

for ball in balls:
    pyglet.clock.schedule(ball.move)

pyglet.app.run()