import os

file_path = 'instructions.txt'

def main():
    print("Turtle Parser v1.0 beginning...")
    try:
        file = open(file_path, "r")
        line = file.readline()
        while line:
            parse_instruction(line)
            line = file.readline()
    finally:
        file.close()


def parse_instruction(line):
    actionable = []
    #print(line)
    instructions = line.split(" ")
    if len(instructions) == 0:
        return

    # read through until empty area
    for value in instructions:
        if value != "":
            actionable.append(value)
        else:
            route_instruction(actionable)
            return


def route_instruction(instruction):
    #print(instruction)
    # set "value" if instruction is more than 1 element
    if len(instruction) == 1:
        control = instruction[0]
        value = ""

    if len(instruction) == 2:
        control = instruction[0]
        value = instruction[1]

    # pen control
    if control == "P":
        inst_select_pen(value)

    if control == "D":
        inst_pen_control(control)

    if control == "U":
        inst_pen_control(control)

    # directional
    if control == "N":
        inst_direction("NORTH", value)

    if control == "S":
        inst_direction("SOUTH", value)

    if control == "E":
        inst_direction("EAST", value)

    if control == "W":
        inst_direction("WEST", value)


def inst_select_pen(pen):
    print("PEN SELECTED:", pen)


def inst_pen_control(value):
    if value == 'D':
        print("PEN IS DOWN")
    else:
        print("PEN IS UP")


def inst_direction(direction, distance):
    if distance == "":
        distance = 1

    print("MOVE", direction, distance)


if __name__ == '__main__':
    main()