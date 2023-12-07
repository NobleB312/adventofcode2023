reference_cubes = {"red": 0, "green": 0, "blue": 0}
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


def calculate_power(cube_counts):
    return cube_counts["red"] * cube_counts["green"] * cube_counts["blue"]


def compare_color_counts(game_color_dict, reference_cubes):
    for color, count in game_color_dict.items():
        if count > reference_cubes[color]:
            reference_cubes[color] = count


total = 0
previous_game_id = None

for game_id, color_dict in parsed_games:
    if previous_game_id is not None and game_id != previous_game_id:
        total += calculate_power(reference_cubes)
        reference_cubes = {color: 0 for color in reference_cubes}

    compare_color_counts(color_dict, reference_cubes)
    previous_game_id = game_id

total += calculate_power(reference_cubes)

print(total)

