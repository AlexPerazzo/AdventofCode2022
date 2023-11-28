#2183 is too high
def main():
    score = 0
    print()

    matrix = create_base_matrix("trees.csv")
    write_a_file("base_matrix.csv", matrix)

    reverse_matrix = make_reverse_matrix("base_matrix.csv")
    write_a_file("reverse_matrix.csv", reverse_matrix)

    rotated_matrix = make_rotated_matrix(matrix)
    write_a_file("rotated_matrix.csv", rotated_matrix)

    rotated_reverse_matrix = make_rotated_reversed_matrix("rotated_matrix.csv")
    write_a_file("rotated_reverse_matrix.csv", rotated_reverse_matrix)

    zero_matrix = make_zeros_matrix(matrix)
    write_a_file("zero_base_matrix.csv", zero_matrix)
    z_m = create_base_matrix("zero_base_matrix.csv")

    zero_reverse_matrix = make_zeros_matrix(reverse_matrix)
    write_a_file("zero_reverse_matrix.csv", zero_reverse_matrix)
    fixed_zero_reverse_matrix = make_reverse_matrix("zero_reverse_matrix.csv")
    write_a_file("zero_reverse_matrix.csv", fixed_zero_reverse_matrix)    
    z_re_m = create_base_matrix("zero_reverse_matrix.csv")

    zero_rotated_matrix = make_zeros_matrix(rotated_matrix)
    fixed_zero_rotated_matrix = make_rotated_matrix(zero_rotated_matrix)
    write_a_file("zero_rotated_matrix.csv", fixed_zero_rotated_matrix)
    z_ro_m = create_base_matrix("zero_rotated_matrix.csv")

    zero_rotated_reverse_matrix = make_zeros_matrix(rotated_reverse_matrix)
    write_a_file("temp1.csv", zero_rotated_reverse_matrix)
    rev_zero_rotated_reverse_matrix = make_reverse_matrix("temp1.csv")
    fixed_zero_rotated_reverse_matrix = make_rotated_matrix(rev_zero_rotated_reverse_matrix)
    write_a_file("zero_rotated_reverse_matrix.csv", fixed_zero_rotated_reverse_matrix)
    z_ro_re_m = create_base_matrix("zero_rotated_reverse_matrix.csv")

    
    for i in range(len(z_m)):
        for j in range(len(z_m)):
            if z_m[i][j] == "-" or z_re_m[i][j] == "-" or z_ro_m[i][j] == "-" or z_ro_re_m[i][j] == "-":
                score += 1

    print(score)


def make_zeros_matrix(matrix):
    zeros_matrix = []
    trees_in_row = []
    trees_with_zero = []
    count = 0
    for row in matrix:
        for number in row:
            for trees in trees_in_row:
                if int(number) > int(trees):
                    count += 1
            if count == len(trees_in_row):
                trees_with_zero.append("-")
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

def create_base_matrix(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            row = []
            for letter in line:
                letter = letter.strip()
                if letter != "":
                    row.append(letter)
            matrix.append(row)
    return matrix

def make_rotated_matrix(matrix):
    rotated_matrix = []
    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            letter = matrix[j][i]
            column.append(letter)
        rotated_matrix.append(column)
    return rotated_matrix

def write_a_file(filename, matrix):
    with open(filename, "wt") as file:
        for row in matrix:
            for letter in row:
                file.write(letter)
            file.write("\n")

def make_rotated_reversed_matrix(fileofrotatedmatrix):
    rotated_reverse_matrix = make_reverse_matrix(fileofrotatedmatrix)
    return rotated_reverse_matrix



main()