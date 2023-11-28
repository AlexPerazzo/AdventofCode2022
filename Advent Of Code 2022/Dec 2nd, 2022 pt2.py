def return_points(letter):
    points = 0
    if letter == "A" or letter == "X":
        points = 1
    if letter == "B" or letter == "Y":
        points = 2
    if letter == "C" or letter == "Z":
        points = 3
    return points
def what_to_throw(them, you):
    throw = 0
    if you == "X":
        if them == 1:
            throw = them + 2
        else:
            throw = them - 1
    elif you == "Y":
        throw = them
    elif you == "Z":
        if them == 3:
            throw = them - 2
        else:
            throw = them + 1
    return throw
total_points = 0
with open("rps.csv") as file:
    for line in file:
        parts = line.split(" ")
        parts[0] = return_points(parts[0])
        #parts[1] = return_points(parts[1])
        you_throw = what_to_throw(parts[0], parts[1].strip())
        if parts[0] + 1 == you_throw or (parts[0] - 2 == you_throw):
            total_points = total_points + 6 + you_throw
        elif parts[0] == you_throw + 1 or (parts[0] == you_throw - 2):
            total_points = total_points + you_throw
        elif parts[0] == you_throw:
            total_points = total_points + you_throw + 3
print(total_points)

