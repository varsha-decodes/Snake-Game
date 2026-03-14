from turtle import Turtle
ALIGNMENT  = "center"
FONT = ("Arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.pu()
        with open("data.txt",'r') as file:
            self.highest_score = int(file.read())
        self.current_score = 0
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.current_score}, Highest score: {self.highest_score}",False,ALIGNMENT,font=FONT)
        self.current_score += 1

    def reset_board(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
        self.current_score = 0
        with open("data.txt",'w') as wfile:
            wfile.write(str(self.highest_score))
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, ALIGNMENT, font=FONT)