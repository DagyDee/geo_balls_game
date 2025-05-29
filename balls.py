import pyglet
import random

# window
WIDTH = 1920
HEIGHT = 1080

green_ball = pyglet.image.load("green.png")
red_ball = pyglet.image.load("red.png")

class Ball:

    def initialize(self):
        self.size = 64
        self.speed = 500
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]  # coordinates x, y
        self.direction = [random.uniform(-1, 1), random.uniform(-1, 1)]  #  in axes x, y
        self.ball_image = green_ball

    def draw(self):
        self.obrazek = pyglet.sprite.Sprite(self.ball_image, self.position[0] - self.size // 2, self.position[1] - self.size // 2)
        self.obrazek.draw()

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
                self.ball_image = red_ball
                pyglet.clock.schedule_once(self.change_image_back, 0.5)
                
    def change_image_back(self, t):
        self.ball_image = green_ball
        

ball_A = Ball()
ball_A.initialize()

ball_B = Ball()
ball_B.initialize()

green_ball = pyglet.image.load("green.png")
red_ball = pyglet.image.load("red.png")

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
    window.clear()
    ball_A.draw()
    ball_B.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    ball_A.change_image(x, y, button, modifiers)
    ball_B.change_image(x, y, button, modifiers)

pyglet.clock.schedule(ball_A.move)
pyglet.clock.schedule(ball_B.move)

pyglet.app.run()