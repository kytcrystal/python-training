import math
color_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
tolerances = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%", "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"} 

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    
    band_value = color_codes[colors[0]] * 10 + color_codes[colors[1]]
    
    if len(colors) == 5:
        band_value = band_value * 10 + color_codes[colors[2]]
        
    exponent = color_codes[colors[-2]]
    multiple = len(str(band_value)) - 1
    
    band_value = band_value / math.pow(10,multiple)
    print(band_value)
    exponent += multiple
    
    unit, value = calculate_value_unit(exponent, band_value)
    
    tolerance = tolerances[colors[-1]]
        
    return f"{value} {unit} ±{tolerance}"


def calculate_value_unit(exponent, band_value):
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
    value = band_value * math.pow(10,exponent)
    return unit,value
