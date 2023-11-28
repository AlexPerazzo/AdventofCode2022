count = 0
with open("dec4th.csv") as file:
    for line in file:
        both_sections = line.split(sep= ",")
        fullsectionA = both_sections[0]
        fullsectionB = both_sections[1]
        sectionA = fullsectionA.split(sep= "-")
        sectionB = fullsectionB.split(sep= "-")
        sectionA[0] = sectionA[0].strip()
        sectionB[0] = sectionB[0].strip()
        sectionA[1] = sectionA[1].strip()
        sectionB[1] = sectionB[1].strip()
        sectionA[0] = float(sectionA[0])
        sectionB[0] = float(sectionB[0])
        sectionA[1] = float(sectionA[1])
        sectionB[1] = float(sectionB[1])        
        if (sectionA[0] >= sectionB[0]) and (sectionA[1] <= sectionB[1]):
            count += 1
        if (sectionA[0] <= sectionB[0]) and (sectionA[1] >= sectionB[1]):
                count += 1
    print(count)
