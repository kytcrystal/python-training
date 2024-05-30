planets_orbital = {"Mercury": 0.2408467, "Venus": 0.61519726, 
                   "Mars": 1.8808158, "Jupiter": 11.862615, 
                   "Saturn": 29.447498, "Uranus": 84.016846, 
                   "Neptune": 164.79132}

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        age = self.seconds / 31557600
        return float("{:.2f}".format(age))

    def on_planet(self, orbital):
        age = self.seconds / (31557600 * orbital)
        return float("{:.2f}".format(age))
    
    def on_mercury(self):
        return self.on_planet(planets_orbital["Mercury"])

    def on_venus(self):
        return self.on_planet(planets_orbital["Venus"])
    
    def on_mars(self):
        return self.on_planet(planets_orbital["Mars"])
    
    def on_jupiter(self):
        return self.on_planet(planets_orbital["Jupiter"])
    
    def on_saturn(self):
        return self.on_planet(planets_orbital["Saturn"])
    
    def on_uranus(self):
        return self.on_planet(planets_orbital["Uranus"])
    
    def on_neptune(self):
        return self.on_planet(planets_orbital["Neptune"])