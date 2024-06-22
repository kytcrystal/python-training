roman_to_arabic = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I" 
   }


def roman(number):
    roman_numeral = ""
    
    for index, key in enumerate(roman_to_arabic):
        if number >= key:
        
            if index % 2 == 0:
                number, roman_numeral = convert_number(number, roman_numeral, key)
            
            if index % 2 == 1:
                number, roman_numeral = convert_special(number, roman_numeral, key)

    return roman_numeral


def convert_special(number, roman_numeral, special):
    roman_numeral += roman_to_arabic[special]
    number -= special
    return number, roman_numeral

def convert_number(number, roman_numeral, factor):
    quotient = number // factor
    roman_numeral += roman_to_arabic[factor] * quotient
    number = number % factor
    return number, roman_numeral

