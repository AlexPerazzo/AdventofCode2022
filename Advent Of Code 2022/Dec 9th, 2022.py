

tail_places = ["0"]
tail = 0
head = 0
with open("dec9th.csv") as file:
    for line in file:
        parts = line.split(" ")
        direction = parts[0]
        how_far = int(parts[1].strip())

        for i in range(how_far):
            if direction == "U":
                head += 1

            elif direction == "D":
                head -= 1

            elif direction == "L":
                head -= .001

            elif direction == "R":
                head += .001


            if (head - tail == 0) or (head - tail == .999) or (head - tail == 1) or (head - tail == 1.001) or (head - tail == .001) or (head - tail == -.999) or (head - tail == -1) or (head - tail == -1.001) or (head - tail == -.001):
                None

            elif (head - tail == .002):
                tail += .001
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -.998):
                tail -= .999
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -1.999):
                tail -= .999
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -2):
                tail -= 1
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -2.001):
                tail -= 1.001
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -1.002):
                tail -= 1.001
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == -.002):
                tail -= .001
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == .998):
                tail += .999
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == 1.999):
                tail += .999
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == 2):
                tail += 1
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == 2.001):
                tail += 1.001
                if tail not in tail_places:
                    tail_places.append(tail)
            elif (head - tail == 1.002):
                tail += 1.001 
                if tail not in tail_places:
                    tail_places.append(tail)              

how_many = len(tail_places)
print(how_many)
