import pgzrun

WIDTH = 600
HEIGHT = 500

def draw():
    screen.fill ("black")
    bounce.ball()

class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    def ball(self):
        screen.draw.filled_circle((self.x,self.y),self.radius, "purple")

bounce = Ball(300,250)

gravity = 2000

def update(dt):
    uy = bounce.vy
    bounce.vy += gravity*dt
    bounce.y += (uy + bounce.vy)*0.5*dt
    if bounce.y > HEIGHT-bounce.radius:
        bounce.y = HEIGHT-bounce.radius
        bounce.vy = -bounce.vy*0.9
    bounce.x += bounce.vx*dt
    if bounce.x > WIDTH-bounce.radius or bounce.x < bounce.radius:
        bounce.vx = -bounce.vx
def on_key_down(key):
    if key == keys.SPACE:
        bounce.vy = -500

# uy = initial velocity, vy = final velocity, dt = change in time
pgzrun.go()