all_pieces_moving = []
allstacks = [["G", "P", "N", "R"], ["H", "V", "S", "C", "L", "B", "J", "T"], ["L", "N", "M", "B", "D", "T"], ["B", "S", "P", "V", "R"], ["H", "V", "M", "W", "S", "Q", "C", "G"], ["J", "B", "D", "C", "S", "Q", "W"], ["L", "Q", "F"], ["V", "F", "L", "D", "T", "H", "M", "W"], ["F", "J", "M", "V", "B", "P", "L"]]
with open("cratemovement.csv") as file:
    for line in file:
        allparts = line.split(" ")
        allparts.pop(0)
        allparts.pop(1)
        allparts.pop(2)
        from_stack = int(allparts[1]) - 1
        to_stack = int(allparts[2].strip()) - 1
        for i in range(int(allparts[0])):
            piece_moving = allstacks[from_stack].pop(0)
            all_pieces_moving.insert(0, piece_moving)
        for i in range(len(all_pieces_moving)):
            allstacks[to_stack].insert(0, all_pieces_moving[i])
        all_pieces_moving = []
for i in range(9):
    print(allstacks[i][0], end="")