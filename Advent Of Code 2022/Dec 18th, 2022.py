x_list = []
y_list = []
z_list = []
total_sides = 0

with open("lavadrops.csv") as file:
    for line in file:
        x, y, z = line.split(",")
        x = int(x)
        y = int(y)
        z = int(z)

        for i in range(len(x_list)):
            if (x + 1 == x_list[i] and y == y_list[i] and z == z_list[i]) or (x - 1 == x_list[i] and y == y_list[i] and z == z_list[i]) or (x == x_list[i] and y + 1 == y_list[i] and z == z_list[i]) or (x == x_list[i] and y - 1 == y_list[i] and z == z_list[i]) or (x == x_list[i] and y == y_list[i] and z + 1 == z_list[i]) or (x == x_list[i] and y == y_list[i] and z - 1 == z_list[i]):
                total_sides -= 2
        
        total_sides += 6

        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
major_count = 0
count = 0
for i in range(25):
    x = i
    for j in range(25):
        y = j
        for k in range(25):
            
            
            z = k

            for l in range(len(x_list)):
                if x == x_list[l] and y == y_list[l] and z == z_list[l]:
                    break
                else:
                    if (x + 1 == x_list[l] and y == y_list[l] and z == z_list[l]):
                        count += 1
                    elif (x - 1 == x_list[l] and y == y_list[l] and z == z_list[l]):
                        count += 1
                    elif (x == x_list[l] and y + 1 == y_list[l] and z == z_list[l]):
                        count += 1
                    elif (x == x_list[l] and y - 1 == y_list[l] and z == z_list[l]):
                        count += 1
                    elif (x == x_list[l] and y == y_list[l] and z + 1 == z_list[l]):
                        count += 1
                    elif (x == x_list[l] and y == y_list[l] and z - 1 == z_list[l]):
                        count += 1

            if count >= 6:
                major_count += 6
                    
            count = 0


print(major_count)
print(total_sides)