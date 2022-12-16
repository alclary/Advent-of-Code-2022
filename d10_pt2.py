def input_to_CRT(file_name):
    cycle = 0
    reg_x = 1

    def sprite_array(reg_x):
        sprite_array = [reg_x-1, reg_x, reg_x+1]
        return sprite_array

    def draw_pixel():
        nonlocal cycle
        # reset cycle count and print newline every 40 characters
        if cycle != 0 and cycle % 40 == 0:
            cycle = 0
            print()

        if cycle in sprite_array(reg_x):
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        return

    with open(file_name, 'r') as infile:
        for line in infile:
            instruction = line.strip().split(' ')
            if len(instruction) == 2: # addx instruction
                for _ in range(2): draw_pixel()
                reg_x += int(instruction[1])
            else:
                draw_pixel()
    return

if __name__ == '__main__':
    # Day 10 Part 2
    input_to_CRT('input\d10_input.txt')