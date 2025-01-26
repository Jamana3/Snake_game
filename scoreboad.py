from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 230)
        self.pendown()
        self.write(f"score : {self.score}", False, "center", ("Verdana", 12, "normal"))
        with open("highscore.txt", "rt") as f:
            data = f.read()
        self.Highscore = int(data)
        self.penup()
        self.hideturtle()
        self.goto(50, 230)
        self.pendown()
        self.write(f"high score : {self.Highscore}", False, "center", ("Verdana", 12, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-50, 230)
        self.pendown()
        self.write(f"score : {self.score}", False, "center", ("Verdana", 12, "normal"))
        self.penup()
        self.hideturtle()
        self.goto(50, 230)
        self.pendown()
        if self.score >= self.Highscore:
            self.Highscore = self.score
            with open("highscore.txt", "wt") as f:
                f.write(str(self.score))
        self.write(f"Highscore : {self.Highscore}", False, "center", ("Verdana", 12, "normal"))

    def game_over(self):
        timmy = Turtle()
        timmy.color("white")
        timmy.write("{Ooo game over}", False, "center", ("Verdana", 12, "normal"))
