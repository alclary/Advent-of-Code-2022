def cargo_reorg_pt1(cargo, file_name):
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip().split(' ')
            steps = int(line[1])
            frm = int(line[3])
            to = int(line[5])

            for _ in range(steps):
                cargo[to].append(cargo[frm].pop())

    return cargo

def cargo_reorg_pt2(cargo, file_name):
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip().split(' ')
            steps = int(line[1])
            frm = int(line[3])
            to = int(line[5])

            tmp_stack = []

            for _ in range(steps):
                try:
                    frm_crate = cargo[frm].pop()
                except:
                    break
                tmp_stack.append(frm_crate)

            tmp_stack.reverse()

            for i in tmp_stack:
                cargo[to].append(i)

    return cargo

if __name__ == '__main__':
    cargo = {
        1:['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
        2:['D', 'N', 'T', 'S', 'B', 'Z'],
        3:['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
        4:['G', 'R', 'Z'],
        5:['Z', 'N', 'R', 'H'],
        6:['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
        7:['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
        8:['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
        9:['S', 'Q', 'P', 'W', 'N']
    }

    # pt1_cargo = cargo_reorg_pt1(cargo, 'input\d5_input.txt')
    # print("Part 1:")
    # for i in range(1,10):
    #     print(pt1_cargo[i][-1])

    # note: pt1 must be commented out or cargo is modified
    pt2_cargo = cargo_reorg_pt2(cargo, 'input\d5_input.txt')
    print("Part 2:")
    for i in range(1,10):
        print(pt2_cargo[i][-1])
