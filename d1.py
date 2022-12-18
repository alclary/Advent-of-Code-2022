def count_elf_calories(file_name):
    elf_list = [0]
    elf_in_list = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            clean_line = line.strip()
            if line.strip() == '':
                elf_in_list += 1
                elf_list.append(0)
                continue
            else:
                elf_list[elf_in_list] += int(clean_line)

    return elf_list

if __name__ == '__main__':
  elf_calories = count_elf_calories('input\d1_input.txt')
  elf_calories.sort(reverse=True)
  total_cal = sum(elf_calories[0:3])
  print(total_cal)