from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.text", mode="r") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
        self.increase()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.text",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()