class Node:
    def __init__(self, x, y, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.value = ord(self.alpha) - 96 # convert lowercase alpha
        self.prior = None
        self.neighbors = []
        self.isStart = False
        self.isEnd = False

    def test_add_neighbor(self, neighbor, visited):
        if neighbor != self.prior and \
            neighbor.value <= self.value + 1 and \
            neighbor not in visited:

            neighbor.prior = self
            self.neighbors.append(neighbor)
        return

def gen_matrix(file_name):
    matrix = []

    with open(file_name, 'r') as infile:
        x = 0
        for line in infile:
            line = line.strip()
            nodeLine = []
            y = 0
            for char in line:
                # create node obj
                node = Node(x, y, char)
                # identify and edit start and finish nodes
                if node.alpha == 'S':
                    node.isStart = True
                    node.value = 1 # start has value of 'a'
                elif node.alpha == 'E':
                    node.isEnd = True
                    node.value = 26 # end has value of 'z'
                nodeLine.append(node)
                y += 1
            matrix.append(nodeLine)
            x += 1
    return matrix

def traverse_matrix(matrix):
    # find the start node
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if matrix[i][j].isStart:
                node = matrix[i][j]
                break

    prior = None
    queue = []
    visited = []

    while node.isEnd is not True:
        # identify neighbors, add to node's neighbors, set neighbor's prior:
        if node.x > 0:
            node.test_add_neighbor(matrix[node.x-1][node.y], visited)
        if node.y > 0:
            node.test_add_neighbor(matrix[node.x][node.y-1], visited)
        if node.x < len(matrix) - 1:
            node.test_add_neighbor(matrix[node.x+1][node.y], visited)
        if node.y < len(row) - 1:
            node.test_add_neighbor(matrix[node.x][node.y+1], visited)

        # add node's neighbor's to queue if they are not already in
        for neighbor in node.neighbors:
            if neighbor not in queue:
                queue.append(neighbor)

        # add node to visited list
        visited.append(node)
        node = queue.pop(0)

    path = []

    while node.prior is not None:
        path.append(node.alpha)
        node = node.prior

    path.append(node.alpha) # append start node; final in reverse path
    path.reverse() # reverse path; start to finish

    return path

if __name__ == '__main__':
    matrix = gen_matrix('input\d12_input.txt')
    path = traverse_matrix(matrix)
    print(path)
    print(len(path)-1) # start doesn't count as step