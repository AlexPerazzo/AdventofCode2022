#25034834167 is too high
#15410367140 is too low
#1441409144245
#14447318805
#14528323362
#14447559083
#17222154663 is too low
#15410367140

def main():
    monkey0 = [89, 73, 66, 57, 64, 80]
    monkey1 = [83, 78, 81, 55, 81, 59, 69]
    monkey2 = [76, 91, 58, 85]
    monkey3 = [71, 72, 74, 76, 68]
    monkey4 = [98, 85, 84]
    monkey5 = [78]
    monkey6 = [86, 70, 60, 88, 88, 78, 74, 83]
    monkey7 = [81, 58]
    monkey0_count = 0
    monkey1_count = 0
    monkey2_count = 0
    monkey3_count = 0
    monkey4_count = 0
    monkey5_count = 0
    monkey6_count = 0
    monkey7_count = 0
    for i in range(10000):
        monkey0_count, monkey0, monkey6, monkey2 = monkey0_throw(monkey0_count, monkey0, monkey6, monkey2)
        monkey1_count, monkey1, monkey7, monkey4 = monkey1_throw(monkey1_count, monkey1, monkey7, monkey4)
        monkey2_count, monkey2, monkey1, monkey4 = monkey2_throw(monkey2_count, monkey2, monkey1, monkey4)
        monkey3_count, monkey3, monkey6, monkey0 = monkey3_throw(monkey3_count, monkey3, monkey6, monkey0)
        monkey4_count, monkey4, monkey5, monkey7 = monkey4_throw(monkey4_count, monkey4, monkey5, monkey7)
        monkey5_count, monkey5, monkey3, monkey0 = monkey5_throw(monkey5_count, monkey5, monkey3, monkey0)
        monkey6_count, monkey6, monkey1, monkey2 = monkey6_throw(monkey6_count, monkey6, monkey1, monkey2)
        monkey7_count, monkey7, monkey3, monkey5 = monkey7_throw(monkey7_count, monkey7, monkey3, monkey5)
        print(i)

    print(monkey0_count)
    print(monkey2_count)
    print(monkey3_count)
    print(monkey4_count)
    print(monkey5_count)
    print(monkey6_count)
    print(monkey7_count)
    all_monkey = [monkey0_count, monkey1_count, monkey2_count, monkey3_count, monkey4_count, monkey5_count, monkey6_count, monkey7_count]
    biggest = max(all_monkey)
    all_monkey.remove(biggest)
    nd_biggest = max(all_monkey)
    print(biggest * nd_biggest)
    



def monkey0_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    
    for item in monkey0_list:
        value = 3 * item
        while value > 10000000:
            value = value - 9699690

         
        if value % 13 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey1_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 1 + item
        while value > 10000000:
            value = value - 9699690 
        
        if value % 3 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey2_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 13 * item
        while value > 10000000:
            value = value - 9699690

        if value % 7 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey3_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = item * item
        while value > 10000000:
            value = value - 9699690
        
        if value % 2 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey4_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 7 + item
        while value > 10000000:
            value = value - 9699690 

        if value % 19 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey5_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 8 + item
        while value > 10000000:
            value = value - 9699690

        if value % 5 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey6_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 4 + item
        while value > 10000000:
            value = value - 9699690

        if value % 11 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

def monkey7_throw(monkey0_count, monkey0_list, monkey6_list, monkey2_list):
    for item in monkey0_list:
        value = 5 + item
        while value > 10000000:
            value = value - 9699690

        if value % 17 == 0:
            monkey6_list.append(value)
        else:
            monkey2_list.append(value)
        monkey0_count += 1
    monkey0_list.clear()

    return monkey0_count, monkey0_list, monkey6_list, monkey2_list

main()