def return_points(letter):
    if letter == "A" or letter == "X":
        points = 1
    if letter == "B" or letter == "Y":
        points = 2
    if letter == "C" or letter == "Z":
        points = 3
    return points
total_points = 0
with open("rps.csv") as file:
    for line in file:
        parts = line.split(" ")
        parts[0] = return_points(parts[0])
        parts[1] = return_points(parts[1].strip())
        A = 1; B = 2; C = 3; X = 1; Y = 2; Z = 3
        if parts[0] + 1 == parts[1] or (parts[0] - 2 == parts[1]):
            total_points = total_points + 6 + parts[1]
        elif parts[0] == parts[1] + 1 or (parts[0] == parts[1] - 2):
            total_points = total_points + parts[1]
        elif parts[0] == parts[1]:
            total_points = total_points + parts[1] + 3
print(total_points)

