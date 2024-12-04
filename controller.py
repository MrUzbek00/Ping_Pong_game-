from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.goto(position)
        self.color("red")
        self.penup()
        self.resizemode(rmode="user")
    
    
        

    def go_up(self):
        y = self.ycor() 
        if y < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)
    def go_down(self):
        y = self.ycor()
        if y > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)

