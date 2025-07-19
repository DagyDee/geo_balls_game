import pyglet
import random

# window
WIDTH = 1920
HEIGHT = 1080

# images
IMAGE_SIZE = 64
IMAGE_FRONT_SIDE = pyglet.image.load("green_ball.png")
IMAGE_BACK_SIDE = pyglet.image.load("red_ball.png")

LABELS = ["A=5", "B=3", "C=7", "D=1", "E=9", "F=2"]

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

class Ball:
    def __init__(self, hide_text):
        self.hide_text = hide_text  
        self.speed = 200
        self.ball_image = IMAGE_FRONT_SIDE
        self.show_text = False
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]  # coordinates x, y
        self.direction = [random.uniform(-1, 1), random.uniform(-1, 1)]  # in axes x, y
        self.sprite = pyglet.sprite.Sprite(self.ball_image, self.position[0] - IMAGE_SIZE // 2, self.position[1] - IMAGE_SIZE // 2)
        self.label = pyglet.text.Label(self.hide_text, font_size=20, color=(0, 0, 0), x=self.position[0], y=self.position[1], anchor_x='center', anchor_y='center')

    def draw(self):
        """
        Draws the image and the label, if it should be displayed.
        """
        self.sprite.draw()
        if self.show_text:
            self.label.draw()

    def move(self, dt):
        """
        Updates the object's position based on its direction and speed.
        Movement barriers ensure the ball bounces off the edges of the window.
        """
        self.position[0] += self.direction[0] * dt * self.speed
        self.position[1] += self.direction[1] * dt * self.speed

        # update sprite and label positions
        self.sprite.x = self.position[0] - IMAGE_SIZE // 2
        self.sprite.y = self.position[1] - IMAGE_SIZE // 2
        self.label.x = self.position[0]
        self.label.y = self.position[1]

        # movement barriers
        if self.position[0] < IMAGE_SIZE // 2:
            self.direction[0] = abs(self.direction[0])
        if self.position[0] > WIDTH - IMAGE_SIZE // 2:
            self.direction[0] = -abs(self.direction[0])
        if self.position[1] < IMAGE_SIZE // 2:
            self.direction[1] = abs(self.direction[1])
        if self.position[1] > HEIGHT - IMAGE_SIZE // 2:
            self.direction[1] = -abs(self.direction[1])
    
    def show_label(self, x, y, button, modifiers):
        """
        Changes the image and displays the label when the user clicks on the object.
        After a set time has passed, it calls the 'hide_label' function.
        """              
        if x >= self.position[0] - IMAGE_SIZE // 2 and x <= self.position[0] + IMAGE_SIZE // 2:
            if y >= self.position[1] - IMAGE_SIZE // 2 and y <= self.position[1] + IMAGE_SIZE // 2:
                self.show_text = True
                self.ball_image = IMAGE_BACK_SIDE
                self.sprite.image = self.ball_image
                pyglet.clock.schedule_once(self.hide_label, 0.5)
                
    def hide_label(self, t):
        """
        Changes the image and hides the label.
        """
        self.show_text = False
        self.ball_image = IMAGE_FRONT_SIDE
        self.sprite.image = self.ball_image

# creating objects:
balls = []

# create balls with secret
for label in LABELS:
    ball = Ball(label)
    balls.append(ball)

# create other balls
for ball in range(100):
    ball = Ball("X")
    balls.append(ball)

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
    pyglet.clock.schedule_interval(ball.move, 1/60)

pyglet.app.run()