calories_list = open("input_1.txt").read().splitlines()
#converting each line into a list item

def find_highest_calories():
    highest_calories = 0
    current_calories = 0
    for item in calories_list:

        if item == "":
            current_calories = 0

        else:
            current_calories += int(item)

        if current_calories > highest_calories:
            highest_calories = current_calories

    return highest_calories

answer = find_highest_calories()
print(f"highest calories is {answer}")
