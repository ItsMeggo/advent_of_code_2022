chores_list = open("input.txt").read().split("\n")

def check_tasks_inside():
    inside_counter = 0
    for item in chores_list:
        first, second = item.split(",")
        first = [int(i) for i in first.split("-")]
        second = [int(i) for i in second.split("-")]
        # formatting data to be easier to work with

        # print(item)
        # print(f"elf one has {first[0]} to {first[1]} and elf two has {second[0]} to {second[1]} ")

        if (first[0] <= second[0] and first[1] >= second[1]) or ((second[0] <= first[0] and second[1] >= first[1])):
            inside_counter += 1
            # print("inside")
            # checking if tasks inside eachother

    print(f"The number of tasks inside paired tasks is {inside_counter}")


def check_tasks_overlap():
    overlap_counter = 0
    for item in chores_list:

        first, second = item.split(",")
        first = [int(i) for i in first.split("-")]
        second = [int(i) for i in second.split("-")]
        # formatting data to be easier to work with

        # print(item)
        # print(f"elf one has {first[0]} to {first[1]} and elf two has {second[0]} to {second[1]} ")

        if (first[0] <= second[0] and first[1] >= second[0]) and ((first[0] <= second[1] and first[1] <= second[1])):
            overlap_counter += 1
            # print("overlap first method")
        elif (first[0] >= second[0] and first[1] >= second[0]) and ((first[0] <= second[1] and first[1] >= second[1])):
            overlap_counter += 1
            # print("overlap second method")
        elif (first[0] >= second[0] and first[1] >= second[0]) and ((first[0] <= second[1] and first[1] <= second[1])):
            overlap_counter += 1
            # print("overlap fourth method")
        elif (first[0] <= second[0] and first[1] >= second[0]) and ((first[0] <= second[1] and first[1] >= second[1])):
            overlap_counter += 1
            # print("overlap fourth method")
            # checking if tasks overlap
        else:
            # print("no overlap")
            pass

    print(f"The number of tasks overlapping is {overlap_counter}")


check_tasks_inside()
check_tasks_overlap()




