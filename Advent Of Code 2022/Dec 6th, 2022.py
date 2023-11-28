code = []
count = 0
with open("dec6th.csv") as file:
    for line in file:
        for letter in line:
            code.append(letter)
            count += 1
            if len(code) == 14:
                if len(set(code)) == len(code):
                    print(count)
                else:
                    code.pop(0)