digits = {"0": 0, "1": 3, "2": 2, "3": 5, "4": 4, "5": 4, "6": 3, "7": 5, "8": 5, "9": 4}
tens = {"0": 0, "2": 6, "3": 6, "4": 5, "5": 5, "6": 5, "7": 7, "8": 6, "9": 6}
sonder = {"0": 3, "1": 6, "2": 6, "3": 8, "4": 8, "5": 7, "6": 7, "7": 9, "8": 8, "9": 8}
hundred = 10
sum = 0
for number in range(1, 1000):
    digit = str(number)
    if len(digit) == 3:
        sum += hundred
        sum += digits[digit[0]]
        if digit[1] == "1":
            sum += sonder[digit[2]]
        else:
            sum += tens[digit[1]]
            sum += digits[digit[2]]
    elif len(digit) == 2:
        if digit[0] == "1":
            sum += sonder[digit[1]]
        else:
            sum += tens[digit[0]]
            sum += digits[digit[1]]
    else:
        sum += digits[digit[0]]
sum += 11
sum -= (9 * 3)
print(sum)
