reference_cubes = {"red": 12, "green": 13, "blue": 14}

parsed_games = []

with open('fin.txt', 'r') as f:
    for line in f:
        game_id, game_descriptions = line.split(': ', 1)
        game_id = game_id.strip()
        games = game_descriptions.split(';')

        for game in games:
            color_counts = game.split(',')
            color_dict = {"red": 0, "green": 0, "blue": 0}

            for color_count in color_counts:
                count, color = color_count.strip().split()
                color_dict[color] += int(count)

            parsed_games.append((game_id, color_dict))

def compare_color_counts(game_color_dict, reference_dict):
    for color, count in game_color_dict.items():
        if count > reference_dict[color]:
            return True
    return False

correct_games = []

for game_id, color_dict in parsed_games:
    if compare_color_counts(color_dict, reference_cubes):
        correct_games.append(game_id)

result = []
for i in correct_games:
    if i not in result:
        result.append(i)

total = 0

for i in result:
    game_number_str = i.split()[1]
    game_number = int(game_number_str)
    total += game_number

print(5050 - total)