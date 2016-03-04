file = open('Test1.txt')

allowed_chars = "1234567890X"

for line in file:
    line = line.strip()
    code = ''.join(char for char in line if char in allowed_chars)
    if len(code) != 10:
        isValid = False
    else:
        digits = code[0:9]
        check = code[9]
        if check == "X":
            check = "10"
        if "X" in digits:
            isValid = False
        else:
            calc = 0
            for posn in range(0,9):
                calc = calc + int(digits[posn])*(posn + 1)
            rem = calc % 11
            isValid = (rem == int(check))

    if isValid:
        print(line,"is a valid ISBN")
    else:
        print(line,"is not a valid ISBN")

file.close()
                    
    
