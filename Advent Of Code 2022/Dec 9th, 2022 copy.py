def where_to_move(head, tail, real_tail):
    if (head - tail == 0) or (head - tail == 999) or (head - tail == 1000) or (head - tail == 1001) or (head - tail == 1) or (head - tail == -999) or (head - tail == -1000) or (head - tail == -1001) or (head - tail == -1):
        pass

    elif (head - tail == 2):
        tail += 1

    elif (head - tail == -998):
        tail -= 999

    elif (head - tail == -1999):
        tail -= 999

    elif (head - tail == -2000):
        tail -= 1000

    elif (head - tail == -2001):
        tail -= 1001

    elif (head - tail == -1002):
        tail -= 1001

    elif (head - tail == -2):
        tail -= 1

    elif (head - tail == 998):
        tail += 999

    elif (head - tail == 1999):
        tail += 999

    elif (head - tail == 2000):
        tail += 1000

    elif (head - tail == 2001):
        tail += 1001

    elif (head - tail == 1002):
        tail += 1001 



    return tail              



tail_places = [0]
all_tails = [0,0,0,0,0,0,0,0,0,0]
with open("dec9th.csv") as file:
    for line in file:
        parts = line.split(" ")
        direction = parts[0]
        how_far = int(parts[1].strip())

        for i in range(how_far):
            if direction == "U":
                all_tails[0] += 1000

            elif direction == "D":
                all_tails[0] -= 1000

            elif direction == "L":
                all_tails[0] -= 1

            elif direction == "R":
                all_tails[0] += 1

            for i in range(len(all_tails)-1):
                all_tails[i+1] = where_to_move(all_tails[i],all_tails[i+1],all_tails[9])
                if all_tails[9] not in tail_places:
                    tail_places.append(all_tails[1])




how_many = len(tail_places)
print(how_many)