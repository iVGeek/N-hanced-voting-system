class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1

    def __str__(self):
        return f"{self.name}: {self.votes} votes"
