digits = {"0": 0, "1": 3, "2": 3, "3": 5, "4": 4, "5": 4, "6": 3, "7": 5, "8": 5, "9": 4}
tens = {"0": 0, "2": 6, "3": 6, "4": 5, "5": 5, "6": 5, "7": 7, "8": 6, "9": 6}
sonder = {"0": 3, "1": 6, "2": 6, "3": 8, "4": 8, "5": 7, "6": 7, "7": 9, "8": 8, "9": 8}
hundred = 10
result = 0
for number in range(1000):
    digit = str(number)
    if len(digit) == 3:
        result += hundred
        result += digits[digit[0]]
        if digit[1] == "1":
            result += sonder[digit[2]]
        else:
            result += tens[digit[1]]
            result += digits[digit[2]]
    elif len(digit) == 2:
        if digit[0] == "1":
            result += sonder[digit[1]]
        else:
            result += tens[digit[0]]
            result += digits[digit[1]]
    else:
        result += digits[digit[0]]
result += 11
result -= (9 * 3)
print(result)
