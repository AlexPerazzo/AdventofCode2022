total_points = 0
def return_points(letter, list):
    for i, alphabet_letter in enumerate(list):
        if letter == alphabet_letter:
            points = i + 1
    return points
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open("compartments.csv") as file:
    for line in file:
        compartmentA = []
        compartmentB = []
        length = len(line) - 1
        for i, letter in enumerate(line):
            if i + 1 <= length / 2:
                compartmentA.append(letter)
            if i + 1 > length / 2:
                compartmentB.append(letter)
        for letter in compartmentA:
            if letter in compartmentB:
                shared_letter = letter
                points = return_points(shared_letter, alphabet)
                total_points += points
                break
print(total_points)


