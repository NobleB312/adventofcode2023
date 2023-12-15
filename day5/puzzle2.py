def read(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    race_time = int(lines[0].split(':')[1].replace(' ', ''))
    record_distance = int(lines[1].split(':')[1].replace(' ', ''))

    return race_time, record_distance

def find_record(race_time, record_distance):
    ways = 0
    for time in range(1, race_time):
        if time * (race_time - time) > record_distance:
            ways += 1
    return ways


file_path = 'fin.txt'
race_time, record_distance = read(file_path)
print(find_record(race_time, record_distance))