chores_list = open("input.txt").read().split("\n")

inside_counter = 0

for item in chores_list:
    first, second = item.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]
    # formatting data to be easier to work with

    print(item)
    print(f"elf one has {first[0]} to {first[1]} and elf two has {second[0]} to {second[1]} ")

    if (first[0] <= second[0] and first[1] >= second[1]) or ((second[0] <= first[0] and second[1] >= first[1])):
        inside_counter += 1
        print("inside")
        print(f"total inside: {inside_counter}")
        #checking if tasks overlap

print(inside_counter)
