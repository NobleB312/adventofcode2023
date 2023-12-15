def read(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))

    arrays = [[time, distance] for time, distance in zip(time_values, distance_values)]

    return arrays


def find_solutions(array):
    records = []
    for time, distance in array:
        button = 0
        max_button = time
        local_records = []
        temp = []

        for _ in range(time):
            temp.append(button * max_button)
            max_button -= 1
            button += 1

        for index, item in enumerate(temp):
            if item > distance:
                local_records.append(index)

        records.append(local_records)
    return records


def permutation(records):
    total = 1
    for i in records:
        total *= len(i)
    return total


file_path = 'fin.txt'
print(permutation(find_solutions(read(file_path))))