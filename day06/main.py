data = open("data.txt").read()
# print(data)

def find_marker(input):
    for letter in range(len(input)):
        first_letter = input[letter]
        second_letter = input[letter+1]
        third_letter = input[letter+2]
        fourth_letter = input[letter+3]


        # print(f"first letter is {first_letter}")
        # print(f"second letter is {second_letter}")
        # print(f"third letter is {third_letter}")
        # print(f"fourth letter is {fourth_letter}")


        if first_letter != second_letter and first_letter != third_letter and first_letter != fourth_letter:
            if second_letter != third_letter and second_letter != fourth_letter:
                if third_letter != fourth_letter:
                    print(f"The code starts at {letter+4}")
                    break

def find_unique_string(input, number):
    for letter in range(len(input)):
        if len(set(data[letter:(letter+number)])) == number:
            return letter + number

find_marker(data)
print(find_unique_string(data, 14))
