class Node:
    def __init__(self, node_id, parent):
        self.id = node_id
        self.parent = parent
        self.row = 0
        self.column = 0
        self.visited = set()
        self.visited.add((self.row, self.column)) # initial visited

    def auto_move(self, direction):
        if direction == 'R':
            self.column += 1
        elif direction == 'L':
            self.column -= 1
        elif direction == 'U':
            self.row -= 1
        elif direction == 'D':
            self.row += 1
        self.visited.add((self.row, self.column))
        return

    def follow_parent(self):
        horizontal_diff = self.parent.column - self.column
        vertical_diff = self.parent.row - self.row
        # no move necessary
        if abs(vertical_diff) <= 1 and \
            abs(horizontal_diff) <= 1:
            return
        # pure vertical moves
        elif horizontal_diff == 0:
            if vertical_diff > 1:
                self.row = self.parent.row - 1
            elif vertical_diff < -1:
                self.row = self.parent.row + 1
        # pure horizontal moves
        elif vertical_diff == 0:
            if horizontal_diff < -1:
                self.column = self.parent.column + 1
            elif horizontal_diff > 1:
                self.column = self.parent.column - 1
        # diagnol left up move
        elif self.parent.column < self.column and\
            self.parent.row < self.row:
            self.column -= 1
            self.row -= 1
        # diagnol left down move
        elif self.parent.column < self.column and\
            self.parent.row > self.row:
            self.column -= 1
            self.row += 1
        # diagnol right up move
        elif self.parent.column > self.column and\
            self.parent.row < self.row:
            self.column += 1
            self.row -= 1
        # diagnol right down move
        elif self.parent.column > self.column and\
            self.parent.row > self.row:
            self.column += 1
            self.row += 1

        self.visited.add((self.row, self.column))
        return

def gen_movement_list(file_name):
    instruction_set = []

    with open(file_name, 'r') as infile:
        for line in infile:
            instructions = line.strip().split(' ')
            instructions[1] = int(instructions[1])  # cast steps to int
            instruction_set.append(instructions)    # instructions as list
    return instruction_set

if __name__ == '__main__':
    head = Node('H', None)
    tails = 9

    # Build Tail List
    parent = head
    tail_list = []
    count = 1
    for _ in range(tails):  # create # of tails
        new_node = Node(count, parent)
        tail_list.append(new_node)
        parent = new_node    # each successive node follows previous node
        count += 1

    movement_list = gen_movement_list('input\d9_input.txt')
    for instruction in movement_list:
        direction = instruction[0]
        steps = instruction[1]

        for _ in range(steps):
            head.auto_move(direction)

            for node in tail_list:
                node.follow_parent()

    print("Count:", len(tail_list[8].visited))