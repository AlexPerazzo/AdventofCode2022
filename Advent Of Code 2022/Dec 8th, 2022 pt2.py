#2183 is too high
def main():
    
    print()

    matrix = create_base_matrix("trees.csv")
    write_a_file("base_matrix.csv", matrix)

    reverse_matrix = make_reverse_matrix("base_matrix.csv")
    write_a_file("reverse_matrix.csv", reverse_matrix)

    rotated_matrix = make_rotated_matrix(matrix)
    write_a_file("rotated_matrix.csv", rotated_matrix)

    rotated_reverse_matrix = make_rotated_reversed_matrix("rotated_matrix.csv")
    write_a_file("rotated_reverse_matrix.csv", rotated_reverse_matrix)

    right_dict = make_point_dict(matrix)
    left_dict = make_point_dict(reverse_matrix)
    top_dict = make_point_dict(rotated_matrix)
    bottom_dict = make_point_dict(rotated_reverse_matrix)

    right_matrix = make_matrix_from_dict(right_dict, matrix)
    write_a_file("right_matrix.csv", right_matrix)





    # total_score = 0
    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         total_score = int(right_dict[f"{i},{j}"]) * int(left_dict[f"{i},{j}"]) * int(top_dict[f"{i},{j}"]) * int(bottom_dict[f"{i},{j}"])
    #         print(total_score)

def make_matrix_from_dict(dict, anymatrix):
    matrix = []
    row = []
    for i in range(len(anymatrix)):
        
        for key in dict.keys():
            both_keys = key.split(",")
            if int(both_keys[0]) == i:
                # part = [both_keys[0], both_keys[1]]
                row.append(f"{key} ")
        matrix.append(row)
        row = []
    
    return matrix



def make_point_dict(matrix):
    score = 0
    all_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if k > j:
                    if int(matrix[i][j]) > int(matrix[i][k]):
                        score += 1
                    if int(matrix[i][j]) <= int(matrix[i][k]):
                        score += 1
                        all_dict[f"{i},{j}"] = score
                        score = 0
                        break
                elif j == 98:
                    all_dict[f"{i},{j}"] = 0

                        
    return all_dict


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

def make_new_rotated_matrix(matrix):
    rotated_matrix = []
    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            letter = matrix[j][i]
            column.append(letter)
        rotated_matrix.append(column)
    return rotated_matrix

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