class Node:
    def __init__(self, name, ftype, parent, size=0):
        self.name = name
        self.ftype = ftype
        self.size = int(size)
        self.parent = parent
        self.children = []
        self.level = 0

    def contains_child(self, name):
        if self.children != []:
            for child in self.children:
                if child.name == name:
                    return child
        return None

class Tree:
    def __init__(self) -> None:
        self.root = None
        self.tree_size = 0
        self._print_list = []

    def add_node(self, node, parent):
        if self.root is None:
            self.root == node
        else:
            parent.children.append(node)
            node.level = parent.level + 1
        self.tree_size += 1
        # percolate up new Node's size
        while parent is not None:
            parent.size += node.size
            parent = parent.parent
        return

    def print_tree(self):
        node = self.root
        Tree.printNodeAndChildren(node)
        return

    @staticmethod
    def printNodeAndChildren(node):
        if node is None:
            return
        else:
            print('  '*node.level + node.name + ' (' + node.ftype + "-" + str(node.size) + ')')
            if len(node.children) > 0:
                for child in node.children:
                    Tree.printNodeAndChildren(child)
            return

    @staticmethod
    def nodes_to_list_given_criteria(root, criteria_func, running_list=[]):
        node = root
        if node is not None:
            if len(node.children) > 0:
                for child in node.children:
                    running_list = Tree.nodes_to_list_given_criteria(child, criteria_func, running_list)
            if criteria_func(node):
                running_list.append(node)
        return running_list

def build_dir_structure(file_name: str):
    dir_tree = Tree()
    working_dir = None

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line[0] == '$':
                # drop command token and following space (i.e. $)
                line = line[2:]
                line = line.split()
                if line[0] == 'cd' and line[1] == "..":
                    working_dir = working_dir.parent
                elif line[0] == 'cd':
                    dir_name = line[1]
                    if working_dir is None:
                        root_node = Node(dir_name, 'dir', None)
                        dir_tree.root = root_node
                        working_dir = root_node
                    else:
                        working_dir_child = working_dir.contains_child(dir_name)
                        if working_dir_child is not None:
                            working_dir = working_dir_child
                            continue
                        else:
                            new_node = Node(dir_name, 'dir', working_dir)
                            dir_tree.add_node(new_node, working_dir)
                            working_dir = new_node
                            continue
            else:
                line = line.split(' ')
                if line[0] == 'dir':
                    size = 0
                    ftype = 'dir'
                else:
                    size = line[0]
                    ftype = 'file'
                new_node = Node(line[1], ftype, working_dir, size)
                dir_tree.add_node(new_node, working_dir)

    return dir_tree

if __name__ == '__main__':
    tree = build_dir_structure('input\d7_input.txt')
    tree.print_tree()

    # Day 7 problem 1
    # ____________________________________________

    # def under_100k(node):
    #     if node.size <= 100000 and node.ftype == 'dir':
    #         return True
    #     else:
    #         return False

    # meetsCriteria = []
    # meetsCriteria = Tree.nodes_to_list_given_criteria(tree.root, under_100k)

    # dir_sum = 0
    # for node in meetsCriteria:
    #     dir_sum += node.size

    # print("Sum of dirs >= 100k: " + str(dir_sum))

    # Day 7 problem 2
    # __________________________________________________
    # Total disk space = 70,000,000
    # Current used space = 40,913,445
    # Current free space = 29,086,555
    # Needed free space = 30,000,000
    # Difference = 913,445

    # def over_eq_913k(node):
    #     if node.size >= 913445 and node.ftype == 'dir':
    #         return True
    #     else:
    #         return False

    # meetsCriteria = []
    # meetsCriteria = Tree.nodes_to_list_given_criteria(tree.root, over_eq_913k)

    # min_size = 70000000
    # for node in meetsCriteria:
    #     if node.size < min_size:
    #         min_size = node.size

    # print("Min dir size to delete:" + str(min_size))