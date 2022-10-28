def total_func(first_line, second_line):
    total_line = first_line + second_line
    for i_one in range(1, len(total_line)):
        for i_two in range(i_one + 1, len(total_line)):
            if total_line[i_one] > total_line[i_two]:
                total_line[i_one], total_line[i_two] = total_line[i_two], total_line[i_one]
    return total_line

first_line = list(range(160, 177, 2))
second_line = list(range(162, 181, 3))

print('Отсортированный список учеников:', total_func(first_line, second_line))