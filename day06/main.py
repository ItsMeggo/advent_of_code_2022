data = open("data.txt").read()
print(data)

for letter in range(len(data)):
    first_letter = data[letter]
    second_letter = data[letter+1]
    third_letter = data[letter+2]
    fourth_letter = data[letter+3]


    print(f"first letter is {first_letter}")
    print(f"second letter is {second_letter}")
    print(f"third letter is {third_letter}")
    print(f"fourth letter is {fourth_letter}")


    if first_letter != second_letter and first_letter != third_letter and first_letter != fourth_letter:
        if second_letter != third_letter and second_letter != fourth_letter:
            if third_letter != fourth_letter:
                print(f"The code starts at {letter+3}")
                break
