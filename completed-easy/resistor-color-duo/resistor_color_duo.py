color_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def value(colors):
    band_value = ""
    for band in colors[0:2]:
        band_value += str(color_codes[band])
    return int(band_value)
