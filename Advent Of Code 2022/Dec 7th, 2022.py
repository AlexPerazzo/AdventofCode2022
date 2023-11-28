def do_point_stuff(key1, key2):

            points = directories_dict[key1]
            pieces_points = directories_dict[key2]
            total_points = pieces_points + points
            directories_dict[key1] = total_points
#make a dictionary. Every time a new directory comes up, add it to the dictionary.
#The value of each directory is what is directly in that directory.
#Later iterate through to figure out what directories are in what directories and add the values.

#1417382 is too high
#86399 is too low
#886710 is too low

directories_dict = {}
command = []
overall_count = 0
dir_count = 0
current_name = "/"
list_of_directories = ["/"]


with open("directories.csv") as file:
    next(file)
    for line in file:
        line = line.strip()
        for character in line:
            command.append(character)
        
        if command[0] == "$":
            if command[2] == "c":
                if command[5] == ".":
                    list_of_directories.pop()
                else:
                    current_name = []
                    for i in range(len(command)):
                        if i >= 5:
                            current_name.append(command[i])
                    current_name = "".join(current_name)
                    
                    list_of_directories.append(current_name)
                    dir_count = directories_dict[current_name]
                    dir_count = float(dir_count)

        if command[0] == "d":
            name = []
            for i in range(len(command)):
                
                if i >= 4:
                    name.append(command[i])

            directory_name = "".join(name)
            directories_dict[directory_name] = 0

        if command[0].isdigit() == True:
            file_size_list = []
            for i in range(len(command)):
                if command[i].isdigit():
                    file_size_list.append(command[i])
            file_size = "".join(file_size_list)
            file_size = float(file_size)
            dir_count += file_size
            directories_dict[list_of_directories[-1]] = dir_count


        command = []


#Take old dictionary with all directories. Make a new dictionary replacing all the values with blank lists.

#When adding a new directory, use list_of_directories to check the father directory.

#Use that name as a key to access our new dictionary. Check if any of the values = our directory we are adding.

#If not, add it to the dictionary. If it's already in it, just skip.

#Cycle through this finished new dictionary. Take the values: use them as keys in our old dictionary to get their points
#Add up all those points, update the dictionary. Run it through the <=100000

list_of_directories = ["/"]
new_dict = {}
for key in directories_dict.keys():
    new_dict[key] = []

with open("directories.csv") as file:
    next(file)
    for line in file:
        line = line.strip()
        for character in line:
            command.append(character)

        if command[0] == "$":
            if command[2] == "c":
                if command[5] == ".":
                    list_of_directories.pop()
                else:
                    current_name = []
                    for i in range(len(command)):
                        if i >= 5:
                            current_name.append(command[i])
                    current_name = "".join(current_name)
                    father_directory = list_of_directories[-1]

                    list_of_directories.append(current_name)
                    
                    test_list = new_dict[father_directory]
                    if current_name not in test_list:
                        new_dict[father_directory].append(current_name)
        command = []

total = 0
super_new_dict = {}
for key, value in new_dict.items():
    super_new_dict[key] = value

points = 0
total_points = 0
for value in new_dict["/"]:
    
        if new_dict.get(value):
            for list in new_dict[value]:


                    if new_dict.get(list):
                        for list2 in new_dict[list]:


                                if new_dict.get(list2):
                                    for list3 in new_dict[list2]:


                                            if new_dict.get(list3):
                                                for list4 in new_dict[list3]:


                                                        if new_dict.get(list4):
                                                            for list5 in new_dict[list4]:

                                                                if new_dict.get(list5):
                                                                    for list6 in new_dict[list5]:

                                                                        if new_dict.get(list6):
                                                                            for list7 in new_dict[list6]:

                                                                                if new_dict.get(list7):
                                                                                    for list8 in new_dict[list7]:

                                                                                        if new_dict.get(list8):
                                                                                            for list9 in new_dict[list8]:

                                                                                                if new_dict.get(list9):
                                                                                                    for list10 in new_dict[list9]:

                                                                                                        if new_dict.get(list10):
                                                                                                            for list11 in new_dict[list10]:

                                                                                                                if new_dict.get(list11):
                                                                                                                    for list12 in new_dict[list11]:

                                                                                                                        if new_dict.get(list12):
                                                                                                                            for list13 in new_dict[list12]:

                                                                                                                                points = directories_dict[list11]
                                                                                                                                pieces_points = directories_dict[list12]
                                                                                                                                total_points = pieces_points + points
                                                                                                                                directories_dict[list11] = total_points
                                                                                                                        points = directories_dict[list11]
                                                                                                                        pieces_points = directories_dict[list12]
                                                                                                                        total_points = pieces_points + points
                                                                                                                        directories_dict[list11] = total_points 



                                                                                                                points = directories_dict[list10]
                                                                                                                pieces_points = directories_dict[list11]
                                                                                                                total_points = pieces_points + points
                                                                                                                directories_dict[list10] = total_points       

                                                                                                        points = directories_dict[list9]
                                                                                                        pieces_points = directories_dict[list10]
                                                                                                        total_points = pieces_points + points
                                                                                                        directories_dict[list9] = total_points       

                                                                                                points = directories_dict[list8]
                                                                                                pieces_points = directories_dict[list9]
                                                                                                total_points = pieces_points + points
                                                                                                directories_dict[list8] = total_points       
                                                                                                
                                                                                        points = directories_dict[list7]
                                                                                        pieces_points = directories_dict[list8]
                                                                                        total_points = pieces_points + points
                                                                                        directories_dict[list7] = total_points


                                                                                points = directories_dict[list6]
                                                                                pieces_points = directories_dict[list7]
                                                                                total_points = pieces_points + points
                                                                                directories_dict[list6] = total_points




                                                                        points = directories_dict[list5]
                                                                        pieces_points = directories_dict[list6]
                                                                        total_points = pieces_points + points
                                                                        directories_dict[list5] = total_points




                                                                    points = directories_dict[list4]
                                                                    pieces_points = directories_dict[list5]
                                                                    total_points = pieces_points + points
                                                                    directories_dict[list4] = total_points



                                                        points = directories_dict[list3]
                                                        pieces_points = directories_dict[list4]
                                                        total_points = pieces_points + points
                                                        directories_dict[list3] = total_points




                                            points = directories_dict[list2]
                                            pieces_points = directories_dict[list3]
                                            total_points = pieces_points + points
                                            directories_dict[list2] = total_points



                                points = directories_dict[list]
                                pieces_points = directories_dict[list2]
                                total_points = pieces_points + points
                                directories_dict[list] = total_points


                    points = directories_dict[value]
                    pieces_points = directories_dict[list]
                    total_points = pieces_points + points
                    directories_dict[value] = total_points


        points = directories_dict["/"]
        pieces_points = directories_dict[value]
        total_points = pieces_points + points
        directories_dict["/"] = total_points


for key, value in directories_dict.items():

    if value <= 100000:
        overall_count += value
total = 0

print()
print()
# print(directories_dict)
print(overall_count)




# while len(super_new_dict) != 0:
#     for old_key, value in new_dict.items():
#         if len(value) == 0:
#             pieces_points = directories_dict[old_key]
#             for newkey, newvalue in new_dict.items():
#                 if old_key in newvalue:
#                     super_new_dict[newkey].remove(old_key)
#                     points = directories_dict[newkey]
#                     points += pieces_points
#                     directories_dict[newkey] = points
#             super_new_dict.pop(old_key)

#     new_dict = {}
#     for key, value in super_new_dict.items():
#         new_dict[key] = value