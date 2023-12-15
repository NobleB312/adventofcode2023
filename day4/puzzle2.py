import re
total = 0


def read_scratchcards(file_path):
    scratchcards = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split("|")
            winning_numbers = [int(num) for num in parts[0].split() if num.isdigit()]
            numbers = [int(num) for num in parts[1].split() if num.isdigit()]
            scratchcards.append((winning_numbers, numbers))
    return scratchcards


def count_matching_numbers(winning_numbers, numbers):
    return len(set(winning_numbers).intersection(set(numbers)))


def process_scratchcards(scratchcards):
    total_count = len(scratchcards)
    copies = [1] * len(scratchcards)

    for i in range(len(scratchcards)):
        winning_numbers, numbers = scratchcards[i]
        matches = count_matching_numbers(winning_numbers, numbers)

        for j in range(i + 1, min(i + 1 + matches, len(scratchcards))):
            copies[j] += copies[i]

    total_count += sum(copies) - len(copies)
    return total_count


def process_points(file_path):
    total_points = 0
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split("|")

            winning_numbers = [int(num) for num in parts[0].split() if num.isdigit()]
            numbers = [int(num) for num in parts[1].split() if num.isdigit()]

            n = len(set(numbers).intersection(winning_numbers))

            if n != 0:
                n -= 1
                total_points += 2 ** n
    return total_points


file = "fin.txt"
scratchers = read_scratchcards(file)

print(process_scratchcards(scratchers))