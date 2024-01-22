import turtle, math, random
class Ball(turtle.Turtle):
    '''
    Purpose: Ball represents the tennis ball within the game and the motion,
        direction, and speed of the ball after it is hit and after it is reset.
    Instance variables:
        self.vx: Velocity of the ball in the x direction.
        self.vy: Velocity of the ball in the y direction.
        self.bounce: Counts how many times the ball bounces on the court.
        self.right_hit_count: Counts how many times the player on the right
            side of the court hits the ball.
        self.left_hit_count: Counts how many times the player on the left
            side of the court hits the ball.
        self.rightpower: Increases and decreases the level of power the player
            on the right side of the court wants to hit the ball at.
        self.leftpower: Increases and decreases the level of power the player
            on the left side of the court wants to hit the ball at.
    Methods:
        __init__(): Initializes instance variables and initializes position and
            appearance of the tennis ball.
        reset(): Resets instance variables to initial values and initializes
            new position and velocities of the ball.
        move(): Gives the ball an arc downwards to represent gravity acting on
            the ball. Also, adds to and resets the self.bounce count.
        rightpower_up(): Increases the player on the right side of the court's
            hit power.
        rightpower_down(): Decreases the player on the right side of the court's
            hit power.
        rightpower_reset(): Resets the player on the right side of the court's
            hit power to the initial power value.
        leftpower_up(): Increases the player on the left side of the court's
            hit power.
        leftpower_down(): Decreases the player on the left side of the court's
            hit power.
        leftpower_reset(): Resets the player on the left side of the court's
            hit power to the initial power value.
        right_hit(): Represents the player on the right side of the court
            hitting the ball. Also, it resets the self.left_hit_count when
            the self.right_hit_count is greater or equal to 1.
        left_hit(): Represents the player on the left side of the court
            hitting the ball. Also, it resets the self.right_hit_count when
            the self.left_hit_count is greater or equal to 1.
    '''
    def __init__(self, x, y, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.bounce = 0
        self.right_hit_count = 0
        self.left_hit_count = 0
        self.rightpower = 0
        self.leftpower = 0
        self.shape('circle')
        self.turtlesize(0.3)
        self.penup()
        self.setpos(x,y)
    def reset(self):
        self.bounce = 0
        self.right_hit_count = 0
        self.left_hit_count = 0
        self.rightpower = 0
        self.leftpower = 0
        rand_x = random.uniform(-100,100)
        rand_y = random.uniform(30,100)
        rand_int = random.randint (1,2)
        if rand_int == 1:
            self.vx = random.uniform(-12,-6)
        else:
            self.vx = random.uniform(6,12)
        self.vy = random.uniform(4,10)
        self.goto(rand_x, rand_y)
    def move(self):
        self.vy = self.vy-0.981
        x_coordinate = self.xcor()+self.vx
        if (self.xcor() >=0 and x_coordinate <= 0) or (self.xcor() <=0 and x_coordinate >= 0):
            self.bounce = 0
        y_coordinate = self.ycor()+self.vy
        if y_coordinate<0:
            y_coordinate = -(y_coordinate*(3/4))
            self.vy = -(self.vy*(3/4))
            self.bounce += 1
        self.goto(x_coordinate,y_coordinate)
    def rightpower_up(self):
        self.rightpower -= 2
    def rightpower_down(self):
        if self.rightpower < 8:
            self.rightpower += 2
    def rightpower_reset(self):
        self.rightpower = 0
    def leftpower_up(self):
        self.leftpower += 2
    def leftpower_down(self):
        if self.leftpower > -8:
            self.leftpower -= 2
    def leftpower_reset(self):
        self.leftpower = 0
    def right_hit(self):
        if self.xcor() >=0:
            self.vx = -10 + self.rightpower
            self.vy = 15
            self.right_hit_count += 1
        if self.right_hit_count >= 1:
            self.left_hit_count = 0
    def left_hit(self):
        if self.xcor() < 0:
            self.vx = 10 + self.leftpower
            self.vy = 15
            self.left_hit_count += 1
        if self.left_hit_count >= 1:
            self.right_hit_count = 0

class Game:
    '''
    Purpose: Creates the court, net, and score system and prompts a tennis
        game to begin. (How to play) W, A, S, and D keys are the controls for
        the left side player and the up, down, right, and left keys are the
        controls for the right side player. The left and D keys hit the ball,
        the up and W keys increases the hit power and the down and S keys
        decrease the hit power, and the right and A keys reset the hit power to
        the default hit power. To reset the game press the space bar.
    Instance variables:
        self.right_point: Keeps track of the amount of points the player on
            the right side of the court scores.
        self.left_point: Keeps track of the amount of points the player on
            the left side of the court scores.
        self.t: Creates a turtle meant for writing the score of the game.
        self.ball: Creates a tennis ball with an initial position and velocity.
    Methods:
        __init__(): Initializes the intance variables, creates a court with
            a net, calls gameloop, and assigns keys to functions that will
            hit the ball and change the hit power for each player.
        point_reset(): Resets the whole game with points back to 0 and calls
            the reset() method from the Ball class.
        score(): Writes and updates the score of the tennis match.
        gameloop(): Assigns rules and regulations to the game and if a player
            loses a point then the game score updates, the reset() method from
            the ball class is called, and a new point automatically begins.
    '''
    def __init__(self):
        print('Right Player Controls:\n   Left: Hit Ball\n   Up: Increase Hit Power\n   Down: Decrease Hit Power\n   Right: Reset Hit Power to Default\n')
        print('Left Player Controls:\n   D: Hit Ball\n   W: Increase Hit Power\n   S: Decrease Hit Power\n   A: Reset Hit Power to Default\n')
        print('Press Space Bar to Reset Game')
        self.right_point = 0
        self.left_point = 0
        self.t = turtle.Turtle()
        turtle.delay(0)
        turtle.tracer(0,0)
        turtle.setworldcoordinates(-500,-500,500,500)
        turtle.setpos(0,0)
        turtle.left(90)
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.setpos(-400,0)
        turtle.pendown()
        turtle.goto(400,0)
        turtle.penup()
        turtle.hideturtle()
        rand_x = random.uniform(-100,100)
        rand_y = random.uniform(30,100)
        rand_int = random.randint (1,2)
        if rand_int == 1:
            rand_vx = random.uniform(-12,-6)
        else:
            rand_vx = random.uniform(6,12)
        rand_vy = random.uniform(4,10)
        self.ball = Ball(x=rand_x, y=rand_y, vx=rand_vx, vy=rand_vy)
        turtle.update()
        self.gameloop()
        turtle.onkeypress(self.ball.right_hit, "Left")
        turtle.onkeypress(self.ball.rightpower_up, "Up")
        turtle.onkeypress(self.ball.rightpower_down, "Down")
        turtle.onkeypress(self.ball.rightpower_reset, "Right")
        turtle.onkeypress(self.ball.left_hit, "d")
        turtle.onkeypress(self.ball.leftpower_up, "w")
        turtle.onkeypress(self.ball.leftpower_down, "s")
        turtle.onkeypress(self.ball.leftpower_reset, "a")
        turtle.onkeypress(self.point_reset, "space")
        turtle.listen()
        turtle.mainloop()
    def point_reset(self):
        self.right_point = 0
        self.left_point = 0
        self.score()
        self.ball.reset()
    def score(self):
        self.t.clear()
        self.t.write(f"{self.left_point}   {self.right_point}", False, align="center")
    def gameloop(self):
        self.t.hideturtle()
        self.score()
        self.ball.move()
        if self.ball.xcor()>=-5 and self.ball.xcor()<=5 and self.ball.ycor()<=32 and self.ball.vx >= 0:
            self.right_point += 1
            self.score()
            self.ball.reset()
        if self.ball.xcor()>=-5 and self.ball.xcor()<=5 and self.ball.ycor()<=32 and self.ball.vx < 0:
            self.left_point += 1
            self.score()
            self.ball.reset()
        if self.ball.xcor()>410 and self.ball.ycor()<10 and self.ball.bounce==0:
            self.right_point += 1
            self.score()
            self.ball.reset()
        if self.ball.xcor()<-410 and self.ball.ycor()<10 and self.ball.bounce==0:
            self.left_point += 1
            self.score()
            self.ball.reset()
        if self.ball.bounce>=2 or self.ball.right_hit_count>=2 or self.ball.left_hit_count>=2:
            if self.ball.xcor() >= 0:
                self.left_point += 1
                self.score()
            if self.ball.xcor() < 0:
                self.right_point += 1
                self.score()
            self.ball.reset()
        turtle.update()
        turtle.ontimer(self.gameloop, 30)

###############################################################################
if __name__ == '__main__':
    Game()
