crates = open("data.txt").read().split("\n\n")[0].split("\n")
columns = {}
print(crates)
for box in crates[:-1]:
        for i in range(1, len(box), 4):
            if box[i] != " ":
                columns.setdefault(i//4 + 1, []).insert(0, box[i])

# for count, value in enumerate(crates):
#     print(count, value)
#     top_box = value[count]
#     crate_position.update({count: column.append(top_box[count-1])})

print(columns)

def move():
    moving_crates = []
    popped_crate = ""
    moving_column = []
    move_list = open("data.txt").read().split("\n\n")[1].split("\n")
    print(move_list)
    for step in move_list:
        if step[6] != " ":
            pass
        else:
            moving_column = columns[(int(step[12]))]
            for i in step[5]:
                popped_crate = moving_column.pop(i)
                moving_crates.append(popped_crate)

            print(moving_crates)

move()
