rucksacks = open("input.txt").read().splitlines()
#converting each line into a list item

#dividing each list item in two and finding duplicate letters

test_string = ["AsdfghjklA"]
def check_rucksacks():
    elf_mistake = []
    score = 0
    for item in rucksacks:

        number_of_items_each_side = len(item)/2
        right_side = item[0:int(number_of_items_each_side)]
        left_side = item[int(number_of_items_each_side):]
        r = list(right_side)
        l = list(left_side)
        print(item)
        print(number_of_items_each_side)
        print(right_side)
        print(left_side)

        for letter in r:
            if letter in l:
                elf_mistake.append(letter)
                print(letter)
                break

    # assigning values to letters
    # add up priorities
    for priority in elf_mistake:
        value = ord(priority)
        score += value - 96 if value > 96 else value - 38

    return score

print(f"The priority score is {check_rucksacks()}.")

# def test():
#     elf_mistake = []
#     score = 0
#     for item in test_string:
#
#         number_of_items_each_side = len(item)/2
#         right_side = item[0:int(number_of_items_each_side)]
#         left_side = item[int(number_of_items_each_side):]
#         r = list(right_side)
#         l = list(left_side)
#         print(number_of_items_each_side)
#         print(right_side)
#         print(left_side)
#
#         for letter in r:
#             if letter in l:
#                 elf_mistake.append(letter)
#
#     # assigning values to letters
#     # add up priorities
#     for priority in elf_mistake:
#         value = ord(priority)
#         print(f"value = {value}")
#         score += value - 96 if value > 96 else value - 38
#         print(f"score = {score}")
#
#
#     return score
#
# test()
