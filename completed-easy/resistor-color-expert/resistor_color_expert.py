import math
color_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
tolerances = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%", "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"} 

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    
    *bands, exponent, tolerance = colors
    band_value = 0
    for band in bands:
        band_value = band_value * 10 + color_codes[band]
    band_value = band_value * math.pow(10,color_codes[exponent])
    
    unit, value = calculate_value_unit(band_value)
    
    return f"{value:n} {unit} ±{tolerances[tolerance]}"


def calculate_value_unit(band_value):
    digit_length = len(str(int(band_value)))
    units = {9:"gigaohms", 6: "megaohms", 3: "kiloohms"}
    for multiple in units:
        if digit_length > multiple:
            return units[multiple], (band_value / math.pow(10,multiple))
        
    return "ohms", band_value
