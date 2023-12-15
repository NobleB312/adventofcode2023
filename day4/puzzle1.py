total = 0

with open('fin.txt', 'r') as f:
    for line in f:
        parts = line.split("|")

        winning_numbers = [int(num) for num in parts[0].split() if num.isdigit()]
        numbers = [int(num) for num in parts[1].split() if num.isdigit()]

        n = len(set(numbers).intersection(winning_numbers))

        if n != 0:
            n -= 1
            total += 2 ** n
print(total)