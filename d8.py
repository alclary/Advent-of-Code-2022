def gen_matrix(file_name):
    matrix = list()

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            matrix.append(line)
    return matrix

def max_left(matrix, row, column):
    if column != 0:
        return max([int(i) for i in matrix[row][:column]])
    else:
        return -1

def max_right(matrix, row, column):
    if column != len(matrix[column])-1:
        column = column + 1
        return max([int(i) for i in matrix[row][column:]])
    else:
        return -1

def max_above(matrix, row, column):
    temp_list = []
    if row != 0:
        for row_i in range(0, row):
            temp_list.append(int(matrix[row_i][column]))
        return max(temp_list)
    else:
        return -1

def max_below(matrix, row, column):
    temp_list = []
    if row != len(matrix)-1:
        for row_i in range(row + 1, len(matrix)):
            temp_list.append(int(matrix[row_i][column]))
        return max(temp_list)
    else:
        return -1

def view_count_left(matrix, row, column, element):
    if column == 0:
        return 0
    else:
        count = 1
        for i in range(column - 1, 0, -1):
            if int(matrix[row][i]) >= element:
                break
            else:
                count += 1
        return count

def view_count_right(matrix, row, column, element):
    if column == len(matrix[row]) - 1:
        return 0
    else:
        count = 1
        for i in range(column + 1, len(matrix[row])-1):
            if int(matrix[row][i]) >= element:
                break
            else:
                count += 1
        return count

def view_count_above(matrix, row, column, element):
    if row == 0:
        return 0
    else:
        count = 1
        for i in range(row - 1, 0, -1):
            if int(matrix[i][column]) >= element:
                break
            else:
                count += 1
        return count

def view_count_below(matrix, row, column, element):
    if row == len(matrix) - 1:
        return 0
    else:
        count = 1
        for i in range(row + 1, len(matrix)-1):
            if int(matrix[i][column]) >= element:
                break
            else:
                count += 1
        return count

if __name__ == '__main__':


    # Day 8, Problem 1
    #_____________________________________________________________
    matrix = gen_matrix('input\d8_input.txt')
    count = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            element = int(matrix[row][column])
            if element > max_left(matrix, row, column) or \
                element > max_right(matrix, row, column) or \
                element > max_above(matrix, row, column) or \
                element > max_below(matrix, row, column):
                count += 1

    print("Visisble tree count:",count)

    # Day 8, Problem 2
    #_____________________________________________________________
    matrix = gen_matrix('input\d8_input.txt')

    scenic_score_list = []

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            element = int(matrix[row][column])
            view_left = view_count_left(matrix, row, column, element)
            view_right = view_count_right(matrix, row, column, element)
            view_above = view_count_above(matrix, row, column, element)
            view_below = view_count_below(matrix, row, column, element)
            ss = view_left * view_right * view_above * view_below
            scenic_score_list.append(ss)


    print('Max scenic score:', max(scenic_score_list))



