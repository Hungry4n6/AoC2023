calibration_values = []
calibration_values_2 = []
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_mappings = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9" 
}

with open("1.txt", "r") as f:
    first = "0"
    last = "0"
    for line in f:
        for char in line:
            if char in digits:
                first = char
                break
        for char in line[::-1]:
            if char in digits:
                last = char
                break
        calibration_value = int(first + last)
        calibration_values.append(calibration_value)

    print(sum(calibration_values))
    
with open("1.txt", "r") as f:
    for line in f:
        line_digits = []
        for k,v in enumerate(line):
            #print(f"{k}: {line[k::]}")
            for digit_word in digit_mappings.keys():
                if line[k::].startswith(digit_word):
                    line_digits.append(digit_mappings[digit_word])
            if v in digits:
                line_digits.append(v)
        if len(line_digits) >= 2:
            calibration_values_2.append(int(line_digits[0] + line_digits[-1]))
        else:
            calibration_values_2.append(int(line_digits[0] + line_digits[0]))
    print(sum(calibration_values_2))
