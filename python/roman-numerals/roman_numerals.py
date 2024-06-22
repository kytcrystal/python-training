roman_to_arabic = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I" 
   }

special_case = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

def roman(number):
    roman_numeral = ""
    
    if number >= 1000:
        quotient = number // 1000
        roman_numeral += roman_to_arabic[1000] * quotient
        number = number % 1000
    
    if number >= 900:
        roman_numeral += special_case[900]
        number -= 900
        
    if number >= 500:
        quotient = number // 500
        roman_numeral += roman_to_arabic[500] * quotient
        number = number % 500
        
    if number >= 400:
        roman_numeral += special_case[400]
        number -= 400
        
    if number >= 100:
        quotient = number // 100
        roman_numeral += roman_to_arabic[100] * quotient
        number = number % 100
        
    if number >= 90:
        roman_numeral += special_case[90]
        number -= 90
        
    if number > 4:
        roman_numeral += roman_to_arabic[5] 
        
    if number > 0 and number < 4:
        roman_numeral += roman_to_arabic[1] * number
    

        
    return roman_numeral

