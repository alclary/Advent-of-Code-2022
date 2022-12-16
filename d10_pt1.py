def cycle_calculator(file_name):
    cycles = {20:None, 60:None, 100:None, 140:None, 180:None, 220:None}
    cycle = 0
    reg_x = 1

    def increment_cycle():
        nonlocal cycle
        cycle += 1
        if cycle in cycles:
            cycles[cycle] = reg_x

    with open(file_name, 'r') as infile:
        for line in infile:
            instruction = line.strip().split(' ')
            if len(instruction) == 2: # addx instruction
                for _ in range(2): increment_cycle()
                reg_x += int(instruction[1])
            else:
                increment_cycle()
    return cycles

if __name__ == '__main__':
    # Day 10 Part 1
    cycle_dict = cycle_calculator('input\d10_input.txt')
    for key, value in cycle_dict.items():
        cycle_dict[key] = key * value
    print("Signal strength sum:", sum(cycle_dict.values()))