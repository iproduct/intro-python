class Answer:
    def __init__(self, text=None, points:int=0, id: str=None):
        self.id = id
        self.text = text
        self.points = points
    def __str__(self):
        return f'{self.text}: {self.points} points'