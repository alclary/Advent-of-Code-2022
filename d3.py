import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
alpha = lowercase + uppercase
alpha_dict = {}
for i in range(1, 53):
    alpha_dict[alpha[i-1]] = i

def rucksack_duplicates_sum(file_name):
    sum_of_dups = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()

            middle = int(len(line) // 2)
            compartment_1 = set(line[:middle])
            compartment_2 = set(line[middle:])

            set_to_char = ''.join(compartment_1.intersection(compartment_2))
            char_to_int = alpha_dict[set_to_char]
            sum_of_dups += char_to_int

    return sum_of_dups

def group_badges_sum(file_name):
    sum_of_badges = 0
    list_of_groups = []
    group = 0
    count = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            if count == 0:
                list_of_groups.append([])
            list_of_groups[group].append(set(line))
            count += 1
            if count == 3:
                group += 1
                count = 0

    for group in list_of_groups:
        common = group[0].intersection(group[1].intersection(group[2]))
        char = ''.join(common)
        value = alpha_dict[char]
        sum_of_badges += value

    return sum_of_badges

if __name__ == '__main__':
    print(rucksack_duplicates_sum('input\d3_input.txt'))
    print(group_badges_sum('input\d3_input.txt'))