def vacuum_cleaner(room, position):
    if room[position] == 1:
        return "Suck"
    elif position == 0:
        return "Right"
    elif position == 1:
        return "Straight"
    elif position == 2:
        return "Straight"
    elif position == 3:
        return "Left"
    else:
        return "No Operation"


rooms = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

room_no = 1

for room in rooms:
    left_initial = sum(room[:2])
    right_initial = sum(room[2:])
    left_cleaned = 0
    right_cleaned = 0

    position = 0
    while position < 4:
        action = vacuum_cleaner(room, position)

        if action == "Suck":
            room[position] = 0
            if position < 2:
                left_cleaned += 1
            else:
                right_cleaned += 1
        elif action in ["Right", "Straight", "Left"]:
            position += 1
        else:
            break

    left_performance = (left_cleaned / left_initial) * 100
    right_performance = (right_cleaned / right_initial) * 100
    total_performance = (left_performance + right_performance) / 2

    print(f"Room {room_no} cleaned array:", room)
    print(f" Left Performance : {left_performance:.2f}%")
    print(f" Right Performance: {right_performance:.2f}%")
    print(f" Total Performance: {total_performance:.2f}%\n")

    room_no += 1
