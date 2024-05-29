class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        age = self.seconds / 31557600
        return float("{:.2f}".format(age))
