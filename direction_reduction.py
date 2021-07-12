corresponding_directions = {
    ('NORTH', 'SOUTH'),
    ('SOUTH', 'NORTH'),
    ('EAST', 'WEST'),
    ('WEST', 'EAST'),
}


def cut_direction(directions):
    for i in range(1, len(directions)):
        x = directions[i], directions[i - 1]
        if x in corresponding_directions:
            directions[i], directions[i - 1] = None, None
        elif None in x:
            continue

    new_directions = [direction for direction in directions if direction is not None]

    if validate(new_directions):
        return cut_direction(new_directions)
    else:
        return new_directions


def validate(directions: list):
    for i in range(1, len(directions)):
        x = directions[i], directions[i - 1]
        if x in corresponding_directions:
            return True
    else:
        return False


print(
    cut_direction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
)
