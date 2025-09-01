class Quiz():
    from Day17_Questions import question_data
    def __init__(self):
        self.score = 0
    def ask(self):
        for Q in self.question_data:
            ans=input(Q["text"])
            if ans == Q["answer"]:
                print("Good")
                self.score += 1
                print("Your score is:", self.score)
            else:
                print("Bad answer")
                print("Your score is:", self.score)
s1=Quiz()
s1.ask()

