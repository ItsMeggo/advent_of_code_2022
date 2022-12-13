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

def top_3_elves():
    top_calories =[0,0,0]
    current_calories = 0
    for item in calories_list:

        if item == "":
            current_calories = 0

        else:
            current_calories += int(item)

        if current_calories > min(top_calories):
            top_calories.sort()
            top_calories[0] = (current_calories)

    print(top_calories)
    top_three_total = sum(top_calories)

    return top_three_total


highest_calories_answer = find_highest_calories()
print(f"highest calories is {highest_calories_answer}")

top_3_answer = top_3_elves()
print(f"Top 3 total is {top_3_answer}")
