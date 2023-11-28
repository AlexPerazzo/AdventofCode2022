def make_zeros_matrix(matrix):
    zeros_matrix = []
    trees_in_row = []
    trees_with_zero = []
    count = 0
    for row in matrix:
        for number in row:
            for trees in trees_in_row:
                if number > trees:
                    count += 1
            if count == len(trees_in_row):
                trees_with_zero.append("0")
            else:
                trees_with_zero.append(number)
            trees_in_row.append(number)
            count = 0
        zeros_matrix.append(trees_with_zero)
        trees_with_zero = []
        trees_in_row = []
    
    return zeros_matrix

def make_reverse_matrix(filename):
    reversed_matrix = []
    with open(filename) as file:
        for line in file:
            row = []
            for letter in line:
                letter = letter.strip()
                if letter != "":
                    row.append(letter)
            row.reverse()
            reversed_row = row
            reversed_matrix.append(reversed_row)
    return reversed_matrix

matrix = []
with open("trees.csv") as file:
    for line in file:
        row = []
        for letter in line:
            letter = letter.strip()
            if letter != "":
                row.append(letter)
        matrix.append(row)

def make_rotated_matrix(matrix):
    rotated_matrix = []
    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            letter = matrix[j][i]
            column.append(letter)
        rotated_matrix.append(column)
    return rotated_matrix

# print(rotated_matrix)

# rotated90_matrix = []
# for i in range(len(rotated_matrix[0])):
#     column = []
#     for j in range(len(rotated_matrix)):
#         letter = rotated_matrix[i][j]
#         column.append(letter)
#     rotated90_matrix.append(column)



reversed_matrix = []
with open("trees.csv") as file:
    for line in file:
        row = []
        for letter in line:
            letter = letter.strip()
            if letter != "":
                row.append(letter)
        row.reverse()
        reversed_row = row
        reversed_matrix.append(reversed_row)

def make_rotated_reversed_matrix(reversed_matrix):
    rotated_reversed180_matrix = []
    for i in range(len(reversed_matrix[0])):
        column = []
        for j in range(len(reversed_matrix)):
            letter = reversed_matrix[j][i]
            column.append(letter)
        rotated_reversed180_matrix.append(column)
    return rotated_reversed180_matrix


rotated_matrix = make_rotated_matrix(matrix)

















with open("test1.csv", "wt") as file:
    for row in matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")


with open("test2.csv", "wt") as file:
    for row in rotated_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

rotated_reversed180_matrix = []
with open("test2.csv") as file:
    for line in file:
        row = []
        for letter in line:
            letter = letter.strip()
            if letter != "":
                row.append(letter)
        row.reverse()
        reversed_row = row
        rotated_reversed180_matrix.append(reversed_row)





with open("test3.csv", "wt") as file:
    for row in reversed_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

with open("test4.csv", "wt") as file:
    for row in rotated_reversed180_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")



#reverting back to original
# rotated_matrix = make_rotated_matrix(rotated_matrix)

# rotated_reversed180_matrix = make_rotated_reversed_matrix(rotated_reversed180_matrix)
# with open("test4.csv", "wt") as file:
#     for row in rotated_reversed180_matrix:
#         for letter in row:
#             file.write(letter)
#         file.write("\n")
# rotated_reversed180_matrix = make_reverse_matrix("test4.csv")

# with open("test3.csv", "wt") as file:
#     for row in reversed_matrix:
#         for letter in row:
#             file.write(letter)
#         file.write("\n")

# reversed_matrix = make_reverse_matrix("test3.csv")


rotated_zero_matrix = make_zeros_matrix(rotated_matrix)
rotated_reversed180_zero_matrix = make_zeros_matrix(rotated_reversed180_matrix)
reversed_zero_matrix = make_zeros_matrix(reversed_matrix)

normal_zero_matrix = make_zeros_matrix(matrix)
fixed_rotated_zero_matrix = make_rotated_matrix(rotated_zero_matrix)

rotated_reversed180_zero_matrix = make_rotated_reversed_matrix(rotated_reversed180_zero_matrix)


with open("rotated_reversed_zero_matrix.csv", "wt") as file:
    for row in rotated_reversed180_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")
rotated_reversed180_zero_matrix = make_reverse_matrix("rotated_reversed_zero_matrix.csv")


with open("reversed_zero_matrix.csv", "wt") as file:
    for row in reversed_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

reversed_zero_matrix = make_reverse_matrix("reversed_zero_matrix.csv")

# fixed_rotated_reversed180_zero_matrix = make_rotated_reversed_matrix(rotated_reversed180_zero_matrix)


with open("reversed_zero_matrix.csv", "wt") as file:
    for row in reversed_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")



with open("normal_zero_matrix.csv", "wt") as file:
    for row in normal_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

with open("rotated_zero_matrix.csv", "wt") as file:
    for row in rotated_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

with open("rotated_reversed_zero_matrix.csv", "wt") as file:
    for row in rotated_reversed180_zero_matrix:
        for letter in row:
            file.write(letter)
        file.write("\n")

# fixed_reversed_matrix = []
# with open("reversed_zero_matrix.csv") as file:
#     for line in file:
#         row = []
#         for letter in line:
#             letter = letter.strip()
#             if letter != "":
#                 row.append(letter)
#         row.reverse()
#         reversed_row = row
#         fixed_reversed_matrix.append(reversed_row)