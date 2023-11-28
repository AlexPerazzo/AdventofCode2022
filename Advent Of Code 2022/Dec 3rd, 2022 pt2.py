total_points = 0
def return_points(letter, list):
    for i, alphabet_letter in enumerate(list):
        if letter == alphabet_letter:
            points = i + 1
    return points
compartmentC = []
compartmentA = []
compartmentB = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open("compartments.csv") as file:
    for i, line in enumerate(file):
        i = i + 1
        if i % 3 == 1:
            compartmentA = line
        if i % 3 == 2:
            compartmentB = line
        if i % 3 == 0:
            compartmentC = line
        for letter in compartmentA:
            if letter in compartmentB:
                if letter in compartmentC:
                    shared_letter = letter
                    points = return_points(shared_letter, alphabet)
                    total_points += points
                    break
        if len(compartmentC) != 0:
            compartmentC = []
            compartmentA = []
            compartmentB = []
print(total_points)


