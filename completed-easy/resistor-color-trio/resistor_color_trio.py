import math

color_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    band_value = ""
    for band in colors[0:2]:
        band_value += str(color_codes[band])
        
    if colors[1] == "black":
        exponent = 1
        band_value = band_value[0]
    else:
        exponent = 0
        
    exponent += color_codes[colors[2]]
    if exponent == 9:
        exponent = 0
        unit = "gigaohms"
    elif exponent >= 6:
        exponent -= 6
        unit = "megaohms"
    elif exponent >= 3:
        exponent -= 3
        unit = "kiloohms"
    else:
        unit = "ohms"
    value = int(int(band_value) * math.pow(10,exponent))
        
    return f"{value} {unit}"
