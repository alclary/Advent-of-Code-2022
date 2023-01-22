def group_overlap_completely(file_name):
    overlap_count = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            ranges = line.split(',')
            range_1 = ranges[0].split('-')
            range_2 = ranges[1].split('-')

            if int(range_1[0]) >= int(range_2[0]) and \
                int(range_1[1]) <= int(range_2[1]):
                overlap_count += 1
            elif int(range_2[0]) >= int(range_1[0]) and \
                int(range_2[1]) <= int(range_1[1]):
                overlap_count += 1

    return overlap_count

def group_overlap_at_all(file_name):
    disjoint_count = 0
    total_lines = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line is not None and line != '':
                total_lines += 1
            ranges = line.split(',')
            range_1 = ranges[0].split('-')
            range_2 = ranges[1].split('-')

            if (int(range_1[1]) < int(range_2[0])) or \
                (int(range_2[1]) < int(range_1[0])):
                disjoint_count += 1

    overlap_count = total_lines - disjoint_count

    return overlap_count

if __name__ == '__main__':
    print(group_overlap_completely('input\d4_input.txt'))
    print(group_overlap_at_all('input\d4_input.txt'))