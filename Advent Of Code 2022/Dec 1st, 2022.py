most_calories = 0
total_calories = 0
with open("calories.csv") as file:
    for line in file:
        if line.strip() == "":
            total_calories = 0
        else:
            calories = float(line)
            total_calories = total_calories + calories
            if total_calories >= most_calories:
                most_calories = total_calories
            print(most_calories)

