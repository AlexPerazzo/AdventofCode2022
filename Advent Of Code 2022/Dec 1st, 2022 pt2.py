most_calories = 0
total_calories = 0
sec_most_calories = 0
third_most_calories = 0
with open("calories.csv") as file:
    for line in file:
        if line.strip() == "":
            if total_calories > most_calories:
                most_calories = total_calories
            total_calories = 0
        else:
            calories = float(line)
            total_calories = total_calories + calories
with open("calories.csv") as file:
    for line in file:
        if line.strip() == "":
            if (total_calories > sec_most_calories) and (total_calories != most_calories):
                sec_most_calories = total_calories
            total_calories = 0
        else:
            calories = float(line)
            total_calories = total_calories + calories
with open("calories.csv") as file:
    for line in file:
        if line.strip() == "":
            if (total_calories > third_most_calories) and (total_calories != most_calories) and (total_calories != sec_most_calories):
                third_most_calories = total_calories
            total_calories = 0
        else:
            calories = float(line)
            total_calories = total_calories + calories
print(most_calories + sec_most_calories + third_most_calories)

            

