file = open('fin.txt', 'r')
schematics = []
part_numbers = []

for line in file:
    line = line.strip()
    schematics.append(line)

def isPartNumber(line_index, start_index, end_index):
    if start_index > 0:
        before_start = start_index - 1
        if not schematics[line_index][before_start].isdigit() and schematics[line_index][before_start] != '.':
            return True
    else:
        before_start = 0

    if end_index == len(schematics[0]) - 1:
        after_end = end_index
    else:
        after_end = end_index + 1
        if not schematics[line_index][after_end].isdigit() and schematics[line_index][after_end] != '.':
            return True

    if line_index > 0:
        for i in range(before_start, after_end + 1):
            if not schematics[line_index - 1][i].isdigit() and schematics[line_index - 1][i] != '.':
                return True
    if line_index < len(schematics) - 1:
        for i in range(before_start, after_end + 1):
            if not schematics[line_index + 1][i].isdigit() and schematics[line_index + 1][i] != '.':
                return True
    return False


for line_index in range(len(schematics)):
    column_index = 0
    while column_index < len(schematics[0]):
        if schematics[line_index][column_index].isdigit():
            start = column_index
            column_index += 1
            while column_index < len(schematics[line_index]) and schematics[line_index][column_index].isdigit():
                column_index += 1
            end = column_index - 1
            if isPartNumber(line_index, start, end):
                part_numbers.append(int(schematics[line_index][start:end+1]))
        column_index += 1

print(sum(part_numbers))
