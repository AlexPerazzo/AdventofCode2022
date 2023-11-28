
def write_thing(time, counter, count):
    
    with open("plz.csv", "at") as file:
        if time <= 40:
            if (counter + 1 == time) or (counter - 1 == time) or (counter == time):
                file.write("#")
            else:
                file.write(".")

        elif time <= 80:
            if count == 0:
                file.write("\n")
                count += 1
            if (counter + 1 == time - 40) or (counter - 1 == time - 40) or (counter == time - 40):
                file.write("#")
            else:
                file.write(".")

        elif time <= 120:
            if count == 1:
                file.write("\n")
                count += 1
            if (counter + 1 == time - 80) or (counter - 1 == time - 80) or (counter == time - 80):
                file.write("#")
            else:
                file.write(".")

        elif time <= 160:
            if count == 2:
                file.write("\n")
                count += 1
            if (counter + 1 == time - 120) or (counter - 1 == time - 120) or (counter == time - 120):
                file.write("#")
            else:
                file.write(".")

        elif time <= 200:
            if count == 3:
                file.write("\n")
                count += 1
            if (counter + 1 == time - 160) or (counter - 1 == time - 160) or (counter == time - 160):
                file.write("#")
            else:
                file.write(".")

        elif time <= 240:
            if count == 4:
                file.write("\n")
                count += 1
            if (counter + 1 == time - 200) or (counter - 1 == time - 200) or (counter == time - 200):
                file.write("#")
            else:
                file.write(".")

    return count



        
#7420 is too low
#10440 is too low
#11160 is too low

time = 0
counter = 1
total_points = []
count = 0

with open("dec10th.csv") as file:
    for line in file:
        parts = line.split(" ")
        if parts[0].strip() == "noop":
            time += 1
            count = write_thing(time, counter, count)
            if time in [20, 60, 100, 140, 180, 220]:
                points = time * counter
                total_points.append(points)            


        if parts[0] == "addx":
            add = int(parts[1])
            time += 1
            count = write_thing(time, counter, count)
            if time in [20, 60, 100, 140, 180, 220]:
                points = time * counter
                total_points.append(points)

            time += 1
            
            

            if time in [20, 60, 100, 140, 180, 220]:
                points = time * counter
                total_points.append(points)

            counter += add
            count = write_thing(time, counter, count)

grand_total = 0
for point in total_points:
    grand_total += point

print(grand_total)




def how_many_points(time, counter):
    points = time * counter

    return points

        
